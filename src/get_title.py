'''
    get_title:
    n = 40
    params: doc -- html document

    Obtains a string document title, to appear as the main link for the
    page in the UI. Finds the first best, non-empty text tag, prioritizing <title>,
    <h1>, <h2>, <h3>, <h4>, <h5>, <h6>, then <p>, and returns a string
    of the first [n] characters. [n] is a constant that should be easily changeable.
    Provide an option for infinite [n], when n=-1.
    If no non-empty tags are found, returns an empty string.

'''
from bs4 import BeautifulSoup
def get_title(doc):
    soup = BeautifulSoup(doc, 'html.parser')
    title = soup.title
    #title is best choice, if no title, try headers, then try paragraph
    if(title == None):
        headers = [soup.h1,soup.h2,soup.h3,soup.h4,soup.h5,soup.h6]
        #this loop goes through all the headers to see if any are not null
        #(None) if so, return that header
        for i in headers:
            if(i != None):
                return i.string
        #if there are no header tags, then, look for the first paragraph tag
        title = soup.p
        if(title == None):
            #if no paragraph tag, return an empty string
            return ""
        else:
            return title.string
    else:
        return title.string
    #title.string removes the tag, so, <title>hello world!</title>
    #becomes hello world!
