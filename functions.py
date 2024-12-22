def create_search_url(search_term):
    search_words = search_term.split()
    search_word_list = list(search_words)
    search_in_url =""
    search_in_url = "+".join(search_word_list)
    return search_in_url
