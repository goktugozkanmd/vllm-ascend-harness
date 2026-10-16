# Architecture Overview

## 概述

vllm-ascend-harness 是 vLLM-Ascend 社区孵化的 Agent 与评测基座，基于 **OpenHarness** 演进打造。面向昇腾 NPU 推理场景，提供可隔离的任务沙箱、Agent 执行主循环、遥测采集、批量回归评测能力。

## 架构分层

```
┌──────────────────────────────────────────────────┐
│                   Examples / CLI                   │
├──────────────────────────────────────────────────┤
│  Evaluator          │  Skills (PR review, ...)    │
├──────────────────────────────────────────────────┤
│                   Core (Agent Loop)                │
│        Event Bus  │  Plugin Manager               │
├──────────────────────────────────────────────────┤
│  Adapters (vllm-ascend)  │  Sandbox (container)    │
├──────────────────────────────────────────────────┤
│                   Telemetry                        │
│        Logger  │  Token Stats  │  Artifacts       │
└──────────────────────────────────────────────────┘
```

## 核心模块

### Core（微内核）

- **AgentLoop**: Agent 执行主循环，编排 plan-act-observe 周期。
- **EventBus**: 进程内发布/订阅事件总线，实现模块间解耦通信。
- **PluginManager**: 插件注册中心，提供 Skill / Adapter / Scorer 的运行时发现与调用。

设计继承 OpenHarness 的微内核思想，核心仅定义接口契约，具体实现通过插件注入。

### Adapters（模型后端适配器）

- **BaseModelAdapter**: 所有推理后端的统一接口。
- **VllmAscendAdapter**: vllm-ascend 推理后端适配器（首要实现目标）。

扩展点：通过继承 `BaseModelAdapter` 可接入任意推理后端。

### Sandbox（任务沙箱）

- **BaseSandbox**: 沙箱接口，定义 `setup/run/teardown` 契约。
- **ContainerSandbox**: 容器隔离实现，对接天罗地网防护体系。
- **CommandWhitelist**: 命令白名单，阻止危险操作。

### Evaluator（评测模块）

- **EvalRunner**: 批量任务执行器，遍历任务集合并采集指标。
- **BaseScorer**: 打分器接口，支持自定义评分策略。
- **AISBenchScorer**: AIS-Bench 接入层，提供标准化回归指标。

扩展点：通过继承 `BaseScorer` 可实现自定义打分策略。

### Telemetry（遥测）

- **Logger**: 统一日志工厂。
- **TokenStatsCollector**: Token 用量统计与聚合。
- **ArtifactCollector**: 运行工件收集与组织。

### Skills（内置技能）

- **BaseSkill**: 技能接口，Agent 可调用的工具集。
- **CodeReadSkill**: 代码读取。
- **PRReviewSkill**: PR 自动检视。
- **CommandExecSkill**: 沙箱内命令执行。

扩展点：通过继承 `BaseSkill` 可注册自定义 Agent 技能。

## 扩展点汇总

| 扩展点 | 基类 | 用途 |
| --- | --- | --- |
| 插件注册 | `core.PluginManager` | 运行时发现与调用 Skill / Adapter / Scorer |
| 模型适配器 | `adapters.BaseModelAdapter` | 接入新推理后端 |
| 自定义打分器 | `evaluator.BaseScorer` | 实现自定义评分策略 |
| Agent 技能 | `skills.BaseSkill` | 注册新 Agent 工具能力 |
| 沙箱实现 | `sandbox.BaseSandbox` | 接入新隔离策略 |

## 上游溯源

本项目在 **OpenHarness** 基础上演进，保留上游设计思想与溯源声明。重大架构变更需要社区 RFC 讨论。
