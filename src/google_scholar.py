import json
import requests
import os
from bs4 import BeautifulSoup as bs
import re


to_remove = ['<div class="gs_gray">', '<span class="gs_oph">', '</span></div>', '</div>', '\n']

def scholar_parser(file_path):

    with open(file_path, 'r', encoding='utf-8') as response:
        soup = bs(response, 'html.parser')
        
        papers = []

        # authors, title + link, publisher, date

        for soup_elem in soup.find_all(class_='gsc_a_t'):
            authors = ''
            title = ''
            paper_link = ''
            publisher = ''

            for link1 in soup_elem.find_all('a', {'class':"gsc_a_at"}):
                title = link1.string
                paper_link = link1.get('href')
            
            for link2 in soup_elem.find_all(class_="gs_gray"):
                link2 = str(link2)

                for remove_elem in to_remove:
                    if remove_elem in link2:
                        link2 = link2.replace(remove_elem, '')

                if 'Hajiramezanali' in link2:
                    authors = link2
                else:
                    publisher = link2
                    year_published = re.findall(r'20[0-9]{2}', str(publisher))
                    article_year = year_published[0] 

            papers.append({
                'authors': authors, 
                'title': title, 
                'paper_link': f"https://scholar.google.com{paper_link}", 
                'publisher': publisher,
                'year': article_year
                })

    sorted_papers = sorted(papers, key=lambda x: x['year'], reverse=True)

    with open('google_scholar_ehsan.json', 'w', encoding='utf-8') as f:
        json.dump(sorted_papers, f)
                

def format_json_scholar(path):
    # pattern - e.g. 2020, 2013 ... 
    # pattern = r'20[0-9][{2}'

    with open(path, 'r') as f:
        papers = json.load(f)

        for paper in papers:
            author = paper['authors']
            title = paper['title']
            paper_link = paper['paper_link']
            publisher = paper['publisher']
            year = paper['year']

            print(f" - **[{title}]({paper_link})**, {year}")


if __name__ == "__main__":
    # scholar_parser('scholar_html/scholar_ehsan.html')

    format_json_scholar('year_ordered_papers.json')