import json
from bot.core import *
from utils.utils import load_class
def main():
    config = json.loads(open("config.json").read())
    print(config)
    bot = Bot(config)
    plugins = config["plugins"]
    for plug in plugins:
        plugName: str = plug.split('.')[1]
        cls: object = load_class(f"{plug}.{plugName}")
        bot.plugins["enabled"].append(cls(bot))

    bot.run()
if __name__ == '__main__':
    main()