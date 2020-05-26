from plugins.BasePlug import BasePlug


class CorePlug:
    def __init__(self, bot):
        self.bot = bot
        self.name = "Core Plug"
        self.commands: dict = {
            "инфо": self.info_cmd,
            "info": self.info_cmd,
        }

    def info_cmd(self, e):
        nl_symb = "\n"
        # msg = f"""
        # untitled bot :: V2
        #     Загруженные плагины: {nl_symb + ' '.join([str(pl.name) for pl in self.bot.plugins["enabled"]])}"""
        #
        msg = "ok"
        self.bot.vk.messages.send(peer_id=e.object.peer_id, random_id=0, message=msg)

    def test_cmd(self, e):
        # self.bot.vk_session.method("messages.send", {
        #     "peer_id" : e.object.peer_id,
        #     "message": "галочка тебе пизда"
        # })
        self.bot.vk.messages.send(peer_id=e.object.peer_id, random_id=0, message="arr")
