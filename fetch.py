import requests
from bs4 import BeautifulSoup
import json

def fetch_google_scholar_publications(profile_url):
    
    headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
        }
    response = requests.get(profile_url, headers=headers)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve profile: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    publications = []

    # Find the publication entries
    for item in soup.find_all('tr', class_='gsc_a_tr'):
        title_element = item.find('a', class_='gsc_a_at')
        authors_element = item.find('div', class_='gs_gray')
        year_element = item.find('span', class_='gsc_a_h gsc_a_hc gs_ibl')

        if title_element:
            title = title_element.get_text()
            link = "https://scholar.google.com" + title_element['href']
            authors = authors_element.get_text() if authors_element else "N/A"
            year = year_element.get_text() if year_element else "N/A"

            publications.append({
                'title': title,
                'link': link,
                'authors': authors,
                'year': year
            })

    # Save publications to a JSON file
    with open('publications.json', 'w') as f:
        json.dump(publications, f, indent=4)

# Replace with the actual URL of the Google Scholar profile
profile_url = 'https://scholar.google.it/citations?hl=it&user=YEz4REYAAAAJ&view_op=list_works&sortby=pubdate'  # Example profile URL
fetch_google_scholar_publications(profile_url)
