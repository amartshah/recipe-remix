'''Version 0.1'''
from parser import Parser

def autograder(url):
    '''Accepts the URL for a recipe, and returns a dictionary of the
    parsed results in the correct format. See project sheet for
    details on correct format.'''
    p = Parser.new(url)
    return p.fully_parsed()
