
import string
import random
from collections import Counter
from jellyfish import damerau_levenshtein_distance

def alphanumerics():
    """Generate all upper and lowercase letters and digits"""
    return string.ascii_letters + string.digits

def random_string(length, selection = None):
    """Generate a random string of alphanumerics"""
    selection = list(alphanumerics()) if selection is None else selection
    return ''.join(np.random.choice(selection, length, replace=False))

def compare_ranks(list1, list2):
    """Compare two ranked lists

    Parameters
    ----------
    list1 : list
       Ranked (ordered) list

    list2 : list
       A ranked list to compare against the first

    Returns
    -------
    (j, dist) : tuple
       j : Jaccard Index - the size of the intersection over the size of the union of 
       		 two lists. Provides a similarity measure of two lists without regard to order.
			 dist : the Damerau-Levenshtein edit distance [1] between two lists. The number 
			 		 list items that must be deleted, inserted, substituted, or swapped to make
			 		 the two lists identical
       measured as the percent overlap in list items. Edit disctance is measured
       as the number of list item swaps would be required for the two lists to be 
       identical

    Examples
    --------
    >>> list1 = ['sam', 'sue', 'stew', 'baloo']
    >>> list2 = ['sue', 'sam', 'baloo', 'new']
    >>> compare_ranks(list1, list2)

    Notes
    -----
    This calls jellyfish.damerau_levenshtein_distance

    References
    ----------
    .. [1] F. J. Damerau, A technique for computer detection and correction
    			 of spelling errors. CACM, 7(3), 1964.

    """

    c1 = Counter(list1)
    c2 = Counter(list2)
    c_all = c1 | c2
    
    overlap = len([x for x in c1 if x in c2])
    total = len(c1) if len(c1) > len(c2) else len(c2)
    j = overlap / total
    j = round(j, 3)
    
    alph = {}
    chars = random_string(len(c_all))
    for i, item in enumerate(c_all):
        print chars[i], item
        alph[item] = chars[i]

    alph = {item: char for char in chars}    
    
    str1 = rank_as_string(list1, alph)
    str2 = rank_as_string(list2, alph)
    
    dist = damerau_levenshtein_distance(unicode(str1), unicode(str2))

    print("list1: ", str1, "len: ", len(str1))
    print("list2: ", str2, "len: ", len(str2))
    return (j, dist)

def rank_as_string(list1, alph):
    '''
    Convert a ranked list of items into a string of characters 
    based on a given dictionary `alph` of the format that contains 
    the ranked items and a random alphanumeric to represent it. 
    (e.g. alph[list1[0]] = 'k', alph[list1[1]] = '4')
    
    
    Args:
        urls1 (:list: str) A list of unique rankings to be converted to letters
        alph (str) An alphabet 
    '''
    string = ''
    for r in list1:
        string += alph[r]
    return string
