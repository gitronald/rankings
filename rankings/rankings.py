# coding=utf8
"""
Measures for comparing ranked lists.
"""

from __future__ import division
from string import ascii_letters, digits
from jellyfish import damerau_levenshtein_distance
from numpy import random
__author__ = """Ronald E. Robertson (robertson.ron@husky.neu.edu)"""
__all__ = ['alphanumerics',
           'random_string',
           'generate_alphanum_dict',
           'rank_as_string',
           'compare_ranks']

def alphanumerics():
    """Generate all upper and lowercase letters and digits"""
    return ascii_letters + digits

def random_string(length, replacement = False, selection = None):
    """Generate a random string of alphanumerics"""
    selection = list(alphanumerics()) if selection is None else selection
    return ''.join(random.choice(selection, length, replace=replacement))

def generate_alphanum_dict(list1):
    """Generate an alphanumeric dictionary
    
    Creates an alphanumeric dictionary where they keys are the
    inputted list items and the values are selected from a random
    alphanumeric string generated with no replacement.
    """
    chars = random_string(len(list1))   
    alphanum_dict = {item: chars[i] for i, item in enumerate(list1)}
    return alphanum_dict

def rank_as_string(list1, alphanum_index):
    """
    Convert a ranked list of items into a string of characters 
    based on a given dictionary `alph` of the format that contains 
    the ranked items and a random alphanumeric to represent it.
    
    Parameters
    ----------
        list1 : list
            A list of rankings to be converted to characters
            
        alph : dict
            A dictionary containing the items in list1 as keys
            and unique characters as the values.
    """
    return ''.join([alphanum_index[l] for l in list1])
    
def jaccard_index(list1, list2, digits=3):
    """Calculate Jaccard Index
    The size of the intersection over the size of the union of two lists. Provides a similarity measure of two 
           lists without regard to order    
    
    """
    intersection = set(list1).intersection(set(list2))
    union = set(list1).union(set(list2))
    j = float(len(intersection)) / float(len(union))
    j = round(j, digits)
    return j
    
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
       j : Jaccard Index - the size of the intersection over the size of 
           the union of two lists. Provides a similarity measure of two 
           lists without regard to order.
			 dist : Damerau-Levenshtein edit distance [1] - the number of list 
           items that must be deleted, inserted, substituted, or swapped 
           to make the rankings of the two lists identical.

    Examples
    --------
    >>> list1 = ['sam', 'sue', 'stew', 'baloo', 'baloo']
    >>> list2 = ['sue', 'sam', 'baloo', 'new', 'baloo']
    >>> compare_ranks(list1, list2)
    (0.6, 3)

    Notes
    -----
    This function uses jellyfish.damerau_levenshtein_distance

    References
    ----------
    .. [1] F. J. Damerau, A technique for computer detection and correction
    			 of spelling errors. CACM, 7(3), 1964.

    """
    j = jaccard_index(list1, list2)
    
    union = set(list1).union(set(list2))
    alphanum_dict = generate_alphanum_dict(union)  
    strings = map(lambda x : rank_as_string(x, alphanum_dict), [list1, list2])
    dist = damerau_levenshtein_distance(unicode(strings[0]), unicode(strings[1]))

    for i, string in enumerate(strings):
        print "list%d: %s  len: %d" % (i, string, len(string))
        
    return (j, dist)
