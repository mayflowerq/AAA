from morse import LETTER_TO_MORSE


def encode(message: str) -> str:
	"""
	Кодирует строку в соответсвии с таблицей азбуки Морзe

	"""
	encoded_signs = [
		LETTER_TO_MORSE[letter] for letter in message
	]
	return ' '.join(encoded_signs)


def test_encode():
	test_exception = 'SOS'
	res = encode(test_exception)
	try:
		assert res == '... --- ...', f'input: {test_exception}, expected: ... --- ..., got: {res}'
	except AssertionError:
		pass
	return


if __name__ == '__main__':
	test_encode()
