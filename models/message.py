
class Message:

    def __init__(self, id, text, topic):
        self.id = id
        self.text = text
        self.topic = topic

    def consume(self):
        l = []
        for user in self.topic.users:
            resp = {
                "topic": self.topic.name,
                "message": self.text,
                "sentTo": user
            }
            l.append(resp)
        return l

