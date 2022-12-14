from what_is_year_now import what_is_year_now
import unittest
from unittest.mock import MagicMock, patch


class TestWhatIsYearNow(unittest.TestCase):
	@patch('urllib.request.urlopen')
	def test_format_ymd(self, urlopen):
		mock = MagicMock()
		mock.read.return_value = '{"$id":"1",' \
									 '"currentDateTime":"2022-10-10T23:32Z",' \
									 '"utcOffset":"00:00:00",' \
									 '"isDayLightSavingsTime":false,' \
									 '"dayOfTheWeek":"Monday",' \
									 '"timeZoneName":"UTC",' \
									 '"currentFileTime":133099183602978015,' \
									 '"ordinalDate":"2022-283",' \
									 '"serviceResponse":null}'
		mock.__enter__.return_value = mock
		urlopen.return_value = mock

		year = what_is_year_now()
		assert year == 2022

	@patch('urllib.request.urlopen')
	def test_format_dmy(self, urlopen):
		mock = MagicMock()
		mock.read.return_value = '{"$id":"1",' \
								 '"currentDateTime":"10.10.20220T23:32Z",' \
								 '"utcOffset":"00:00:00",' \
								 '"isDayLightSavingsTime":false,' \
								 '"dayOfTheWeek":"Monday",' \
								 '"timeZoneName":"UTC",' \
								 '"currentFileTime":133099183602978015,' \
								 '"ordinalDate":"2022-283",' \
								 '"serviceResponse":null}'
		mock.__enter__.return_value = mock
		urlopen.return_value = mock

		year = what_is_year_now()
		assert year == 2022

	@patch('urllib.request.urlopen')
	def test_invalid_format(self, urlopen):
		mock = MagicMock()
		mock.read.return_value = '{"$id":"1",' \
								 '"currentDateTime":"Christmas_2022",' \
								 '"utcOffset":"00:00:00",' \
								 '"isDayLightSavingsTime":false,' \
								 '"dayOfTheWeek":"Monday",' \
								 '"timeZoneName":"UTC",' \
								 '"currentFileTime":133099183602978015,' \
								 '"ordinalDate":"2022-283",' \
								 '"serviceResponse":null}'
		mock.__enter__.return_value = mock
		urlopen.return_value = mock
		with self.assertRaises(ValueError):
			what_is_year_now()

