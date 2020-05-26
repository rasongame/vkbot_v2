def eventHandler(self: object, event):
    import logging
    from vk_api.bot_longpoll import VkBotEventType
    if event.t == VkBotEventType.MESSAGE_NEW:
        try:
            resp = self.vk.users.get(user_ids=event.obj.from_id)[0]
            logging.info(f'{resp["first_name"]} {resp["last_name"]} in {event.obj.peer_id} sent {event.obj.text}')
            cmd = event.obj.text.split(maxsplit=1)[0]
            if cmd is not "":
                checkCmd(self, cmd, event)
        except:
            pass


def checkCmd(self, cmd, e):
    for plug in self.plugins["enabled"]:
        if cmd in plug.commands:
            plug.commands[cmd](e)
