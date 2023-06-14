from bs4 import BeautifulSoup as Bs
import requests

url = f"https://merojob.com/category/it-telecommunication/?page=1"

result = requests.get(url)
doc = Bs(result.text, "html.parser")
# print(doc.prettify())
page_num = []
for pagination in doc.find_all('li', class_='page-item'):
    page_num.append(pagination.a.text)
last_page = int(page_num[-2])

for page in range(1, last_page + 1):
    url = f"https://merojob.com/category/it-telecommunication/?page={page}"
    result = requests.get(url)
    doc = Bs(result.text, "html.parser")

    print(url)
    for articles in doc.find_all('div', class_='job-card'):
        try:
            job_title = articles.a.text
            company_name = articles.h3.a.text
            link = articles.h1.a['href']
            location = articles.find(itemprop='addressLocality').text
        except Exception as e:
            print("None")

        print(f"Job Title = {job_title.lstrip()}Company Name = {company_name.lstrip()}Link = https://merojob.com{link}\n "
              f"Location = {location.lstrip()} \n")


