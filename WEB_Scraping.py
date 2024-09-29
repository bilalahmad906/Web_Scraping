import requests
from bs4 import BeautifulSoup


def extract_pdf_links(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        pdf_links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            if 'prodotto' in href and (href.lower().split('/')[-3] == 'prodotto'):
                pdf_links.append(href)

        return set(pdf_links)
    else:
        print(f"Failed to fetch the webpage: {response.status_code}")
        return []


def main():
    # Replace this with the URL you want to extract PDF links from
    url = "https://siraradiosystems.com/categoria-prodotto/antennas/"
    pdf_links = extract_pdf_links(url)
    url = "https://siraradiosystems.com/categoria-prodotto/antennas/page/2/"
    pdf_links = extract_pdf_links(url)
    url = "https://siraradiosystems.com/categoria-prodotto/antennas/page/3/"
    pdf_links = extract_pdf_links(url)
    if pdf_links:
        print("PDF Links:")
        for link in pdf_links:
            print(link)
    else:
        print("No PDF links found.")


if __name__ == "__main__":
    main()
