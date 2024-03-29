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

# Internals imports
import common
import word_finder
import crawler
import ranker
import search

def _add_crawler_parser(subparser):
    """
    Creating the Crawl Action subparser
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
    Creating the Rank Page Action subparser
    """
    ranker_parser = subparser.add_parser('page_rank',
        help="Ranking all the pages in the given website")
    ranker_parser.add_argument('iterations',
        help="Number of iterations for ranking",
        type=int)
    ranker_parser.add_argument('links_file',
        help="Path to the links dictionary (from crawl)")
    ranker_parser.add_argument('out_file',
        help="Path to the output file")

def _add_word_dict_parser(subparser):
    """
    Creating the Word Dict Action subparser
    """
    word_dict_parser = subparser.add_parser('words_dict',
        help="Extracting all the words from the website")
    word_dict_parser.add_argument('base_url', 
        help="The base URL address to crawl")
    word_dict_parser.add_argument('index_file', 
        help="Path to the file storing the index of the website")
    word_dict_parser.add_argument('out_file', 
        help="Path to the output file")

def _add_search_parser(subparser):
    """
    Creating the Search Action subparser
    """
    search_parser = subparser.add_parser('search',
        help="Searching Moogle with the supplied query")
    search_parser.add_argument('query',
        help="The query to search in Moogle. MUST HAVE QUOTATION MARKS!")
    search_parser.add_argument('rank_file',
        help="Path to the ranks file on the drive")
    search_parser.add_argument('words_file',
        help="Path to the words index on the drive")
    search_parser.add_argument('max_results',
        help="How many results to show",
        type=int)

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
    _add_word_dict_parser(subparsers)
    _add_search_parser(subparsers)

    return vars(parser.parse_args())

def _execute_crawler_action(params: dict) -> None:
    """
    Run the Crawl Action with the given parameters
    """
    links_table = crawler.crawl(
        params['base_url'],
        common.parse_index_file(params['index_file']))
    common.save_pickle(params['out_file'], links_table)

def _execute_ranker_action(params: dict) -> None:
    """
    Run the Page Rank Action with the given parameters
    """
    ranking = ranker.rank_pages(
        common.load_pickle(params['links_file']), 
        params['iterations'])
    common.save_pickle(params['out_file'], ranking)

def _execute_word_dict_action(params: dict) -> None:
    """
    Run the Word Dictionary assembly with the given parameters
    """
    word_dict = word_finder.extract_words(
        params['base_url'], 
        common.parse_index_file(params['index_file']))
    common.save_pickle(params['out_file'], word_dict)

def _execute_search_action(params: dict) -> None:
    """
    Execute the Search Query Action with the given parameters
    This function *prints* to the screen the results
    """
    ranks = common.load_pickle(params['rank_file'])
    words = common.load_pickle(params['words_file'])
    results = search.search_query(params['query'], 
                                  params['max_results'],
                                  ranks, 
                                  words)

    sorted_results = common.sort_dict_by_value(results)
    for current_page in sorted_results:
        print("{page} {score}".format(page=current_page, 
                                      score=sorted_results[current_page]))

def _create_submission_results():
    """
    Utility function for creating submission results file.
    This function is not relevant for all the other parts of the code.
    Function is intentionally not used.
    """
    base_url = "https://www.cs.huji.ac.il/w~intro2cs1/ex6/wiki/"
    iterations = 100
    max_results = 4
    queries = ["scar", "Crookshanks", "Horcrux", "Pensieve McGonagall", "broom wand cape"]
    index = common.parse_index_file("week6\\assignment\\small_index.txt")
    links_table = crawler.crawl(base_url,index)
    ranks_table = ranker.rank_pages(links_table, iterations)
    word_dict = word_finder.extract_words(base_url, index)
    with open("C:\\Temp\\results.txt", "w") as results_file:
        for query in queries:
            results = search.search_query(query, max_results, ranks_table, word_dict)
            sorted_results = common.sort_dict_by_value(results)
            for result in sorted_results:
                results_file.write("{page} {score}\n".format(page=result, 
                                      score=sorted_results[result]))
            results_file.write("**********\n")

def main():
    """
    The main program, executes the need action with the parameters rececived
    from the user.
    """
    actions = {
        'crawl': _execute_crawler_action,
        'page_rank': _execute_ranker_action,
        'words_dict': _execute_word_dict_action,
        'search': _execute_search_action
    }

    params = _parse_parameters()
    actions[params["action"]](params)

if __name__ == "__main__":
    main()
