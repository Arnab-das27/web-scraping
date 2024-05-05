import os
import requests
from bs4 import BeautifulSoup

url = 'https://riptutorial.com/ebook/scrapy'

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Create folder for downloads
os.makedirs('downloaded_pdfs', exist_ok=True) 

pdf_links = [a['href'] for a in soup.find_all('a') if '.pdf' in a['href']]

# Download and save PDFs
for link in pdf_links:
  pdf_url = requests.compat.urljoin(url, link)
  filename = link.split('/')[-1] 
  pdf_response = requests.get(pdf_url)

  with open(f'downloaded_pdfs/{filename}', 'wb') as f:
    f.write(pdf_response.content)