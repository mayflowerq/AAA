import click
from random import randint


class Based:
	recipes = []
	names = []

	def __init__(self, size: str):
		if size == 'L' or size == 'XL':
			self.size = {'size': size}
		else:
			print('Choose another size')
			raise ValueError

	def dict(self):

		"""Выводит рецепт в виде словаря и размер пиццы"""

		print(self.recipe)
		print(self.size)

	def __eq__(self, other):
		return self.size == other.size


class Margherita(Based):
	recipe = {'ingredients': f'tomato_sauce, mozzarella, tomatoes, dough'}
	recipe_ingredients = recipe['ingredients']
	Based.recipes.append(recipe_ingredients)
	name = 'Margherita🧀'
	Based.names.append(name)


class Pepperoni(Based):
	recipe = {'ingredients': f'tomato_sauce, mozzarella, pepperoni, dough'}
	recipe_ingredients = recipe['ingredients']
	Based.recipes.append(recipe_ingredients)
	name = 'Pepperoni🍕'
	Based.names.append(name)


class Hawaiian(Based):
	recipe = {'ingredients': f'tomato_sauce, mozzarella, chicken, pineapples, dough'}
	recipe_ingredients = recipe['ingredients']
	Based.recipes.append(recipe_ingredients)
	name = 'Hawaiian🍍'
	Based.names.append(name)


def log(func):

	"""Декоратор, считающий время выполнения функции"""

	def wrapper(*args, **kwargs):
		result = func(*args, **kwargs)
		random_proceeding_time = randint(1, 5)
		print(f'Время выполнения функции {func.__name__} - {random_proceeding_time}с\n')
		return result
	return wrapper


@log
def bake(pizza: str):

	"""Готовит пиццу"""

	random_time_cooking = randint(1, 5)
	print(f'Приготовили вашу {pizza} за {random_time_cooking}с!')


@click.group()
def cli():
	pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza, delivery):

	"""Готовит и доставляет пиццу"""

	random_time_cooking = randint(1, 5)
	random_time_delivery = randint(1, 5)
	print(f'Приготовили вашу {pizza} за {random_time_cooking}с!')
	if delivery:
		print(f'Доставили вашу {pizza} за {random_time_delivery}с!')


@cli.command()
def menu():

	"""Выводит меню"""

	print('Our menu:')
	for i in range(len(Based.recipes)):
		print(f'{Based.names[i]}: \n'
			  f'	Ingredients: {Based.recipes[i]}\n'
			  f'	Avaliable sizes: L, XL')


if __name__ == '__main__':
	pizza1 = Margherita('XL')
	pizza2 = Margherita('XL')
	pizza1.dict()
	print(pizza1 == pizza2)
	bake('Pepperoni')
	cli()
