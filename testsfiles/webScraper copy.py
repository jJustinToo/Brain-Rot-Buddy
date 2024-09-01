import requests
from bs4 import BeautifulSoup

# Step 1: Send a GET request to the GitHub profile page
url = "https://github.com/jjustintoo"
response = requests.get(url)

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Find the avatar image tag (GitHub profile avatar image)
avatar_tag = soup.find('img', {'class': 'avatar'})  # The avatar image is identified by the 'alt' attribute being 'Avatar'

# Step 4: Get the 'src' attribute from the image tag, which contains the avatar URL
if avatar_tag:
    avatar_url = avatar_tag['src']
    print("Avatar URL:", avatar_url)
else:
    print("Avatar not found.")