from what_is_year_now import what_is_year_now
import unittest
from unittest.mock import patch


class TestWhatIsYearNow(unittest.TestCase):
	def test_what_is_year_now(self):
		with patch('what_is_year_now.urllib.request') as requests_mock:
			requests_mock.urlopen.return_value = lambda: (2022)

