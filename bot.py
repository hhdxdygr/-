import nonebot
from nonebot.adapters.qq import Adapter as QQAdapter  # 确认导入的是 QQ 适配器

nonebot.init()
driver = nonebot.get_driver()
driver.register_adapter(QQAdapter) 

nonebot.load_plugins("plugins")

app = nonebot.get_asgi()


if __name__ == "__main__":
    nonebot.run(app="bot:app")