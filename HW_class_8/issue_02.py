class Color:
	END = '\033[0'
	START = '\033[1;38;2'
	MOD = 'm'

	def __init__(self, red: int = 0, green: int = 0, blue: int = 0):
		if not (0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255):
			raise ValueError('Incorrect input')
		self.rgb = [red, green, blue]

	def __str__(self):
		return (
			f'{self.START};{self.rgb[0]};{self.rgb[1]};{self.rgb[2]}{self.MOD}'
			f'●'
			f'{self.END}{self.MOD}'
		)

	def __eq__(self, other):
		if type(other) != Color:
			return False
		return self.rgb == other.rgb


if __name__ == '__main__':
	green = Color(0, 255, 0)
	print(green)
	print(green == Color(255, 255, 0))
