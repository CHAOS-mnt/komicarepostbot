# K岛讨论串转发bot

## 使用教程

环境：python3

1.将 `bot.ini.example` 重命名为 `bot.ini` ,并修改配置文件

2.执行 `python3 main.py` 

### Config example

```
[Telegram]
token = //bot token
channelid = //@yourchannelid

[Program]
lastpostnumber = //贴文号，用于从指定回复开始转发，从头开始转发则填0
lastpostposition = //最后转发的回复在串里的序号，从头开始转发写填0，否则请填任意大于0的数字
url = //要转发的串的json格式完整url, e.g:https://majeur.zawarudo.org/virtuelles/res/181499.json
```
## Bug
- 在 IBM CF 上运行时一旦崩溃重启会导致配置文件回档（并不是程序的bug）
- 不明原因崩溃，因没有本地持久log导致debug困难

## To do

- 自动识别最后转发贴文并继续转发后面的贴文，不再依赖配置文件
- 重构，要优雅
- 自动识别新串，并在旧串一定时间无回复后停止爬取