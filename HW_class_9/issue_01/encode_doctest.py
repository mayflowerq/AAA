from morse import LETTER_TO_MORSE


def encode(message: str) -> str:
	"""
	Кодирует строку в соответсвии с таблицей азбуки Морзe

	>>> encode('SOS') # doctest: +ELLIPSIS
	'... --- ...'

	>>> encode(123)
	Traceback (most recent call last):
	TypeError: 'int' object is not iterable

	>>> encode(['123321'])
	Traceback (most recent call last):
	KeyError: '123321'

	>>> encode('some_statement') # doctest: +SKIP

	"""
	encoded_signs = [
		LETTER_TO_MORSE[letter] for letter in message
	]
	return ' '.join(encoded_signs)
