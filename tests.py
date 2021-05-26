# tests.py
import tickets
import unittest
import pytest
import requests
from dotenv import load_dotenv
import os
import clui
import array_helper

class TestTickets(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def _pass_fixtures(self, capsys):
        self.capsys = capsys

    def test_exit():
        ''' Test that choice 3 prints correct message '''
        get_data(3, 0)
        captured = capsys.readouterr()
        assert captured.out == 'Thank you and have a nice day. Goodbye.\n'

    def test_page_response():
        test_url = "https://d3v-mackroetech.zendesk.com/api/v2/tickets/1"
        assert str(get_page(test_url2)) == "<Response [200]>"


if __name__ == '__main__':
    unittest.main()
