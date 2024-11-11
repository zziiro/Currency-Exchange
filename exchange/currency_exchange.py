
import requests
import json


class Conversion:

	def __init__(self, res, data, amount_usd, convert_to):
		self = self
		self.res = res 
		self.data = data	
		self.amount_usd = amount_usd
		self.convert_to = convert_to
		self.rates = data["conversion_rates"] # get rates from json data

	def convert(self):
		# calc the conversion
		conversion = amount_usd * self.rates[convert_to]
		print(f"{conversion}")
		quit()


	def print_exchange_rate(self):
		# print all the currencies that USD can be converted to 
		# bring in json data and load it
		with open('rates.json') as f:
			data = json.load(f)

		# print each currency
		for i in data['currency']:
			print(f"{i}")


def prompt(data):
	check = True # checker
	while check:
		try:
			# get data from user 
			amount_usd = int(input("Current Amount in USD: \n"))
		except ValueError:
			print("[ERROR] Must be a number")
			prompt(data)


		convert_to = input("Convert to: [To see conversion rates enter: T]")
		if convert_to.upper() == "T":
			see_rates(res, data, amount_usd, convert_to)
			check = True
		elif convert_to in data["conversion_rates"]:
			con = Conversion(res, data, amount_usd, convert_to)
			print(con.convert())
		elif convert_to not in data["conversion_rates"]:
			print("[ERROR] Currency does not exist")
			check = False

def see_rates(res, data, amount_usd, convert_to):
	con = Conversion(res, data, amount_usd, convert_to)
	con.print_exchange_rate()



if __name__ == "__main__":
	# api url 
	url = ""

	# connect to api
	res = requests.get(url)
	# if api is unresponsive 
	if not res:
		print("[ERROR] No Response")

	# conversion obj
	data = res.json()

	prompt(data)

	

