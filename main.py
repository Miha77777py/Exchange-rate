import eel
from bs4 import BeautifulSoup as Bs
from lxml import etree
import requests

@eel.expose
def exchange_rate(currency, currency2, value):
	try:
		response = requests.get(f"https://minfin.com.ua/ua/currency/converter/?from={currency}&to={currency2}&val1={value}")
		html = etree.HTML(str(Bs(response.content, 'html.parser')))
		xpath_str = "/html/body/main/div/div/section/div/div/div/section[2]/div/table/tbody/tr[4]/td[3]/span/label/button"
		return html.xpath(xpath_str)[0].text
	except IndexError:
		return "Error"

if __name__ == "__main__":
	eel.init("web")
	eel.start("index.html", mod="chrome", port="3333", size=(500, 270))
