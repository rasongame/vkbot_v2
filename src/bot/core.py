class Bot:
    def __init__(self, config):
        import vk_api
        import logging
        logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')
        logging.getLogger("urllib3").setLevel(logging.DEBUG)
        self.group_id = config["group_id"]
        self.token = config["token"]
        self.vk_session = vk_api.VkApi(token=self.token)
        self.vk = self.vk_session.get_api()
        self.plugins: dict = {
            "enabled": [],
            "disabled": []
        }

    def run(self):
        from vk_api.bot_longpoll import VkBotLongPoll
        from .cmd_handler import eventHandler
        longpoll = VkBotLongPoll(self.vk_session, self.group_id)
        [eventHandler(self, event) for event in longpoll.listen()]