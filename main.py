import requests
from bs4 import BeautifulSoup

class pcSpyder:
	def __init__(self):
		pass
		
	def get_products(self, keyword):
		url = "https://www.pcstore.com.tw/adm/psearch.htm"
		params = {"store_k_word": keyword.encode("big5"), "slt_k_option": 1}

		res = requests.get(url, params=params)
		soup = BeautifulSoup(res.content, "lxml")
		products = soup.find_all("div", class_="pic2t")

		title_list = []
		for i in range(len(products)):
			title_list.append(products[i].text)
			print(products[i].text)
			
		return title_list

if __name__ == "__main__":
	keyword = input("Please enter keyword:")
	pc = pcSpyder()
	result = pc.get_products(keyword)
