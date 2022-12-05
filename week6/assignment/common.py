#################################################################
# FILE : common.py
# WRITER : Nimrod M.
# EXERCISE : intro2cs1 ex6 2023
# DESCRIPTION: Some common functionality used around all code
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

import requests
import urllib
import pickle

def save_pickle(file_path: str, obj) -> None:
    """
    Saving the given object to a file using pickle
    """
    with open(file_path, "wb") as pickle_file:
        pickle.dump(obj, pickle_file)

def load_pickle(file_path: str):
    """
    Loading a pickle object from the given file
    """
    with open(file_path, "rb") as pickle_file:
        return pickle.load(pickle_file)

def get_webpage(base_url: str, path: str) -> str:
    """
    Getting webpage's HTML source 
    """
    return requests.get(urllib.parse.urljoin(base_url, path)).text

def parse_index_file(file_path: str) -> list:
    """
    Utility function, if the index is packed in a file
    :return: List of the webpages.
    """
    with open(file_path, "r") as index_file:
        return index_file.read().splitlines()

def sort_dict_by_value(dict_to_sort: dict) -> tuple[dict, list]:
    """
    Sortng the given dictionary by the value.
    """
    return dict(sorted(dict_to_sort.items(), key=lambda rank: rank[1], reverse=True))
    