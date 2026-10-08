# 语音数据预处理工具（Audio Data Preprocessor）

## 项目简介
对真实语音与AI克隆语音的音频样本进行统一管理、统计与导出的预处理工具。基于面向对象设计（OOP），使用 dataclass 定义数据模型、组合模式实现数据集管理。

## 技术栈
- Python 3.10+
- 仅依赖标准库（dataclasses / pathlib / csv / json / logging）

## 目录结构
```
audio_preprocessor_v0.3/
├── src/
│   ├── models/          # 数据模型层：AudioSample / AudioDataset
│   ├── core/            # 业务逻辑层：parser（解析）、exporter（导出）
│   ├── utils/           # 通用工具层：logger（日志）
│   ├── config/          # 配置文件（占位）
│   └── main.py          # 程序入口
├── data/                # 输入音频数据（不提交Git）
├── output/              # 输出结果（不提交Git）
├── logs/                # 运行日志（不提交Git）
├── docs/                # 文档：数据规范
├── requirements.txt     # 依赖清单
└── .gitignore           # Git忽略规则
```

## 快速开始
1. 创建虚拟环境：`python -m venv venv`（Windows：`venv\Scripts\activate`）
2. 安装依赖：`pip install -r requirements.txt`（本版本无第三方依赖）
3. 运行：
   ```
   cd src
   python main.py
   ```
   或从 src 目录运行前先准备好 `../data/test_audio/` 下的音频文件。

## 输入数据规范
- 文件命名：`说话人ID_标签_序号.wav`，标签取 `real`（真实）或 `fake`（克隆）
- 示例：`speaker001_real_001.wav`、`speaker002_fake_003.wav`
- 详见 `docs/语音项目数据规范.md`

## 输出说明
- `output/audio_samples.csv`：样本明细（文件路径、说话人ID、标签、时长）
- `output/audio_stats.json`：数据集统计（总样本数、独立说话人数、标签分布、总时长）
- `logs/app.log`：运行日志

## 版本记录
- **v0.3**：OOP重构——dataclass数据模型 + 组合模式数据集管理，模块化分层（models/core/utils），加入异常处理与日志
