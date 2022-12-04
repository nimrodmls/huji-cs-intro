#################################################################
# FILE : search.py
# WRITER : Nimrod M.
# EXERCISE : intro2cs1 ex6 2023
# DESCRIPTION: Implementing the Search of Moogle
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

import common
from ranker import RanksTable
from word_finder import WordDict

def calculate_page_score(page: str, query:str, ranks_table: RanksTable, word_dict: WordDict) -> float:
    """
    """
    minimal_value = None
    for word in query.split():
        # The word is not indexed, or the requested page doesn't have this word
        # The requested page doesn't have this word
        if (word not in word_dict) or (page not in word_dict[word]):
            return 0
        
        if (minimal_value is None) or (minimal_value >= word_dict[word][page]):
            minimal_value = word_dict[word][page]

    if minimal_value is None:
        return 0
        
    return minimal_value * ranks_table[page]

def search_query(query: str, max_results: int, ranks_table: RanksTable, words_dict: WordDict):
    """
    Searching the given query using the given ranks and words tables.
    If the query doesn't appear in any of the first pages from 'max_results',
    then the search is rendered empty of results.
    Otherwise, the search scores are returned. They should be sorted if needed.
    """
    scores = {}
    sorted_ranks = common.sort_dict_by_value(ranks_table)

    # Taking only the max_results amount of pages from the ranks
    # If there are less pages in the rank table than the max results requested,
    # take the minimal value.
    for page in list(sorted_ranks.keys())[:min(max_results, len(sorted_ranks))]:
        score = calculate_page_score(page, query, ranks_table, words_dict)
        if 0 == score: # If there are no results for a certain word, return
            return {}
        scores[page] = score

    return scores
