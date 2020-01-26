import csv
import re

import requests
from bs4 import BeautifulSoup


def fix_title(title):
    title = remove_punct(title)
    title = remove_multiple_spaces(title)
    return title


def remove_punct(string):
    string = re.sub(r"[']+", '', string)
    return re.sub(r"[-:_!,/\[\].()#?;&\n]+", ' ', string).strip()


def remove_multiple_spaces(string):
    return re.sub(r'\s+', ' ', string).strip()


def search_youtube(query):
    print(f"querying youtube for '{query}'")
    base_url = "https://www.youtube.com"
    url = base_url + "//results?sp=egiqavau&q=" + query

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        title_list = []
        for tile in soup.find_all(attrs={"class": "yt-lockup-tile"}):
            yt_uix_tile = tile.find(attrs={"class": "yt-uix-tile-link"})
            title = yt_uix_tile["title"]
            title = fix_title(title)
            title_list.append(title)
        return title_list

    except Exception as e:
        print(f"error: {e}")
        exit()


with open("data.csv", "w", encoding="UTF-8") as file:
    csv_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    dictionary = open("words.txt")
    for word in dictionary:
        word = word.strip()
        titles = search_youtube(word)
        for title in titles:
            csv_writer.writerow([word, title])
