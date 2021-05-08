import enum


class Roles(enum.Enum):
    admin = 0
    user = 1

    v = {admin: "ADMIN", user: "USER"}

    @staticmethod
    def verbose(role):
        return Roles.v[role]


class User:

    def __init__(self, username, role):
        self.username = username
        self.role = role
        self.topics = {}

    def subscribe(self, topic):
        self.topics[topic.name] = topic
        topic.users[self.username] = self
        print(f'Successfully subscribed {self.username} to {topic.name}')

    def unsubscribe(self, topic):
        if self.topics[topic.name] is None:
            raise Exception(f"UnsubscribeErr: {self.username} not subscribed to the topic {topic.name}")

        self.topics.pop(topic.name)
        topic.remove(self)
        print(f'Successfully unsubscribed {self.username} from {topic.name}')
