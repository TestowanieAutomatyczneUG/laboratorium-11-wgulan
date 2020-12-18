import unittest
from unittest.mock import MagicMock
from src.sample.FriendshipsStorage import FriendshipsStorage


class TestFriendshipsStorage(unittest.TestCase):

    def setUp(self):
        self.temp = FriendshipsStorage()

    def test_make_friends(self):
        self.temp.database = MagicMock()
        self.temp.make_friends("doe", "shmoe")
        self.temp.database.make_friends.assert_called_with("doe", "shmoe")

    def test_make_friends_not_a_string(self):
        self.temp.database.make_friends = MagicMock(side_effect=TypeError)
        with self.assertRaises(TypeError):
            self.temp.make_friends("doe", 123)
        self.temp.database.make_friends.assert_called_with("doe", 123)

    def test_get_friends(self):
        self.temp.database.get_friends = MagicMock(return_value=["shmoe", "xyz"])
        self.assertEqual(self.temp.get_friends("doe"), ["shmoe", "xyz"])
        self.temp.database.get_friends.assert_called_with("doe")

    def test_get_friends_not_a_string(self):
        self.temp.database.get_friends = MagicMock(side_effect=TypeError)
        with self.assertRaises(TypeError):
            self.temp.get_friends(["doe"])
        self.temp.database.get_friends.assert_called_with(["doe"])

    def test_get_friends_non_existing_person(self):
        self.temp.database.get_friends = MagicMock(side_effect=ValueError)
        with self.assertRaises(ValueError):
            self.temp.get_friends("doe")
        self.temp.database.get_friends.assert_called_with("doe")

    def test_are_friends_true(self):
        self.temp.database.are_friends = MagicMock(return_value=True)
        self.assertEqual(self.temp.are_friends("shmoe", "doe"), True)
        self.temp.database.are_friends.assert_called_with("shmoe", "doe")

    def test_are_friends_false(self):
        self.temp.database.are_friends = MagicMock(return_value=False)
        self.assertEqual(self.temp.are_friends("shmoe", "doe"), False)
        self.temp.database.are_friends.assert_called_with("shmoe", "doe")

    def test_are_friends_not_a_string(self):
        self.temp.database.are_friends = MagicMock(side_effect=TypeError('Person must be a string'))
        with self.assertRaisesRegex(TypeError, 'Person must be a string'):
            self.temp.are_friends([], {})
        self.temp.database.are_friends.assert_called_with([], {})

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()