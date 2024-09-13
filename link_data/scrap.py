import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


def scrape_linkedin_data(query):
    search_url = f"https://www.linkedin.com/search/results/people/?keywords={query}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    }
    
    response = requests.get(search_url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch data from LinkedIn, status code: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    
    with open('data.html', 'w', encoding='utf-8') as file:
        file.write(str(soup))
        print("HTML data has been written to data.html")
        
    profiles = []
    
    for profile in soup.find_all('div', class_='search-result__info'):
        name = profile.find('span', class_='name').get_text(strip=True)
        position = profile.find('span', class_='position').get_text(strip=True)
        location = profile.find('span', class_='location').get_text(strip=True)

        profiles.append({
            'Name': name,
            'Position': position,
            'Location': location
        })

    df = pd.DataFrame(profiles)

    return df


def save_to_csv(df, filename='linkedin_data.csv'):
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")


def main():
    
    query = input("Enter the keyword or name to search on LinkedIn: ")
    
    data = scrape_linkedin_data(query)
    
    if data is not None:
        save_to_csv(data)
    else:
        print("No data found or failed to scrape.")


if __name__ == "__main__":
    main()
