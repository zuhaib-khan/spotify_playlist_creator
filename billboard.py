import requests
from bs4 import BeautifulSoup


date_selection = input("Enter the year whose playlist you want in YYYY-MM-DD format: ")

URL = f'https://www.billboard.com/charts/hot-100/{date_selection}/'

response = requests.get(URL)
website_data = response.text

soup = BeautifulSoup(website_data, 'html.parser')


song_titles = soup.find_all(name='li', class_ = 'o-chart-results-list__item')
for songs in song_titles:
    song = songs.find('h3')
    if song is not None:
        print(f"{song.getText().strip()}")
        
# for songs in song_titles:
#     print(songs.getText())

#Fetches the title of the web-Page
# a_tag = soup.find(name='a', class_ = 'c-logo')
# if a_tag is not None:
#     print(a_tag.get('title'))

# web_site_title = soup.find(name='div', class_ = 'lrv-u-flex')
# print(web_site_title.find('h2').getText())
# for songs in song_titles:
#     print(songs.getText())

