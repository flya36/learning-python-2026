"""
TMDB-TOP300电影榜单数据统计
功能：
1. 统计TOP300的电影中,每一年上映的电影数量的变化。(折线图)
2. 统计对比不同语言电影数量。(柱状图)
3. 统计对比不同类型电影数量。(柱状图)
4. 统计对比各个电影评分的比例。(饼状图)

优化点（2026-10-21）：
- 加载数据时清洗字符串列（去除首尾空格），避免同一语言/类型因空格被拆成两根柱子
- 中文字体加入回退列表，并修复负号显示（axes.unicode_minus）
- 移除 SimHei 不支持的粗体标题，消除 findfont 警告
- 折线图横轴刻度补上最大年份，并标注数量最多的年份
- 柱状图按数量降序排序、柱顶标注数量，与语言图风格一致
- 饼图去掉与标签重叠的图例，百分比放扇区内部、评分标签放外部
- 图片保存路径改为相对脚本目录，任何目录下运行都能找到输出图
"""

import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple
import os


def setup_chinese_font():
    """设置中文显示"""
    # SimHei 若不存在则依次回退到微软雅黑/宋体
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'SimSun']
    # 修复中文环境下坐标轴负号显示为方块的问题
    plt.rcParams['axes.unicode_minus'] = False


def load_movie_data(file_path: str) -> pd.DataFrame:
    """
    加载电影数据

    Args:
        file_path: CSV文件路径

    Returns:
        DataFrame: 加载并清洗后的数据
    """
    usecols = ['电影名', '年份', '上映时间', '评分', '语言', '类型']
    data = pd.read_csv(file_path, usecols=usecols)

    # 清洗：去除文本首尾空格，防止"印地语"与"印地语 "被当成两种语言
    for col in ['电影名', '上映时间', '语言', '类型']:
        data[col] = data[col].astype('string').str.strip().replace('', pd.NA)

    # 数值列统一转为数值类型，非法值置为 NaN
    data['年份'] = pd.to_numeric(data['年份'], errors='coerce')
    data['评分'] = pd.to_numeric(data['评分'], errors='coerce')

    # 丢弃关键字段缺失的行
    data = data.dropna(subset=['年份', '评分', '语言', '类型'])

    return data


def count_movies_by_year(data: pd.DataFrame) -> Tuple[List[int], List[int]]:
    """
    统计每年上映的电影数量

    Args:
        data: 电影数据

    Returns:
        Tuple[List[int], List[int]]: (年份列表, 电影数量列表)
    """
    year_count = data.groupby('年份')['年份'].count()

    min_year = int(year_count.index.min())
    max_year = int(year_count.index.max())

    # 缺失年份补 0，保证折线图横轴连续
    years = list(range(min_year, max_year + 1))
    counts = [int(year_count.get(year, 0)) for year in years]

    return years, counts


def count_movies_by_language(data: pd.DataFrame) -> Tuple[List[str], List[int]]:
    """
    统计不同语言电影数量

    Args:
        data: 电影数据

    Returns:
        Tuple[List[str], List[int]]: (语言列表, 数量列表)
    """
    language_count = data.groupby('语言')['语言'].count().sort_values(ascending=False)

    languages = language_count.index.tolist()
    counts = language_count.values.tolist()

    return languages, counts


def count_movies_by_type(data: pd.DataFrame) -> Tuple[List[str], List[int]]:
    """
    统计不同类型电影数量

    Args:
        data: 电影数据

    Returns:
        Tuple[List[str], List[int]]: (类型列表, 数量列表)
    """
    type_count: Dict[str, int] = {}

    for types in data['类型'].str.split(','):
        for movie_type in types:
            movie_type = movie_type.strip()
            if movie_type:
                type_count[movie_type] = type_count.get(movie_type, 0) + 1

    # 按数量降序排序，与其他图表风格保持一致
    sorted_types = sorted(type_count.items(), key=lambda x: x[1], reverse=True)
    types_list = [item[0] for item in sorted_types]
    counts_list = [item[1] for item in sorted_types]

    return types_list, counts_list


def count_movies_by_score(data: pd.DataFrame, threshold: float = 0.02) -> Tuple[List, List]:
    """
    统计各评分电影数量占比，合并小数据

    Args:
        data: 电影数据
        threshold: 合并阈值，默认2%

    Returns:
        Tuple[List, List]: (评分列表, 数量列表)
    """
    score_count = data.groupby('评分')['评分'].count()
    total = score_count.sum()

    # 合并占比小于阈值的小评分段
    large_score = score_count.loc[score_count >= total * threshold]
    small_score = score_count.loc[score_count < total * threshold]

    if small_score.sum() > 0:
        large_score = large_score.copy()
        large_score['其它'] = small_score.sum()

    scores = large_score.index.tolist()
    counts = large_score.values.tolist()

    return scores, counts


