import keyword


class InitialAdvert:
	def __init__(self, mapping):
		old_dict = dict()
		counter = 0
		for i in mapping:
			if type(mapping[i]) == dict:
				old_dict[i] = Advert(mapping[i])
			else:
				old_dict[i] = mapping[i]
		new_dict = dict()
		for i in old_dict:
			if i == 'price':
				counter += 1
				if old_dict['price'] < 0:
					old_dict['price'] = 'ValueError: must be >= 0'
		if counter == 0:
			new_dict['price'] = 0
		for i in old_dict:
			if keyword.iskeyword(i):
				new_dict[i + '_'] = old_dict[i]
			else:
				new_dict[i] = old_dict[i]
		self.__dict__ = new_dict

	def __str__(self):
		object_list = []
		for i in self.__dict__.values():
			i = str(i)
			object_list.append(i)
		return f"{' | '.join(object_list)} ₽"


class ColorizeMixin:
	def __str__(self):
		text: str = super().__str__()
		repr_color_code_new = f'[{repr_color_code}m'
		return f"\033{repr_color_code_new} {text}\n"


class Advert(ColorizeMixin, InitialAdvert):
	global repr_color_code
	repr_color_code = '32'


iphone_ad = Advert({'title': 'iPhone X', 'price': 100})
print(iphone_ad)
