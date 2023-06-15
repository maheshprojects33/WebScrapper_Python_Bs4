from bs4 import BeautifulSoup as Bs
import requests

url = 'https://www.kumarijob.com/'
result = requests.get(url)
doc = Bs(result.text, 'html.parser')
# print(doc.prettify())

# for pages in doc.find_all('section', class_="position-relative"):
for pages in doc.find_all('div', class_="cardone__body"):
    # print(pages)
    try:
        job_title = pages.find('span', class_='title')
        company = pages.find('span', class_='meta').text
        link = job_title.a['href']
        print(f"Job Title: {job_title.text} \nCompany: {company} \nLink: {link} \n")

    except Exception as e:
        print("Data Not Available")



