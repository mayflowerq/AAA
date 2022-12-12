from morse import MORSE_TO_LETTER
import pytest


def decode(morse_message: str) -> str:
    """
    Декодирует строку из азбуки Морзе в английский
    """
    decoded_letters = [
        MORSE_TO_LETTER[letter] for letter in morse_message.split()
    ]

    return ''.join(decoded_letters)


@pytest.mark.parametrize('source_string, result',
                         [
                             ('.-..', 'L'),
                             ('..', 'I'),
                             ('--...', '7'),
                         ]
                         )
def test_decode(source_string, result):
    assert decode(source_string) == result
