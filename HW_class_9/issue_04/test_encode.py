from one_hot_encoder import fit_transform
import pytest


def test_seqw():
	assert fit_transform(['Seqw', 'Terwfre', 'Dolce', 'pops']) == [('Seqw', [0, 0, 0, 1]),
																('Terwfre', [0, 0, 1, 0]),
																('Dolce', [0, 1, 0, 0]),
																('pops', [1, 0, 0, 0])]


def test_two():
	assert fit_transform(['2']) == [('2', [1])]


def test_one_two_three():
	assert fit_transform(['1', '2', '3']) == [('1', [0, 0, 1]), ('2', [0, 1, 0]), ('3', [1, 0, 0])]


def test_qwerty():
	assert fit_transform(['Q', 'W', 'E', 'R', 'T', 'Y']) == [('Q', [0, 0, 0, 0, 0, 1]),
															('W', [0, 0, 0, 0, 1, 0]),
															('E', [0, 0, 0, 1, 0, 0]),
															('R', [0, 0, 1, 0, 0, 0]),
															('T', [0, 1, 0, 0, 0, 0]),
															('Y', [1, 0, 0, 0, 0, 0])]


def test_exception():
	with pytest.raises(TypeError):
		fit_transform(7)
