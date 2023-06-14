from bs4 import BeautifulSoup as Bs
import requests

url = f"https://www.jobsnepal.com/jobs?page=1"

result = requests.get(url)
doc = Bs(result.text, "html.parser")

page_num = []
for tag in doc.find_all(class_='page-link'):
    page_num.append(tag.string)
last_page = int(page_num[-2])

for page in range(1, last_page + 1):
    url = f"https://www.jobsnepal.com/jobs?page={page}"
    result = requests.get(url)
    doc = Bs(result.text, "html.parser")

    print(url)
    for article in doc.find_all('div', class_='card-inner'):
        # print(article)
        job_title = article.h2.a.text.strip()
        company = article.p.text
        link = article.h2.a['href']
        location = article.find_all_next('li')[1].div.text.strip()
        detail = article.find_all_next('div', class_="d-flex align-items-center pl-1 pr-1 py-1")[1].text.strip()

        print(f"Title= {job_title} \nCompany= {company} \nLocation= {location} \nTags= {detail} \nLink= {link} \n")





