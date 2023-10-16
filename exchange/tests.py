
import json

def test():

	with open('rates.json') as f:
		data = json.load(f)

	for i in data['currency']:

		print(f"{i}")

if __name__ == "__main__":
	
	test()