#################################################################
# FILE : crawler.py
# WRITER : Nimrod M.
# EXERCISE : intro2cs1 ex6 2023
# DESCRIPTION: Implementing the Crawler of Moogle
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

import urllib.parse
import requests
import bs4
import pickle

def _get_webpage(url: str) -> str:
    """
    Getting webpage's HTML source
    """
    return requests.get(url).text

def _parse_href(href: str) -> str:
    """
    """
    return href.get('href') if 0 != len(href.get('href')) else None

def _extract_all_links(webpage: str) -> dict:
    """
    Extracts all the links (hrefs) from the given webpage (HTML source)

    :param webpage: HTML source of the webpage
    """
    page_links = {}
    soup = bs4.BeautifulSoup(webpage, "html.parser")
    # Iterating through all paragraphs, finding all the inks
    for paragraph in soup.find_all("p"):
        for link in paragraph.find_all("a"):
            page = _parse_href(link)
            # Making sure there is indeed a reference, as it may be empty
            if page is not None:
                # If there is already an entry, use it, if not, create it
                if page in page_links.keys():
                    page_links[page] += 1
                else:
                    page_links[page] = 1

    return page_links

def parse_index_file(file_path: str) -> list:
    """
    Utility function, if the index is packed in a file
    :return: List of the webpages.
    """
    with open(file_path, "r") as index_file:
        return index_file.read().split('\n')

def crawl(base_url: str, site_index):
    """
    :param base_url: The base URL of the website to crawl.
    :param site_index: The website index (all relative webpage paths)
    :return: The links table.
    """
    links_table = {}
    for current_entry in site_index:
        current_page = _get_webpage(urllib.parse.urljoin(base_url, current_entry))
        links_table[current_entry] = _extract_all_links(current_page)
    return links_table
