import nonebot
from nonebot.adapters.qq import Adapter as QQAdapter

nonebot.init()
driver = nonebot.get_driver()
driver.register_adapter(QQAdapter)
nonebot.load_plugins("plugins")

app = nonebot.get_asgi()

# 调试：打印所有注册的路由
for route in app.routes:
    print(f"Route: {route.path}")

if __name__ == "__main__":
    nonebot.run(app="bot:app")
