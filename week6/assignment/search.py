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

def _calculate_page_score(page: str, query:str, ranks_table: RanksTable, word_dict: WordDict) -> float:
    """
    """
    minimal_value = None
    for word in query.split():
        # The word is not indexed, ignore it
        if word not in word_dict:
            continue
        
        # The requested page doesn't have this word
        if page not in word_dict[word]:
            return 0
        
        if (minimal_value is None) or (minimal_value >= word_dict[word][page]):
            minimal_value = word_dict[word][page]

    if minimal_value is None:
        return 0
        
    return minimal_value * ranks_table[page]

def search_query(query: str, max_results: int, ranks_table: RanksTable, words_dict: WordDict):
    """
    Searching the given query using the given ranks and words tables.
    """
    scores = {}
    sorted_ranks = common.sort_dict_by_value(ranks_table)

    # Taking only the max_results amount of pages from the ranks
    # If there are less pages in the rank table than the max results requested,
    # take the minimal value.
    for page in sorted_ranks:
        # If we reached the max scores we should not continue for another search
        if len(scores) == max_results:
            return scores

        score = _calculate_page_score(page, query, ranks_table, words_dict)
        # If there are no results for a certain word in this page, we continue searching
        if 0 == score: 
            continue
        
        scores[page] = score

    # If we reached here, max_results was more than len(ranks_table), but it's fine!
    return scores
