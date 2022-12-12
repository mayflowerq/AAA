class Color:
	def __init__(self, r: int, g: int, b: int) -> None:
		self.red_level = r
		self.green_level = g
		self.blue_level = b
		
	def print(self) -> None:
		END = '\033[0'
		START = '\033[1;38;2'
		MOD = 'm'
		print(f'{START};{self.red_level};{self.green_level};{self.blue_level}{MOD}●{END}{MOD}')


if __name__ == '__main__':
	color = Color(255, 0, 0)
	color.print()
	
