import re
#matchingStrings HackerRank
def matchingStrings(strings, queries):
    result = []
    for query in queries:
        result.append(sum([1 for i in strings if i == query]))
    return result



if __name__ == "__main__":
    strings = ['ab', 'ab', 'abc']
    queries = ['ab', 'abc', 'bc']
    matchingStrings(strings=strings, queries=queries)
