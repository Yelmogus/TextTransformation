'''
    get_title:
    n = 40
    params: doc -- html document
    
    Obtains a string document title, to appear as the main link for the
    page in the UI. Finds the first best, non-empty text tag, prioritizing <title>,
    <h1>, <h2>, <h3>, <h4>, <h5>, <h6>, then <p>, and returns a string
    of the first [n] characters. [n] is a constant that should be easily changeable.
    If no non-empty tags are found, returns an empty string.
    
'''
def get_title(doc)
    return ""
