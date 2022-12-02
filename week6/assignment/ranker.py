#################################################################
# FILE : ranker.py
# WRITER : Nimrod M.
# EXERCISE : intro2cs1 ex6 2023
# DESCRIPTION: Implementing the Crawler of Moogle
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

def _do_iteration(ranks: dict, links_table) -> dict:
    """
    """
    new_ranks = {}
    for current_page in ranks:
        for link in links_table:
            # If it's the same page, don't count it in
            if current_page != link:

                # If the link isn't already in the new ranks, add it
                if link not in new_ranks.keys():
                    new_ranks[link] = 0
                
                if link in links_table[current_page]:
                    new_ranks[link] += ranks[current_page] * \
                        (links_table[current_page][link] / \
                        sum(links_table[current_page].values()))
    return new_ranks

def rank_pages(links_table, iterations):
    """
    """
    ranks = {name: 1 for name in links_table}
    for iteration in range(iterations):
        ranks = _do_iteration(ranks, links_table)

    return ranks
