import requests
import json
from bs4 import BeautifulSoup


def collect_data(numbers, subjects, summaries):
    data = {}
    data['subjects'] = []

    for idx in range(len(numbers)):
        if idx > 0:
            number = int(numbers[idx].getText())
            subject = subjects[idx].getText()
            summary = summaries[idx].getText()
            data['subjects'].append(
                {'number': number, 'subject': subject, 'summary': summary})
    print('Done crawl')

    try:
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2) #convert obj to JSON string and write to file
    except IOError as err:
        print(err)


def crawl_data():
    res = requests.get('https://daa.uit.edu.vn/content/bang-tom-tat-mon-hoc')
    soup = BeautifulSoup(res.text, 'html.parser')

    numbers = soup.select("td[width='43'] > p")
    subjects = soup.select("td[width='157'] > p")
    summaries = soup.select("td[width='643'] > p")

    collect_data(numbers, subjects, summaries)

crawl_data()
