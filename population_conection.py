from bs4 import BeautifulSoup
import requests
import pprint
from config import census_key
pp = pprint.pprint

census_api = 'https://api.census.gov/data/'
year = '2019'
census_pop_suffix = '/pep/population?get='
variables = 'POP,DENSITY'
filters = '&for=county:*&in=state:06'
key = '&key=' + census_key
api_address = census_api + year + census_pop_suffix + variables + filters + key


pop_json = requests.get(api_address).json()

pp(pop_json[0:20])