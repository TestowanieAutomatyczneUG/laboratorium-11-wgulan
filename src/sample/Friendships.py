class Friendships:
    def __init__(self):
        self.friendships = {}

    def add_friend(self, person, friend):
        if person not in self.friendships.keys():
            self.friendships[person] = [friend]
        else:
            self.friendships[person].append(friend)

    def make_friends(self, person1, person2):
        if type(person1) != str or type(person2) != str:
            raise TypeError('Person must be a string')
        if person1 in self.friendships.keys() and person2 in self.friendships[person1]:
            raise ValueError('Given persons are already friends')
        self.add_friend(person1, person2)
        self.add_friend(person2, person1)

    def get_friends(self, person):
        if type(person) != str:
            raise TypeError('Person must be a string')
        if person not in self.friendships.keys():
            raise ValueError("No such person")
        return self.friendships[person]

    def are_friends(self, person1, person2):
        if type(person1) != str or type(person2) != str:
            raise TypeError('Person must be a string')
        if person1 in self.friendships[person2] and person2 in self.friendships[person1]:
            return True
        else:
            return False
