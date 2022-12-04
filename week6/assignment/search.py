#################################################################
# FILE : search.py
# WRITER : Nimrod M.
# EXERCISE : intro2cs1 ex6 2023
# DESCRIPTION: Implementing the Search of Moogle
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

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
    """
    scores = {}
    sorted_ranks = dict(sorted(ranks_table.items(), key=lambda rank: rank[1]))
    all_pages = list(sorted_ranks.keys())
    all_pages.reverse()
    
    for page in range(min(max_results, len(sorted_ranks))):
        score = calculate_page_score(all_pages[page], query, ranks_table, words_dict)
        if 0 == score: # If there are no results for a certain word, return
            return {}
        scores[all_pages[page]] = score

    sorted_scores = dict(sorted(scores.items(), key=lambda score: score[1]))
    return sorted_scores
