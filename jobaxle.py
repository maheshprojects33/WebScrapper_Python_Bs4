from bs4 import BeautifulSoup as Bs
import requests

url = 'https://jobaxle.com/search'
result = requests.get(url)
doc = Bs(result.text, 'html.parser')

# print(doc.prettify())

for page in doc.find_all('div', class_='job_block'):
    # print(page)
    job_title = page.find('div', class_='job_block_ttl').a.text
    link = page.find('div', class_='job_block_ttl').a
    link_text = link['href']
    company = page.find('div', class_='job_block_company_name').span.text
    location = page.find('li', class_='job_area').text
    experience = page.find('h3', string='Education + Experience:')
    exp_value = [li.get_text(strip=True) for li in experience.find_next('ul').find_all('li')]

    print(f"Job Title= {job_title} \n"
          f"Company = {company} \n"
          f"Location = {location} \n"
          f"Link = {link_text} \n"
          f"Experience = {exp_value} \n")

# requirement = page.find('h3', string='Job Description: ')
# print(requirement)
# value = [li.get_text(strip=True) for li in requirement.find_next('ul').find_all('li')]
# print(value)