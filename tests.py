# tests.py
import tickets
import unittest
import pytest

def test_thing_1():
    ''' Doc string goes here '''
    a = 0 * 0
    assert a == 0

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
        test_url = "https://www.google.com/search?q=weather+results&oq=weather+results&aqs=chrome..69i57.4626j0j1&sourceid=chrome&ie=UTF-8"
        assert str(get_page(test_url2)) == "<Response [200]>"
