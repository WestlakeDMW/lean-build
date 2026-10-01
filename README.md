# lean-build

控制 agent 主动扩张的防御性工程工作，同时完整实现当前需求。默认档位为 **Low**。

这是指令型 Skill，可约束 agent 的工程选择和验证范围；它不会更改 GPT 模型参数，也不承诺所有模型和会话都绝对遵循。

## 三个档位

| 档位 | 行为 | 默认验证 |
| --- | --- | --- |
| Enable | 对具体相关故障添加适量处理，保留有价值的解释，避免假想需求 | 初步验证 |
| Low | 保留必要校验与有信息量的简短注释，避免额外兜底和通用框架 | 初步验证 |
| Disable | 不主动添加可选防御、解释性注释、兼容层或加固措施 | 初步验证 |

所有档位都必须完整实现需求、保留必要保护、修复自己引入的问题。切换档位不授权删除既有保护、测试或质量门禁。

初步验证按需选择一个相关构建、编译、类型或静态检查，加最多三个直接相关的冒烟场景；只做有用的检查，不重复等价检查。完整功能测试、全面回归、安全审计及压力测试需用户单独明确指定范围，授权只适用于本次任务。

## 安装

将仓库作为完整 Skill 文件夹克隆到目标项目：

```sh
git clone https://github.com/WestlakeDMW/lean-build.git .agents/skills/lean-build
```

个人级安装可改用 `~/.agents/skills/lean-build`。请勿覆盖同名现有目录。Skill 入口、引用和辅助工具要一起保留。Codex 的项目与个人发现路径见[官方 Skill 文档](https://learn.chatgpt.com/docs/build-skills)。

## 使用

```text
使用 $lean-build，将当前项目的防御性构筑设置为 Low。
```

```text
使用 $lean-build，仅本次任务临时设为 Disable，完成这个修改并检查一下。
```

```text
使用 $lean-build，切换到 Enable；对登录和密码重置流程执行完整功能测试。
```

启用后，每条面向用户的文字消息以实际状态开头，例如：

```text
Defensive Construction: Low
```

进度和最终答复显示该行，应用界面、源码注释、工具参数及生成文档不添加状态横幅。Disable 是工程档位，不是停用 Skill。

每次实现或修改后的交付仅提醒一次实际验证情况。纯讨论、规划、进度和档位切换不重复提醒；未执行、失败或受阻的检查不能写成 passed。

## 按需读取的文件

```text
lean-build/
├── SKILL.md                  # 英文入口：状态、档位、范围、注释、验证、交付
├── agents/openai.yaml        # Codex 展示信息
├── references/
│   ├── validation.md         # 选择验证、授权边界、典型场景
│   └── persistence.md        # 持久化步骤、完整英文 Soul.md 区块
├── scripts/update_soul.py    # 可选的区块更新与回读工具，仅依赖 Python 3
└── README.md                 # 使用说明
```

通用关键边界直接放在 `SKILL.md`，不会隐藏在可选引用里；仅选择验证和保存配置时读取对应详细文件。

## Soul.md 与跨会话

首次持久启用默认创建项目根目录的 `Soul.md`；已有有效档位时沿用，明确切换才更新。完整英文规则保存在 `defensive-construction` 专属区块，只修改自己的区块并回读确认。临时档位和状态查询不写文件；无法持久化时只在会话执行并说明。

`Soul.md` 不在 Codex 默认指令发现文件名中。若希望每次任务自动读取，在项目实际生效的指令入口（通常是 `AGENTS.md`）中加入：

```text
At the start of each task, read the project-root Soul.md if it exists and apply its Defensive Construction Policy to this project.
```

Skill 不会自行修改该入口或全局配置。Codex 的入口优先级见[官方 AGENTS.md 文档](https://learn.chatgpt.com/docs/agent-configuration/agents-md)。

## 本次验证

- Skill 格式、展示元数据、相对引用路径及辅助工具语法检查通过。
- Soul.md 工具的创建、档位更新、区块外内容保留、重复调用不追加，以及异常区块拒绝修改检查通过。
- 独立 agent 在隔离购物车项目中采用临时 Disable，完成必需的折扣输入校验，只执行语法检查与三个相关冒烟场景；长期 Low 设置保持原样，未触发全量回归。

以上是一个工程场景的初步验证，尚未进行跨模型、多项目的行为评测或安全审计。
