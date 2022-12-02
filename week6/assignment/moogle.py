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
import ranker

def _add_crawler_parser(subparser):
    """
    """
    crawl_parser = subparser.add_parser('crawl', 
        help="Extracting links information",)
    crawl_parser.add_argument('base_url', 
        help="The base URL address to crawl")
    crawl_parser.add_argument('index_file', 
        help="Path to the file storing the index of the website")
    crawl_parser.add_argument('out_file', 
        help="Path to the output file")

def _add_ranker_parser(subparser):
    """
    """
    ranker_parser = subparser.add_parser('rank_page',
        help="Ranking all the pages in the given website")
    ranker_parser.add_argument('iterations',
        help="Number of iterations for ranking",
        type=int)
    ranker_parser.add_argument('links_file',
        help="Path to the links dictionary (from crawl)")
    ranker_parser.add_argument('out_file',
        help="Path to the output file")

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

    _add_crawler_parser(subparsers)
    _add_ranker_parser(subparsers)

    return vars(parser.parse_args())
    
def _save_pickle(file_path: str, obj) -> None:
    """
    Saving the given object to a file using pickle
    """
    with open(file_path, "wb") as pickle_file:
        pickle.dump(obj, pickle_file)

def _load_pickle(file_path: str):
    """
    """
    with open(file_path, "rb") as pickle_file:
        return pickle.load(pickle_file)

def _execute_crawler_action(params: dict) -> None:
    """
    """
    links_table = crawler.crawl(
        params['base_url'],
        crawler.parse_index_file(params['index_file']))
    _save_pickle(params['out_file'], links_table)

def _execute_ranker_action(params: dict) -> None:
    """
    """
    ranking = ranker.rank_pages(
        _load_pickle(params['links_file']), 
        params['iterations'])
    _save_pickle(params['out_file'], ranking)

def main():
    """
    """
    actions = {
        'crawl': _execute_crawler_action,
        'rank_page': _execute_ranker_action
    }

    params = _parse_parameters()
    actions[params["action"]](params)

if __name__ == "__main__":
    main()
