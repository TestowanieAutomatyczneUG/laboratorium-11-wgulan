from src.sample.Checker import Checker
from unittest.mock import *
from unittest import TestCase, main


class TestChecker(TestCase):

    def setUp(self):
        self.test_checker = Checker()

    def test_checker_play_file_after_17(self):
        wav_file = 'file.wav'
        # prepare mock
        self.test_checker.env.getTime = MagicMock(return_value=20)

        self.test_checker.reminder(wav_file)
        # testing
        self.assertEqual(self.test_checker.env.played, True)

    def test_checker_do_not_play_file_before_17(self):
        wav_file = 'file.wav'
        # prepare mock
        self.test_checker.env.getTime = MagicMock(return_value=16)

        self.test_checker.reminder(wav_file)
        # testing
        self.assertEqual(self.test_checker.env.played, False)

    def tearDown(self):
        self.test_checker = None


if __name__ == '__main__':
    main()
