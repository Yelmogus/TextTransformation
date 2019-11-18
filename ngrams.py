'''
calculateNGrams
params: String data
        int n
errors:
    - If the data is empty, return an empty list
    - If n is not such that 1 <= n <= number of words in the data,
      return an empty list


description: Given a string data and and int n, calculateNGrams will:
    1.) Find all the n grams
    2.) Find out how many times those n grams appear in the data
    3.) Find out their relative locations in the data

ex: INPUT: "hello other search engine team hello other"; 2
ex: OUTPUT: [{"hello other", 2, [0, 5]} , {"other search", 1, [1]},
            {"search engine"}, 1, [2]}, {"engine team", 1, [3]}, {"team hello"},
            1, [4]}]
'''
def calculateNGrams(file_name, n):
    retrun [0]
