import requests
from bs4 import BeautifulSoup as bs
import csv
import os

def main():
    username = input('Username: ')
    # username = 'toh14699'
    # password = 'Lunch123'
    password = input('Password: ')
    url = 'https://thehub.standrews.vic.edu.au'

    # Session 
    s = requests.Session()
    
    # Logs in to user
    login = {"username": username, "password": password}
    r = s.post(f'{url}', data = login)
    soup = bs(r.text, 'html.parser')

    if soup.find('input', {'type' : "submit"}, {'name' :"Submit"}) is None:
        print('Successfully logged in!')
    else:
        print('Authentication Error')
        return
    
    # Gets PFP and saves it.
    pfp = soup.find('img', {'title' : 'View Profile'})['src']
    user_code = pfp.removeprefix("/portrait.php?id=").removesuffix('&size=square72')
    image_url = url + "/portrait.php?id=" + user_code
    print(image_url)
    
    # Saves image to USER_CODE.jpg
    img_data = s.get(image_url).content
    with open(f'./webScraper/{user_code}.jpg' , 'wb') as handler:
        handler.write(img_data)
    
    # Goes to user page. 
    url = 'https://thehub.standrews.vic.edu.au/search/user/' + user_code
    r = s.get(url)
    soup = bs(r.content, 'html.parser')
    
    # Writes USER_DATA to csv
    user_data = [soup.find_all('dt', {'class' : 'small-4 medium-3 columns'}), soup.find_all('dd', {'class' : 'small-8 medium-9 columns'})]
    if os.path.isfile(f'./webScraper/{user_code}.csv'):
        os.remove(f'./webScraper/{user_code}.csv')
    with open(f'./webScraper/{user_code}.csv','a', newline='') as file:
        key, value = 'Name', soup.find('div', {'class': 'small-12 column'}).get_text().strip()
        csv.writer(file).writerow([key, value])
        print(key + ': ' + value)
        for i in range(1, len(user_data[0]) - 1):
            key, value = user_data[0][i].get_text().strip(':'), user_data[1][i].get_text()
            print(key + ': ' + value)
            csv.writer(file).writerow([key, value])
    
    # Goes to Grades page.
    url = 'https://thehub.standrews.vic.edu.au/learning/grades/' + user_code
    r = s.get(url)
    soup = bs(r.content, 'html.parser')
    
    # Writes GRADES_DATA into csv
    grades = soup.find_all("a", {"class": "flex-grade link-row"}, {'title': 'View Grades'})
    for grade in grades:
        grades_data = grade.find_all("span")
        print(grades_data[0].get_text().strip().strip('( )') + ': ' + grades_data[1].get_text())
        with open(f'./webScraper/{user_code}.csv','a', newline='') as file:
            csv.writer(file).writerow([grades_data[0].get_text().strip().strip('( )'), grades_data[1].get_text()])
    
    
main()