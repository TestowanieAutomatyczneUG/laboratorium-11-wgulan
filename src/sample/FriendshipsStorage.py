from src.sample.Friendships import Friendships


class FriendshipsStorage:
    def __init__(self):
        self.database = Friendships()

    def make_friends(self, person1, person2):
        self.database.make_friends(person1, person2)

    def get_friends(self, person):
        return self.database.get_friends(person)

    def are_friends(self, person1, person2):
        return self.database.are_friends(person1, person2)
