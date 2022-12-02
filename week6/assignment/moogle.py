#################################################################
# FILE : moogle.py
# WRITER : Nimrod M.
# EXERCISE : intro2cs1 ex6 2023
# DESCRIPTION: The main program of Moogle
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

# External imports
import argparse
import pickle

# Internals imports
import crawler

def _parse_parameters():
    """
    Getting the command line arguments from the user.
    """
    parser = argparse.ArgumentParser(
        description="Searching through the Harry Potter Web")
    subparsers = parser.add_subparsers(
        help="One of the actions below", 
        required=True, 
        metavar="[Action]",
        dest="action")

    # Crawler subparser
    crawl_parser = subparsers.add_parser('crawl', 
        help="Extracting links information",)
    crawl_parser.add_argument('base_url', 
        help="The base URL address to crawl")
    crawl_parser.add_argument('index_file', 
        help="File storing the index of the website")
    crawl_parser.add_argument('out_file', 
        help="The output file")

    return vars(parser.parse_args())
    
def _save_pickle(file_path: str, obj) -> None:
    """
    Saving the given object to a file using pickle
    """
    with open(file_path, "wb") as pickle_file:
        pickle.dump(obj, pickle_file)

def _execute_crawler_action(params: dict):
    """
    """
    links_table = crawler.crawl(
        params['base_url'],
        crawler.parse_index_file(params['index_file']))
    _save_pickle(params['out_file'], links_table)

def main():
    """
    """
    actions = {
        'crawl': _execute_crawler_action
    }

    params = _parse_parameters()
    actions[params["action"]](params)

if __name__ == "__main__":
    main()
