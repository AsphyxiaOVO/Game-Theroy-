# Game-Theroy-

> 中文：物联网多播路由博弈算法复现项目  
> English: A reproduction project for game-theoretic multicast routing algorithms in IoT

## 中文说明

### 项目简介

本项目围绕论文《A Game-Theoretic Approach for Cost-Effective Multicast Routing in the Internet of Things》展开，重点复现其中两个核心部分：

- `PSA`（路径选择算法，Path Selection Algorithm）
- `Potential Function Value`（潜在函数值计算）

项目目标是用 Python 复现论文中的基本思路，并通过示例网络观察多播路由在博弈更新过程中的变化。

### 项目内容

本仓库主要完成了以下工作：

- 使用 `networkx` 构建示例网络拓扑
- 实现路径选择配置的初始化与迭代更新
- 通过路径成本比较，近似寻找多播树中的纯纳什均衡
- 计算潜在函数值，用于衡量当前路由配置的整体效率与成本表现
- 保留示例图像，辅助展示网络结构与实验结果

### 仓库结构

| 文件 | 说明 |
| --- | --- |
| `Algorithm1(PSA).py` | PSA 算法的基础复现，展示路径如何迭代到稳定状态 |
| `Algorithm2(Potential Function Value).py` | 潜在函数值的计算实现 |
| `an example.py` | 更复杂网络下的综合示例，打印路径与潜在函数值 |
| `Figure_1.png` | 论文或实验相关示意图 |
| `picture of the example.py` | 示例脚本对应的结果图或辅助图片 |
| `README.md` | 仓库说明文档 |

### 依赖环境

当前脚本主要依赖：

```bash
pip install networkx
```

说明：

- `random` 为 Python 标准库的一部分，无需额外安装。
- 当前仓库中的核心脚本主要通过终端输出结果，不依赖复杂的可视化框架。

### 运行方式

#### 1. 运行 PSA 复现

```bash
python "Algorithm1(PSA).py"
```

该脚本会：

- 构造一个简单的无向带权网络
- 为目标节点随机初始化路径
- 通过多轮更新选择成本更低的路径
- 输出最终的路径选择配置

#### 2. 运行潜在函数值计算

```bash
python "Algorithm2(Potential Function Value).py"
```

该脚本会：

- 为给定的路径配置计算潜在函数值
- 用于评估整体多播路由配置的代价表现

#### 3. 运行综合示例

```bash
python "an example.py"
```

该脚本会：

- 构造更复杂的网络拓扑
- 为多个目标节点分配初始路径
- 在迭代过程中输出每个目标节点当前路径、路径成本和潜在函数值
- 最后打印收敛后的路径选择结果

### 适合理解的重点

- `PSA` 更偏向“每个目标节点怎么选路”
- `Potential Function Value` 更偏向“当前整棵多播树整体好不好”
- 两者结合后，可以同时观察“个体策略变化”和“系统整体成本变化”

### 项目特点与局限

- 适合用于理解论文中的核心算法思路与基本流程
- 代码结构直观，便于继续改造成更多网络拓扑实验
- 当前实现偏重教学复现，示例网络规模较小
- 部分实现采用了简化建模，更适合课程展示，而不是直接用于真实网络部署

## English Overview

### Summary

This repository reproduces two core ideas from the paper *A Game-Theoretic Approach for Cost-Effective Multicast Routing in the Internet of Things*:

- `PSA` for path selection
- `Potential Function Value` for evaluating routing efficiency

The code uses small graph examples to show how multicast routing strategies evolve and how the potential function can be used to assess the overall routing configuration.

### Repository Structure

| File | Purpose |
| --- | --- |
| `Algorithm1(PSA).py` | Basic PSA reproduction |
| `Algorithm2(Potential Function Value).py` | Potential function calculation |
| `an example.py` | A larger end-to-end example |
| `Figure_1.png` | Related illustration |
| `picture of the example.py` | Example-related output image |

### Quick Start

Install dependency:

```bash
pip install networkx
```

Run the scripts:

```bash
python "Algorithm1(PSA).py"
python "Algorithm2(Potential Function Value).py"
python "an example.py"
```

### Notes

- The repository is mainly intended for paper reproduction and teaching.
- The current examples use relatively small and simplified graph settings.
- The scripts are useful for understanding the interaction between path updates and global routing efficiency.
