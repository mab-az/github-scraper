import json
from bs4 import BeautifulSoup as bs
import os
import re


def books():
    """ Use the downloaded page to parse GitHub Organisation members logins """
    books = {}

    file_path = "books.html"

    pattern = r'"(.+?)"'
    pattern1 = r'>(.+?)<'
    

    with open(file_path, 'r') as f:
        for line in f.readlines():
            if "<h" in line:
                print(f"## {line}")
            if "href" in line:
                m = re.findall(pattern, line)
                # print(m)
                m2 = re.findall(pattern1, line)
                # print(m2)

                print(f"""- {m2}("{m[0]}")""")









if __name__ == "__main__":
   
    books()
