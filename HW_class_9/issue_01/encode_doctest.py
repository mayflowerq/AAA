from morse import LETTER_TO_MORSE


def encode(message: str) -> str:
	"""
	Кодирует строку в соответсвии с таблицей азбуки Морзe

	>>> encode('SOS') # doctest: +ELLIPSIS
	'... --- ...'
	"""
	encoded_signs = [
		LETTER_TO_MORSE[letter] for letter in message
	]
	return ' '.join(encoded_signs)
