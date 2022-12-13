import sys


def redirect_output(filepath):
	def decorator(func):
		def wrapper(*args, **kwargs):
			sys.stdout = open(filepath, 'w')
			result = func(*args, **kwargs)
			sys.stdout.close()
			return result
		return wrapper
	return decorator


@redirect_output('./function_output.txt')
def calculate():
	for power in range(1, 5):
		for num in range(1, 20):
			print(num ** power, end=' ')
		print()

calculate()