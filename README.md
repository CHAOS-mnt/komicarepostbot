# K岛讨论串转发bot

[![State-of-the-art Shitcode](https://img.shields.io/static/v1?label=State-of-the-art&message=Shitcode&color=7B5804)](https://github.com/trekhleb/state-of-the-art-shitcode)

## 使用教程

环境：python3

1.将 `bot.ini.example` 重命名为 `bot.ini` ,并修改配置文件

2.执行 `python3 main.py` 

### Config example

```
[Telegram]
token = //bot token
channel_id = //@yourchannelid

[Program]
last_post_position = 0 //最后转发的回复在串里的序号，从头开始转发写填0，否则请填任意大于0的数字
update_interval = 30 //刷新间隔时间
send_interval = 3 //发送间隔时间
url = //要转发的串的json格式完整url, e.g:https://majeur.zawarudo.org/virtuelles/res/181499.json
log_level = DEBUG //log等级
```
## Bug
- 不明原因崩溃，因没有本地持久log导致debug困难

## To do
- 重构，要优雅
- 自动识别新串，并在旧串一定时间无回复后停止爬取