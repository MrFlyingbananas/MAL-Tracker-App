import constraints;
import requests as req

from bs4 import BeautifulSoup
response = req.get(constraints.ANIMELIST_GET_LINK.format("mrflyingbananas"))

print(response.status_code)
list_soup = BeautifulSoup(response.text, 'lxml')
