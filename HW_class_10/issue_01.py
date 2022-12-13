import sys
from datetime import datetime


original_write = sys.stdout.write


def my_write(string_text):
	current_datetime = datetime.now()
	time_format = "%Y-%m-%d %H:%M:%S"
	if string_text != '\n':
		string_text = f'[{current_datetime:{time_format}}]: {string_text}'
	original_write(string_text)


sys.stdout.write = my_write
print('1, 2, 3')
sys.stdout.write = original_write
