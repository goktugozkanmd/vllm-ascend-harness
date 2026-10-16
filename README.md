<!-- Evolved from OpenHarness -->

# vllm-ascend-harness

> An agent & evaluation harness evolved from OpenHarness for vLLM-Ascend, supporting LLM regression, code agent and sandboxed task execution on Ascend NPU.

**vllm-ascend-harness** 是 vLLM-Ascend 社区孵化的 Agent 与评测基座，基于 **OpenHarness** 演进打造。面向昇腾 NPU 推理场景，提供可隔离的任务沙箱、Agent 执行主循环、遥测采集、批量回归评测能力，用于模型回归验证、代码检视、CI 自动化任务，支撑 vLLM-Ascend 工程防护与效能建设。

---

## 项目定位

vllm-ascend-harness 是一个面向昇腾 NPU 推理场景的 Agent 与评测基座，用于：

- **模型回归验证**：批量回归评测，采集回归指标，保障 vLLM-Ascend 推理质量。
- **代码 Agent 任务**：提供代码读取、PR 检视、命令执行等内置 Skill，支撑 CI 自动化任务。
- **任务沙箱隔离**：容器隔离、命令白名单，对接天罗地网防护体系，保障执行安全。

本项目在 **OpenHarness** 基础上演进，保留上游溯源声明，重大架构变更需要社区 RFC 讨论。

## 能力范围

| 模块 | 说明 |
| --- | --- |
| `core` | 微内核：Agent 主循环、事件总线、插件管理器，继承 OpenHarness 设计思想 |
| `adapters` | 模型后端适配器，优先实现 vllm-ascend 推理后端适配 |
| `sandbox` | 任务沙箱模块：容器隔离、命令白名单，对接天罗地网防护体系 |
| `evaluator` | 评测模块：批量任务执行、打分器、AIS-Bench 接入层、回归指标采集 |
| `telemetry` | 遥测埋点、日志、token 统计、工件收集 |
| `skills` | 内置 Skill：代码读取、PR 检视、命令执行等工具集 |

## 快速上手

### 环境要求

- Python >= 3.9
- 昇腾 NPU 驱动与 CANN 环境（推理后端适配需要）
- vllm-ascend（推理后端，可选）

### 安装

```bash
git clone https://github.com/vllm-ascend/vllm-ascend-harness.git
cd vllm-ascend-harness
pip install -e .
```

### 运行示例

单轮 Agent 任务：

```bash
python examples/run_agent.py --prompt "Hello, vllm-ascend!"
```

Nightly 回归评测：

```bash
python examples/run_regression_eval.py --config examples/regression_config.yaml
```

## 贡献指引

我们欢迎社区贡献！请参阅 [贡献指南](docs/contributing.md) 了解如何参与本项目。

**注意**：本项目在 OpenHarness 基础上演进，重大架构变更需要社区 RFC 讨论。

## 上游溯源

本项目基于 **OpenHarness** 演进而来，保留上游开源声明与许可证（MIT License）。感谢 OpenHarness 社区提供的基础架构与设计思想。

## 开源协议

本项目基于 [MIT License](LICENSE) 开源。

---

# vllm-ascend-harness (English)

**vllm-ascend-harness** is an agent & evaluation harness evolved from **OpenHarness**, incubated by the vLLM-Ascend community. It targets Ascend NPU inference scenarios, providing isolated task sandboxes, an agent execution main loop, telemetry collection, and batch regression evaluation capabilities for model regression verification, code review, and CI automation tasks — supporting vLLM-Ascend engineering protection and efficiency.

## Overview

| Module | Description |
| --- | --- |
| `core` | Micro-kernel: agent loop, event bus, plugin manager — inheriting OpenHarness design philosophy |
| `adapters` | Model backend adapters, prioritizing vllm-ascend inference backend |
| `sandbox` | Task sandbox: container isolation, command allowlist, integrated with the defense system |
| `evaluator` | Evaluation: batch task execution, scorers, AIS-Bench integration, regression metrics |
| `telemetry` | Telemetry, logging, token statistics, artifact collection |
| `skills` | Built-in skills: code reading, PR review, command execution |

## Quick Start

```bash
git clone https://github.com/vllm-ascend/vllm-ascend-harness.git
cd vllm-ascend-harness
pip install -e .
python examples/run_agent.py --prompt "Hello, vllm-ascend!"
```

## Contributing

See [Contributing Guide](docs/contributing.md). Note: this project evolves from OpenHarness; major architectural changes require community RFC discussion.

## Upstream Attribution

This project is evolved from **OpenHarness**, retaining the upstream open-source notice and MIT License. We thank the OpenHarness community for the foundational architecture and design philosophy.

## License

[MIT License](LICENSE).
