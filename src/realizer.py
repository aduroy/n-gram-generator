'''
Created on 8 nov. 2015

@author: Antonin Duroy
'''

class Punctuation():
    """
    """
    
    def __init__(self, lspace, value, rspace):
        self.value = value
        self.lspace = lspace
        self.rspace = rspace
    
    def tokenize(self):
        """
        """
        tokens = []
        if self.lspace is True:
            tokens.append(' ')
        tokens.append(self.value)
        if self.rspace is True:
            tokens.append(' ')
        return tokens


class Realizer():
    """
    """
    
    punctuations = {'french': {'.': Punctuation(None, '.', True),
                               ',': Punctuation(None, ',', True),
                               ';': Punctuation(True, ';', True),
                               ':': Punctuation(True, ':', True),
                               '...': Punctuation(None, '...', True),
                               '?': Punctuation(True, '?', True),
                               '!': Punctuation(True, '!', True),
                               '-': Punctuation(True, '-', True),
                               '(': Punctuation(True, '(', None),
                               ')': Punctuation(None, ')', True),
                               '[': Punctuation(True, '[', None),
                               ']': Punctuation(None, ']', True),
                               '``': Punctuation(True, '"', None),
                                "''": Punctuation(None, '"', True)
                               },
                    'english': {'.': Punctuation(None, '.', True),
                                ',': Punctuation(None, ',', True),
                                ';': Punctuation(None, ';', True),
                                ':': Punctuation(None, ':', True),
                                '...': Punctuation(None, '...', True),
                                '?': Punctuation(None, '?', True),
                                '!': Punctuation(None, '!', True),
                                '-': Punctuation(None, '-', None),
                                '(': Punctuation(True, '(', None),
                                ')': Punctuation(None, ')', True),
                                '[': Punctuation(True, '[', None),
                                ']': Punctuation(None, ']', True),
                                '``': Punctuation(True, '"', None),
                                "''": Punctuation(None, '"', True)
                                }
                    }
    
    def __init__(self, lang='english'):
        self.lang = lang
    
    def realize(self, words=[]):
        """ Transform a list of tokens into a correct and readable text.
        """
        realized_words = []
        punctuations = self.punctuations[self.lang].keys()
        for word in words:
            if word in punctuations:
                punct = self.punctuations[self.lang][word]
                if realized_words[-1] == ' ':
                    realized_words = realized_words[:-1] + punct.tokenize()
                else:
                    realized_words += punct.tokenize()
            else:
                realized_words += [word, ' ']
        
        return ''.join(realized_words).strip()