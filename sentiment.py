from typing import TextIO, List, Union, Dict, Tuple
from operator import itemgetter

# PART I: File I/O, strings, lists

def is_word(token: str) -> bool:
    '''Return True IFF token is an alphabetic word optionally containing
    forward slashes or dashes.
    
    >>> is_word('Amazing')
    True
    >>> is_word('writer/director')
    True
    >>> is_word('true-to-life')
    True
    >>> is_word("'re")
    False
    >>> is_word("1960s")
    False
    '''
    flag = True
    for cha in token:
        if cha == '-' or cha == '/':
            flag = False
        elif not cha.isalpha():
            return False
        else:
            flag = True
    return flag


def get_word_list(statement: str) -> List[str]:
    '''Return a list of words contained in statement, converted to lowercase. 
    Use is_word to determine whether each token in statement is a word.
    
    >>> get_word_list('A terrible , 1970s mess of true-crime nonsense from writer/director Shyamalan .')
    ['a', 'terrible', 'mess', 'of', 'true-crime', 'nonsense', 'from', 'writer/director', 'shyamalan']
    '''
    return_list = []
    token_list = statement.split(' ')
    for token in token_list:
        if is_word(token):
            return_list.append(token.lower())
    
    return return_list


def judge(score: float) -> str:
    '''Return 'negative' if score is 1.5 or less.
    Return 'positive' if score is 2.5 or more.
    Return 'neutral' otherwise.
    >>> judge(1.3)
    'negative'
    >>> judge(1.8)
    'neutral'
    >>> judge(3.4)
    'positive'
    '''
    if score <= 1.5:
        return 'negative'
    elif score >= 2.5:
        return 'positive'
    else:
        return 'neutral'




def word_kss_scan(word: str, file: TextIO) -> Union[None, float]:
    '''Given file composed of rated movie reviews, return the average score
    of all occurrences of word in file. If word does not occur in file, return None.
    [examples not required]
    '''
    num = 0
    sum_score = 0
    for line in file:
        line = line.rstrip()
        for item in get_word_list(line):
            if word.lower() == item:
                num += 1
                sum_score += float(line[0])
    if num:
        return sum_score / num



# PART II: Dictionaries 

def extract_kss(file: TextIO) -> Dict[str, List[int]]:
    '''Given file composed of rated movie reviews, return a dictionary
    containing all words in file as keys. For each key, store a list
    containing the total sum of review scores and the number of times
    the key has occurred as a value, e.g., { 'a' : [12, 4] }
    [examples not required]
    
    '''
    return_dict = {}
    for line in file:
        line = line.rstrip()
        word_list = get_word_list(line)
        for word in word_list:
            if word in return_dict:
                return_dict[word][0] += float(line[0])
                return_dict[word][1] += 1
            else:
                return_dict[word] = [float(line[0]), 1]   
    return return_dict



def word_kss(word: str, kss: Dict[str, List[int]]) -> Union[float, None]:
    '''Return the Known Sentiment Score of word if it appears in kss. 
    If word does not appear in kss, return None.
    [examples not required]
    '''    
    if word in kss:
        return kss[word][0] / kss[word][1]
             
             
def statement_pss(statement: str, kss: Dict[str, List[int]]) -> Union[float, None]:
    '''Return the Predicted Sentiment Score of statement based on
    word Known Sentiment Scores from kss.
    Return None if statement contains no words from kss.'''
    word_num = 0
    sum_score = 0
    word_list = get_word_list(statement)
    for word in word_list:
        if word in kss:
            word_num += 1
            sum_score += word_kss(word, kss)
    if word_num > 0:
        return sum_score / word_num



# PART III: Word Frequencies

def score(item: Tuple[str, List[int]]) -> float:
    '''Given item as a (key, value) tuple, return the
    ratio of the first and second integer in value
    '''
    return_list = item[1]
    return (return_list[0] / return_list[1])


def most_extreme_words(count: int, min_occ: int, kss:Dict[str, List[int]], pos:bool)-> list:
    '''Return a list of lists containing the count most extreme words
    that occur at least min_occ times in kss.
    Each item in the list is formatted as follows:
    [word, average score, number of occurrences]
    If pos is True, return the most positive words.
    If pos is False, return the most negative words.
    [examples not required]
    '''
    sorted_list = sorted(kss.items(), key=score, reverse=pos)
    i = 0
    return_list = []
    for item in sorted_list:
        if i < count and item[1][1] >= min_occ:
            i += 1
            return_list.append([item[0], score(item), item[1][1]])
        
    return return_list
    
    
def most_negative_words(count, min_occ, kss):
    '''Return a list of the count most negative words that occur at least min_occ times in kss.
    '''
    return most_extreme_words(count, min_occ, kss, False)

    
def most_positive_words(count, min_occ, kss):
    '''Return a list of the count most positive words that occur at least min_occ times in kss.
    '''
    
    return most_extreme_words(count, min_occ, kss, True)

        
    
if __name__ == "__main__":

# Pick a dataset    
    #dataset = 'tiny.txt'
    #dataset = 'small.txt'
    #dataset = 'medium.txt'
    dataset = 'full.txt'
    
    # Your test code here
    pass