def plot_year_trend(ax: plt.Axes, years: List[int], counts: List[int]) -> None:
    """
    绘制每年电影数量变化折线图

    Args:
        ax: 子图对象
        years: 年份列表
        counts: 数量列表
    """
    ax.plot(years, counts, color='green', linewidth=2)
    ax.set_title('每年电影数量变化', fontsize=16)
    ax.set_xlabel('年份', fontsize=12)
    ax.set_ylabel('电影数量', fontsize=12)

    # 刻度：每10年一个，且必须包含最大年份，避免折线画到刻度范围之外
    ticks = years[::10]
    if years[-1] not in ticks:
        ticks.append(years[-1])
    ax.set_xticks(ticks)

    y_max = max(counts) if counts else 30
    step = max(3, (y_max + 5) // 10)
    ax.set_yticks(list(range(0, y_max + 5, step)))
    ax.set_ylim(0, y_max + step)  # 顶部留白

    # 标注数量最多的年份
    peak_index = counts.index(max(counts))
    ax.annotate(f"{counts[peak_index]}部",
                xy=(years[peak_index], counts[peak_index]),
                xytext=(0, 8), textcoords='offset points',
                ha='center', fontsize=10, color='darkred')

    ax.grid(linestyle='--', alpha=0.5)


def plot_language_distribution(ax: plt.Axes, languages: List[str], counts: List[int]) -> None:
    """
    绘制不同语言电影数量柱状图

    Args:
        ax: 子图对象
        languages: 语言列表
        counts: 数量列表
    """
    bars = ax.bar(languages, counts, color='green', width=0.8)
    ax.set_title('不同语言电影数量', fontsize=16)
    ax.set_xlabel('语言', fontsize=12)
    ax.set_ylabel('数量', fontsize=12)
    ax.grid(linestyle='--', alpha=0.5, axis='y')
    ax.tick_params(axis='x', rotation=45, labelsize=9)

    # 柱顶标注数量
    for bar, count in zip(bars, counts):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
                str(count), ha='center', va='bottom', fontsize=8)
    ax.set_ylim(0, max(counts) * 1.12)  # 顶部留白给标注


def plot_type_distribution(ax: plt.Axes, types: List[str], counts: List[int]) -> None:
    """
    绘制不同类型电影数量柱状图

    Args:
        ax: 子图对象
        types: 类型列表
        counts: 数量列表
    """
    bars = ax.bar(types, counts, color='green', width=0.8)
    ax.set_title('不同类型电影数量', fontsize=16)
    ax.set_xlabel('类型', fontsize=12)
    ax.set_ylabel('数量', fontsize=12)
    ax.grid(linestyle='--', alpha=0.5, axis='y')
    ax.tick_params(axis='x', rotation=45, labelsize=9)

    # 柱顶标注数量
    for bar, count in zip(bars, counts):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
                str(count), ha='center', va='bottom', fontsize=8)
    ax.set_ylim(0, max(counts) * 1.12)


def plot_score_distribution(ax: plt.Axes, scores: List, counts: List) -> None:
    """
    绘制各评分电影数量占比饼状图

    Args:
        ax: 子图对象
        scores: 评分列表
        counts: 数量列表
    """
    # 评分标签放扇区外部，百分比放扇区内部；去掉图例避免与标签重叠
    ax.pie(counts, labels=scores, autopct='%.1f%%',)
    ax.set_title('不同评分电影数量占比', fontsize=16)
    ax.legend(loc='center',ncol =4,bbox_to_anchor=(0.5,-0.1),fontsize=10)



def create_visualization(data: pd.DataFrame, save_path: str = None) -> None:
    """
    创建可视化图表

    Args:
        data: 电影数据
        save_path: 图片保存路径，默认为None时不保存
    """
    # 设置中文显示
    setup_chinese_font()

    # 创建子图
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(22, 14), dpi=100)
    fig.suptitle('电影数据统计', fontsize=25, y=0.98)
    fig.subplots_adjust(
        top=0.90,      # 为总标题留出顶部空间（避免截断）
        bottom=0.10,   # 底部边距
        left=0.07,     # 左边距
        right=0.96,    # 右边距
        wspace=0.30,   # 子图水平间距
        hspace=0.45    # 子图垂直间距
    )

    # 获取子图
    ax1, ax2, ax3, ax4 = axes[0, 0], axes[0, 1], axes[1, 0], axes[1, 1]

    # 需求1: 每年电影数量变化
    years, year_counts = count_movies_by_year(data)
    plot_year_trend(ax1, years, year_counts)

    # 需求2: 不同语言电影数量
    languages, language_counts = count_movies_by_language(data)
    plot_language_distribution(ax2, languages, language_counts)

    # 需求3: 不同类型电影数量
    types, type_counts = count_movies_by_type(data)
    plot_type_distribution(ax3, types, type_counts)

    # 需求4: 各评分电影占比
    scores, score_counts = count_movies_by_score(data)
    plot_score_distribution(ax4, scores, score_counts)

    # 保存图片
    if save_path:
        # 确保目录存在
        os.makedirs(os.path.dirname(save_path) if os.path.dirname(save_path) else '.', exist_ok=True)
        plt.savefig(save_path, bbox_inches='tight', dpi=100)
        print(f"图表已保存至: {os.path.abspath(save_path)}")

    # 仅交互式后端才弹窗显示（Agg/PDF等无界面后端不弹窗，避免警告）
    import matplotlib
    if matplotlib.get_backend().lower() not in ('agg', 'pdf', 'ps', 'svg', 'template'):
        plt.show()
    plt.close(fig)  # 释放内存，避免重复运行产生堆积


def main():
    """主函数"""
    # 获取当前这个py脚本所在的文件夹
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # 拼接csv完整路径
    data_file = os.path.join(base_dir, 'csv_data', 'movie_list.csv')

    # 检查文件是否存在
    if not os.path.exists(data_file):
        print(f"错误: 数据文件 '{data_file}' 不存在!")
        print("请确保数据文件位于正确的位置")
        return

    # 加载数据
    print("正在加载数据...")
    data = load_movie_data(data_file)
    print(f"成功加载 {len(data)} 条电影数据")

    # 创建可视化（保存到脚本目录下的 data/ 文件夹，保证任何目录下运行都能找到）
    print("正在生成统计图表...")
    save_path = os.path.join(base_dir, 'data', 'movie_analysis.png')
    create_visualization(data, save_path)

    print("统计分析完成!")


if __name__ == '__main__':
    main()
