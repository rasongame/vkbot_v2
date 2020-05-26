
class BasePlug():
    def __init__(self, bot):
        self.bot = bot
        self.name = "BasePlug"
        self.commands: dict = {"test": self.test_cmd}
    def test_cmd(self, e):
        # self.bot.vk_session.method("messages.send", {
        #     "peer_id" : e.object.peer_id,
        #     "message": "галочка тебе пизда"
        # })
        self.bot.vk.messages.send(peer_id=e.object.peer_id, random_id=0, message="?")
    def work(self, **kwargs):
        return
