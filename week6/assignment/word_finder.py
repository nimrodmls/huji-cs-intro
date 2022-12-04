#################################################################
# FILE : word_finder.py
# WRITER : Nimrod M.
# EXERCISE : intro2cs1 ex6 2023
# DESCRIPTION: Implementing the Word Finder Logic of Moogle
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

import bs4
import common

WordDict = dict[str, dict[str, int]]

def _extract_words_from_page(webpage: str, page_path: str, words_dict: WordDict) -> None:
    """
    Extracts all words from the given webpage.
    The given word dictionary is updated.

    :param webpage: The HTML source of the page.
    """
    soup = bs4.BeautifulSoup(webpage, "html.parser")
    # Iterating through all paragraphs, finding all the inks
    for paragraph in soup.find_all("p"):
        words_list = paragraph.text.split()
        for word in words_list:

            # Removing garbage from the word
            if 0 != len(word):

                # Dealing with the possibility of having uninitialized fields
                if word not in words_dict:
                    words_dict[word] = {}
                if page_path not in words_dict[word]:
                    words_dict[word][page_path] = 0

                words_dict[word][page_path] += 1

def extract_words(base_url: str, site_index: list[str]) -> WordDict:
    """
    Extracts all words from the given website.
    The words are organized in a dictionary, 
    with every value being a dictionary of page to number of mentions
    """
    words_dict = {}
    for current_entry in site_index:
        current_page = common.get_webpage(base_url, current_entry)
        _extract_words_from_page(current_page, current_entry, words_dict)
    return words_dict
