import requests
from bs4 import BeautifulSoup

URL = 'https://www.billboard.com/charts/hot-100/2013-08-10/'

response = requests.get(URL)
website_data = response.text

soup = BeautifulSoup(website_data, 'htmlparser')

date_selection = input("Enter the year whose playlist you want in YYYY-MM-DD format.")

