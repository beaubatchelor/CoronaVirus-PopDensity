from bs4 import BeautifulSoup
import requests
import pprint
pp = pprint.pprint


census_datasets = requests.get('https://api.census.gov/data.json').json()

title_list = []
pop_title_list = []
counter = 0
for dataset in census_datasets['dataset']:
    title = dataset['title']
    title_list.append(str(counter) + "|" + title)

    if 'population' in title.lower():
        pop_title_list.append(str(counter) + "|" + title)
    counter += 1
pp(pop_title_list)

pp(census_datasets['dataset'][398]['c_valuesLink'])

pop_json = requests.get('https://api.census.gov/data/2019/pep/population/values.json?STATE=CA').json()

print(pop_json.keys())

