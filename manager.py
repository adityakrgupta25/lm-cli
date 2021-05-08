import models
from models.user import Roles
from models.topic import Topic
from models.message import Message

Users = {}      # username : user
Topics = {}     # topic_name : topic
Messages = []   # list of messages to be consumed

roles = {
    "user": Roles.user,
    "admin": Roles.admin
}


# Add new instances
def add_user(username, role):
    user = Users.get(username, None)

    if user is not None:
        raise Exception("User already exists")

    role = roles.get(role, None)
    if role is None:
        raise Exception(f"Invalid role")
    user = models.user.User(username, role)
    Users[user.username] = user


def add_topic(username, topic_name):
    user = Users.get(username, None)
    if user is None:
         raise Exception("NotFoundErr: User does not exist")

    if user.role != Roles.admin:
        raise Exception("Forbidden to create a new topic")

    topic = Topics.Get(topic_name, None)
    if topic is not None:
        raise Exception("Topic already exists")

    topic = Topic(topic_name)
    Topics[topic_name] = topic


def add_message(text, topic_name):
    topic = Topics.get(topic_name, None)
    if topic is None:
        raise Exception(f'NotFoundErr: Topic {topic_name} does not exist')
    # calculate id
    id = 0
    if len(Messages) != 0:
        id = Messages[-1].id + 1

    message = Message(id, text, topic)
    Messages.append(message)


# Operations
def subscribe_topic(username, topic_name):
    user = Users.get(username, None)
    topic = Topics.get(topic_name, None)

    if topic is None or user is None:
        raise Exception("User or template does not exists")
    user.subscribe(topic)


def process_messages():
    print("**Consuming messages**")
    final_response = []
    for message in Messages:
        resp = message.consume()
        final_response.extend(resp)
    print(final_response)
