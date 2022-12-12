class Pokemon:
	def __init__(self, name: str, poketype: str):
		self.name = name
		self.poketype = poketype

	def __repr__(self):
		return f'{self.name}/{self.poketype}'


bulbasaur = Pokemon(name='Bulbasaur', poketype='grass')
print(bulbasaur)
