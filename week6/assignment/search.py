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
    if page not in ranks_table:
        return 0

    minimal_value = 0
    for word in query.split(' '):
        # The word is not indexed, searching it is meaningless
        if word not in word_dict:
            continue
        
        # The requested page doesn't have this word
        if page not in word_dict[word]:
            continue

        if minimal_value >= word_dict[word][page]:
            minimal_value = word_dict[word][page]

    return minimal_value * ranks_table[page]

def search_query(query: str, ranks_table: RanksTable, words_dict: WordDict):
    """
    """
    scores = {}
    for page in ranks_table:
        scores[page] = calculate_page_score(page, query, ranks_table, words_dict)

    sorted_scores = dict(sorted(scores.items(), key=lambda score: score[1]))
    return sorted_scores
    