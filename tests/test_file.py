import unittest
from unittest.mock import mock_open, patch
from src.sample.File import File


class TestFile(unittest.TestCase):
    def setUp(self):
        self.temp = File()

    def test_read_file(self):
        with patch("builtins.open", mock_open(read_data="test_data")) as mock_file:
            self.assertEqual(self.temp.read_file('/fake/file/path.txt'), "test_data")
            mock_file.assert_called_with('/fake/file/path.txt', 'r')

    def test_write_file(self):
        with patch("builtins.open", mock_open(read_data="test_data")) as mock_file:
            self.temp.write_file('/fake/file/path.txt', 'new_data')
            mock_file.assert_called_with('/fake/file/path.txt', 'w')

    @patch('os.path.isfile')
    @patch('os.remove')
    def test_delete_existing_file(self, mock_isfile, mock_remove):
        mock_isfile.return_value = True
        self.temp.delete_file('/fake/file/path.txt')
        mock_remove.assert_called_with('/fake/file/path.txt')

    @patch('os.path.isfile')
    def test_delete_non_existing_file(self, mock_isfile):
        mock_isfile.return_value = False
        with self.assertRaises(Exception):
            self.temp.delete_file('/fake/file/path.txt')