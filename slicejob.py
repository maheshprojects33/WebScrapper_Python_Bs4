from bs4 import BeautifulSoup
import requests

url = 'https://www.slicejob.com/jobs/search/?job_category=information-technology-it-jobs&job_tittle=&submit=Search&page=1'
result = requests.get(url)
doc = BeautifulSoup(result.text, 'html.parser')

pagination = doc.find('ul', class_='pagination').text
pages = int(pagination[12:15])

for page in range(1, pages + 1):
    url = f'https://www.slicejob.com/jobs/search/?job_category=information-technology-it-jobs&job_tittle=&submit' \
          f'=Search&page={page}'
    result = requests.get(url)
    doc = BeautifulSoup(result.text, 'html.parser')

    print(url)
    for post in doc.find_all('div', id='item_list'):
        job_title = post.find("li", class_='job_tittle').text
        address = post.find('li', class_='job_company').text
        experience = post.find('li', class_='job_experience').text
        link = post.find('li', class_='job_tittle').a['href']

        print(f"Job Title = {job_title} \nAddress = {address} \nExperience = {experience} \nLink = {link} \n")

