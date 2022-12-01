import json
import keyword


class Advert:
	def __init__(self, mapping):
		old_dict = dict()
		price_counter = 0
		title_counter = 0
		for i in mapping:
			if i == 'title' or 'address':
				title_counter += 1
			if type(mapping[i]) == dict:
				old_dict[i] = Advert(mapping[i])
			else:
				old_dict[i] = mapping[i]
		if title_counter == 0:
			raise ValueError
		new_dict = dict()
		for i in old_dict:
			if i == 'price':
				price_counter += 1
				if old_dict['price'] < 0:
					old_dict['price'] = 'ValueError: must be >= 0'
		if price_counter == 0:
			new_dict['price'] = 0
		for i in old_dict:
			if keyword.iskeyword(i):
				new_dict[i + '_'] = old_dict[i]
			else:
				new_dict[i] = old_dict[i]
		self.__dict__ = new_dict


lesson_str = """{
"title": "python",
"price": 0,
"location": {
"address": "город Москва, Лесная, 7",
"metro_stations": ["Белорусская"]
}
}"""
lesson = json.loads(lesson_str)
lesson_ad = Advert(lesson)
print(lesson_ad.location.address)

dog_str = """{
"title": "Вельш-корги",
"price": 1000,
"class": "dogs"
}"""
dog = json.loads(dog_str)
dog_ad = Advert(dog)
print(dog_ad.class_)

lesson_price_check_str = '{"title": "python", "price": -1}'
lesson_price_check = json.loads(lesson_price_check_str)
lesson_price_check_ad = Advert(lesson_price_check)
print(lesson_price_check_ad.price)

lesson_price_change_str = '{"title": "python", "price": 1}'
lesson_price_change = json.loads(lesson_price_change_str)
lesson_price_change_ad = Advert(lesson_price_change)
lesson_price_change_str = '{"title": "python", "price": -3}'
lesson_price_change = json.loads(lesson_price_change_str)
lesson_price_change_ad = Advert(lesson_price_change)
print(lesson_price_change_ad.price)

lesson_no_price_str = '{"title": "python"}'
lesson_no_price = json.loads(lesson_no_price_str)
lesson_no_price_ad = Advert(lesson_no_price)
print(lesson_no_price_ad.price)
