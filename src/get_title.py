"""
    get_title:
    n = 40
    params: doc -- html document

        # title is best choice, if no title, try headers, then try paragraph
        # this loop goes through all the headers to see if any are not null
        # (None) if so, return that header
        #if there are no header tags, then, look for the first paragraph tag
        # title.string removes the tag, so, <title>hello world!</title>
        # becomes hello world!
    Obtains a string document title, to appear as the main link for the
    page in the UI. Finds the first best, non-empty text tag, prioritizing <title>,
    <h1>, <h2>, <h3>, <h4>, <h5>, <h6>, then <p>, and returns a string
    of the first [n] characters. [n] is a constant that should be easily changeable.
    Provide an option for infinite [n], when n=-1.
    If no non-empty tags are found, returns an empty string.
"""
from bs4 import BeautifulSoup
def get_title(doc, title_req=True):
    if not title_req:
        return ""
    soup = BeautifulSoup(doc, 'html.parser')
    title = soup.title
    if not title:
        headers = [soup.h1, soup.h2, soup.h3, soup.h4, soup.h5, soup.h6]
        for header in headers:
            if header:
                return header.string.strip()
        potential_title = soup.p
        if potential_title:
            return potential_title.string
        else:
            return ""
    else:
        return title.string.strip()

