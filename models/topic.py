class Topic:

    def __init__(self, name):
        self.name = name
        self.users = {}  # {"username" : User}

    def remove(self, user):
        if self.users[user.username] is None:
            raise Exception(f"UnsubscribeErr: {self.name} not subscribed by the {user.username}")
        self.users.pop(user.username)
        print(f'Successfully removed {user.username} from {self.name}')