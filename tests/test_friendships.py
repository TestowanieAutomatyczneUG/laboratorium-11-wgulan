import unittest
from src.sample.Friendships import Friendships


class TestFriendships(unittest.TestCase):

    def setUp(self):
        self.temp = Friendships()
        self.temp.friendships = {
            "nowak": ["kowalski", "wiśniewski"],
            "wiśniewski": ["nowak"],
            "kowalski": ["nowak"],
            "lewandowski": []
        }

    def test_add_friend_of_new_person(self):
        self.temp.add_friend("doe", "shmoe")
        self.assertEqual(self.temp.friendships["doe"], ["shmoe"])

    def test_add_friend_of_existing_person(self):
        self.temp.add_friend("kowalski", "shmoe")
        self.assertEqual(self.temp.friendships["kowalski"], ["nowak", "shmoe"])

    def test_make_friends(self):
        self.temp.make_friends("doe", "shmoe")
        self.assertEqual(self.temp.friendships, {
            "nowak": ["kowalski", "wiśniewski"],
            "wiśniewski": ["nowak"],
            "kowalski": ["nowak"],
            "lewandowski": [],
            "doe": ["shmoe"],
            "shmoe": ["doe"]
        })

    def test_make_friends_not_a_string(self):
        with self.assertRaisesRegex(TypeError, 'Person must be a string'):
            self.temp.make_friends("doe", 123)

    def test_make_friends_already_friends(self):
        with self.assertRaisesRegex(ValueError, 'Given persons are already friends'):
            self.temp.make_friends("kowalski", "nowak")

    def test_get_friends(self):
        self.assertEqual(self.temp.get_friends("kowalski"), ["nowak"])

    def test_get_friends_not_a_string(self):
        with self.assertRaisesRegex(TypeError, 'Person must be a string'):
            self.temp.get_friends(12)

    def test_get_friends_non_existing_person(self):
        with self.assertRaisesRegex(ValueError, "No such person"):
            self.temp.get_friends("doe")

    def test_are_friends_true(self):
        self.assertEqual(self.temp.are_friends("kowalski", "nowak"), True)

    def test_are_friends_false(self):
        self.assertEqual(self.temp.are_friends("kowalski", "wiśniewski"), False)

    def test_are_friends_not_a_string(self):
        with self.assertRaisesRegex(TypeError, 'Person must be a string'):
            self.temp.are_friends([], {})

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()