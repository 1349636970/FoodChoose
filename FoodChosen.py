import random

import urllib3
import certifi
from bs4 import BeautifulSoup

http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
html_code = http.request('GET', 'https://www.allrecipes.com/recipes/')
soup = BeautifulSoup(html_code.data, 'html.parser')
categories = soup.find_all('div', {"class": "all-categories-col"})
category_titles = []
category_links = []
for category in categories:
    anchors = category.find_all('a')
    for anchor in anchors:
        category_titles.append(anchor.string)
        category_links.append(anchor)
for category_title in category_titles:
    print(category_title)

category_choose=""
while category_choose!='exit':
    category_choose = input("Plz enter one of categories from the list: ")
    if category_choose == "exit":
        break
    elif category_choose == "":
        category_choose = str(category_titles[random.randint(0,len(category_titles)-1)])
    recipes_name_list = []
    recipe_name_links = []
    recipe_name_links_title = []
    recipe_name_spcific = []
    recipe_hypertext_link = []
    for category_link in category_links:
        if category_choose == category_link.string:
            html_code_recipes = http.request('GET', category_link.attrs['href'])
            soup = BeautifulSoup(html_code_recipes.data, 'html.parser')
            recipe_names = soup.find_all('span', {"class": "fixed-recipe-card__title-link"})
            for recipe_name in recipe_names:
                recipe_name_links.append(recipe_name.parent)
                recipes_name_list.append(recipe_name.string)
    for recipe_name_link in recipe_name_links:
        recipe_name_links_title.append(str(recipe_name_link).split("\n"))
    random_number = random.randint(0,len(recipe_name_links_title)-1)
    for recipe_name_link_title in recipe_name_links_title[random_number]:
        soup = BeautifulSoup(recipe_name_link_title,'html.parser')
        recipe_name_spcific.append(soup.span)
        recipe_hypertext_link.append(soup.a)

    print('Your food: {}'.format(recipe_name_spcific[1].string))
    print('Go here to learn how to cook: {}'.format(recipe_hypertext_link[0].attrs['href']))
