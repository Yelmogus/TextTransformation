"""
calculateNGrams
params: String data
        int n
errors:
    - If the data is empty, return an empty list
    - If n is not such that 1 <= n <= number of words in the data,
      return an empty list
Breaks the data_string into ngrams, then assigns each gram by its relevant position in the string
        data_str = 'hello world this is a string' and n = 2 then:
        ngram_list = [(0, 'hello world'), (1, 'world this'), (2, 'this is'), (3, 'is a'), (4, 'a string')]

description: Given a string data_str and and list n_list, calculateNGrams will:
    1.) Find all the n grams for the n's in n_list
    2.) Find out how many times those n grams appear in the data
    3.) Find out their relative locations in the data

ex: INPUT: "hello other search engine team hello other"; [2]
ex: OUTPUT: [{"hello other", 2, [0, 5]} , {"other search", 1, [1]},
            {"search engine"}, 1, [2]}, {"engine team", 1, [3]}, {"team hello"},
            1, [4]}]
"""

# from pattern.text.en import ngrams
from nltk.util import ngrams as ng

def calculate_ngrams(data_str, n_list):
    """ Breaks the data_string into ngrams, then assigns each gram by its relevant position in the string
        data_str = "hello world this is a string" and n = 2 then:
        ngram_list = [(0, 'hello world'), (1, 'world this'), (2, 'this is'), (3, 'is a'), (4, 'a string')]"""
    all_ngrams = dict.fromkeys([str(n) for n in n_list], {})
    for n in n_list:
        ngram_index = {}
        tokens = [token for token in data_str.split(" ") if token != ""]
        # ngram_list = [(pos, " ".join(gram).strip()) for pos, gram in enumerate(ngrams(data_str, n=n))]
        ngram_list = [(pos, " ".join(gram).strip()) for pos, gram in enumerate(ng(tokens, n=n))]
        for pos, gram in ngram_list:
            if gram in ngram_index:
                ngram_index[gram].append(pos)
            else:
                ngram_index[gram] = [pos]
        all_ngrams[str(n)] = ngram_index
    return all_ngrams
