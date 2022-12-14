import requests
from bs4 import BeautifulSoup

# Start with a URL.
res = requests.get('https://cs.byu.edu/department/directory/faculty-directory/sean-warnick/', verify=False)
print("The status code is ", res.status_code)
print("\n")
soup_data = BeautifulSoup(res.text, 'html.parser')
print(soup_data.title)
print("\n")
print(soup_data.contents)

tags = soup_data.find_all()
for tag in tags:
    if 'id' in tag.attrs:
        print(tag.name,tag['id'],sep='->')
        
div_bs4 = soup_data.find_all('section', id = "students")
print(div_bs4)
person = {}

for div in soup_data.findAll('div', {'class': 'card-title'}):
    print(div)
    #person[div.find('class').attrs['card-title'][0]] = div.text.strip()

print(person)

print(soup_data.find_all("div", {'class':'card-title'}))