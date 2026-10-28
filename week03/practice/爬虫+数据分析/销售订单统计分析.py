"""
销售订单统计分析模块

提供销售数据的加载、处理、统计和可视化功能。

## 输出文件格式
- 折线图：每天销售额变化趋势
- 柱状图：不同城市累计销售数量对比
- 饼状图：不同产品类型订单比例
- 饼状图：不同支付方式订单比例
"""

from typing import Tuple, Dict, Any
import pandas as pd
import matplotlib.pyplot as plt
import os


# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']


def load_and_clean_data(file_path: str) -> pd.DataFrame:
    """
    加载并清洗销售数据。
    
    参数:
        file_path: CSV文件路径
        
    返回:
        清洗后的DataFrame，包含销售额列
        
    异常:
        FileNotFoundError: 当数据文件不存在时抛出
    """
    # 读取数据
    data = pd.read_csv(
        file_path,
        usecols=['产品类别', '销售数量', '单价', '客户所在城市', '订单日期', '支付方式']
    )
    
    # 计算销售额
    data['销售额'] = data['销售数量'] * data['单价']
    
    # 处理异常值
    # 删除缺失值
    data = data.dropna()
    
    # 将单价为负的取绝对值
    data['单价'] = data['单价'].abs()
    
    # 统一日期格式
    data['订单日期'] = data['订单日期'].str.replace('/', '-')
    
    return data


def plot_daily_sales(ax: plt.Axes, data: pd.DataFrame) -> None:
    """
    绘制每天销售额变化的折线图。
    
    参数:
        ax: matplotlib Axes对象
        data: 销售数据DataFrame
    """
    daily_sales = data.groupby('订单日期')['销售额'].sum()
    
    x = daily_sales.index.tolist()
    y = daily_sales.values.tolist()
    
    ax.plot(x, y)
    ax.set_title('每天销售额变化', fontsize=20)
    ax.set_xlabel('订单日期', fontsize=15)
    ax.set_ylabel('销售额', fontsize=15)
    ax.set_xticks(x[::50])
    ax.grid(linestyle='--', alpha=0.5)


def plot_city_sales(ax: plt.Axes, data: pd.DataFrame) -> None:
    """
    绘制不同城市累计销售数量的柱状图。
    
    参数:
        ax: matplotlib Axes对象
        data: 销售数据DataFrame
    """
    city_sales = data.groupby('客户所在城市')['销售数量'].sum()
    
    x = city_sales.index.tolist()
    y = city_sales.values.tolist()
    
    ax.bar(x, y, width=0.8)
    ax.set_title('不同城市累计销售数量', fontsize=20)
    ax.set_xlabel('城市', fontsize=15)
    ax.set_ylabel('销售数量', fontsize=15)
    ax.grid(linestyle='--', alpha=0.5)


def plot_product_type_sales(ax: plt.Axes, data: pd.DataFrame) -> None:
    """
    绘制不同产品类型对应的订单比例饼状图。
    
    参数:
        ax: matplotlib Axes对象
        data: 销售数据DataFrame
    """
    product_type_sales = data.groupby('产品类别')['销售数量'].sum()
    
    x = product_type_sales.index.tolist()
    y = product_type_sales.values.tolist()
    
    ax.pie(y, labels=x, autopct='%1.2f%%')
    ax.set_title('不同产品类型对应的订单比例', fontsize=20)
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))


def plot_payment_method_sales(ax: plt.Axes, data: pd.DataFrame) -> None:
    """
    绘制不同支付方式对应的订单比例饼状图。
    
    参数:
        ax: matplotlib Axes对象
        data: 销售数据DataFrame
    """
    payment_method_sales = data.groupby('支付方式')['销售数量'].sum()
    
    x = payment_method_sales.index.tolist()
    y = payment_method_sales.values.tolist()
    
    ax.pie(y, labels=x, autopct='%1.2f%%')
    ax.set_title('不同支付方式对应的订单比例', fontsize=20)
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))


def create_visualization(data: pd.DataFrame, output_path: str = 'data/销售订单统计分析.png') -> None:
    """
    创建销售数据可视化图表。
    
    参数:
        data: 销售数据DataFrame
        output_path: 图片保存路径
    """
    # 创建画布
    fig, axes = plt.subplots(2, 2, figsize=(20, 10), dpi=100)
    fig.suptitle('销售订单统计分析', fontsize=25, y=0.95)
    fig.subplots_adjust(wspace=0.3, hspace=0.3)
    
    # 获取子图
    ax1: plt.Axes = axes[0, 0]
    ax2: plt.Axes = axes[0, 1]
    ax3: plt.Axes = axes[1, 0]
    ax4: plt.Axes = axes[1, 1]
    
    # 绘制各个图表
    plot_daily_sales(ax1, data)
    plot_city_sales(ax2, data)
    plot_product_type_sales(ax3, data)
    plot_payment_method_sales(ax4, data)
    
    # 保存图片
    os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
    plt.savefig(output_path, dpi=100)
    
    # 显示图片
    plt.show()


def get_sales_statistics(data: pd.DataFrame) -> Dict[str, Any]:
    """
    获取销售数据统计摘要。
    
    参数:
        data: 销售数据DataFrame
        
    返回:
        包含统计信息的字典
    """
    return {
        '总销售额': data['销售额'].sum(),
        '总销售数量': data['销售数量'].sum(),
        '订单数量': len(data),
        '平均订单金额': data['销售额'].mean(),
        '城市数量': data['客户所在城市'].nunique(),
        '产品类型数量': data['产品类别'].nunique(),
        '支付方式数量': data['支付方式'].nunique()
    }


def main() -> None:
    """
    主函数：执行销售订单分析流程。
    """
    # 数据文件路径
    base_path = os.path.dirname(__file__)
    csv_path = os.path.join(base_path, "csv_data", "sales.csv")
    data_file = pd.read_csv(csv_path)
    
    # 检查数据文件是否存在
    if not os.path.exists(data_file):
        print(f"错误：数据文件 '{data_file}' 不存在")
        return
    
    print("正在加载数据...")
    data = load_and_clean_data(data_file)
    
    print("\n数据统计摘要：")
    stats = get_sales_statistics(data)
    for key, value in stats.items():
        print(f"  {key}: {value:,.2f}" if isinstance(value, float) else f"  {key}: {value}")
    
    print("\n正在生成可视化图表...")
    create_visualization(data)
    print("图表已保存到 'data/销售订单统计分析.png'")


if __name__ == '__main__':
    main()
