#################################################################
# FILE : crawler.py
# WRITER : Nimrod M.
# EXERCISE : intro2cs1 ex6 2023
# DESCRIPTION: Implementing the Crawler of Moogle
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

import bs4
import common

LinksTable = dict[str, dict[str, int]]

def _parse_href(href: str) -> str:
    """
    Parsing the href.
    If it's empty, None returned.
    """
    return href.get('href') if 0 != len(href.get('href')) else None

def _extract_all_links(webpage: str, index: list[str]) -> dict:
    """
    Extracts all the links (hrefs) from the given webpage (HTML source)
    Links which doesn't appear in the given index, are hence not added.

    :param webpage: HTML source of the webpage
    """
    page_links = {}
    soup = bs4.BeautifulSoup(webpage, "html.parser")
    # Iterating through all paragraphs, finding all the inks
    for paragraph in soup.find_all("p"):
        for link in paragraph.find_all("a"):
            page = _parse_href(link)
            # Making sure there is indeed a reference, as it may be empty
            if (page is not None) and (page in index):

                # If there is already an entry, use it, if not, create it
                if page not in page_links.keys():
                    page_links[page] = 0

                page_links[page] += 1

    return page_links

def crawl(base_url: str, site_index: list[str]) -> LinksTable:
    """
    :param base_url: The base URL of the website to crawl.
    :param site_index: The website index (all relative webpage paths)
    :return: The links table.
    """
    links_table = {}
    for current_entry in site_index:
        current_page = common.get_webpage(base_url, current_entry)
        links_table[current_entry] = _extract_all_links(current_page, site_index)
    return links_table
