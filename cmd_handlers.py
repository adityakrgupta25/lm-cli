import manager


def addUser(params):
    if len(params) != 2:
        print("Insufficient args")
        return

    username = params[0]
    role = params[1]

    try:
        manager.add_user(username, role)
    except Exception as e:
        print(e)
        return

    print(f"Successfully created new {role}-user {username}")


def addTopic(params):
    if len(params) != 2:
        print("Insufficient args")
        return

    topic_name = params[0]
    username = params[1]
    try:
        manager.add_topic(username, topic_name)
    except Exception as e:
        print(e)
        return

    print(f"Successfully created new topic {topic_name}")


def subscribeTopic(params):
    if len(params) != 2:
        print("Insufficient args")
        return

    topic_name = params[0]
    username = params[1]
    try:
        manager.subscribe_topic(username, topic_name)
    except Exception as e:
        print(e)
        return
    print("Subscribed to topic!")


def publishMessage(params):
    if len(params) < 2:
        print("Insufficient args")
        return

    topic_name = params[0]
    msg = ' '.join(params[1:])

    try:
        manager.add_message(msg, topic_name)
    except Exception as e:
        print(e)
        return
    print("Published message!")


def processMessages(params):
    if len(params) != 0:
        print("unrecognized args")
        return
    manager.process_messages()


exec = {
    "addUser":         addUser,
    "addTopic":        addTopic,
    "subscribeTopic":  subscribeTopic,
    "publishMessage":  publishMessage,
    "processMessages": processMessages,
}
