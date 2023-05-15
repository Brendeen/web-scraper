from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


website = "https://en.wikipedia.org/wiki/Manga"


def get_citations_needed_count(url_str):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto(url_str)

        elements = page.query_selector_all(f":text-matches('citation needed')")

        print(elements)

        count = len(elements)

        print(f"There are {count} citations needed.")
        browser.close()
        return count


def get_citations_needed_report(url_str):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto(url_str)

        content = page.content()
        soup = BeautifulSoup(content, 'html.parser')

        paragraphs = soup.find_all('p')
        for paragraph in paragraphs:
            citation_needed = paragraph.find('sup', class_='noprint Inline-Template Template-Fact')
            if citation_needed:
                print(paragraph.text)


if __name__ == "__main__":
    get_citations_needed_count(website)
    get_citations_needed_report(website)
