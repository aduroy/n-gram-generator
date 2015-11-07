'''
Created on 7 nov. 2015

@author: Antonin Duroy
'''

import codecs
import numpy as np

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.util import ngrams
from nltk import FreqDist, ConditionalFreqDist
from scipy import stats
from nltk.probability import ConditionalFreqDist

class NgramModel:
    
    def __init__(self, filepath, n):
        self.text = self._loadFile(filepath)
        self.n = n
    
    def _getStartingWords(self):
        """Extract the first words of the sentences in the text. They will become
        the entry point of the text generator.
        """
        sentences = sent_tokenize(self.text, language='french')
        return [word_tokenize(sentence, language='french')[0] for sentence in sentences]
    
    def _selectFirstWord(self, first_words):
        fdist = FreqDist(first_words)
        x_k = np.arange(fdist.B())
#         candidates = list({fw for fw in first_words})
        candidates = [word for word in fdist]
        p_k = [fdist.freq(word) for word in candidates]
        custm = stats.rv_discrete(values=(x_k, p_k))
        return candidates[custm.rvs()]
    
    def _selectNextWord(self, ngram, cfdist=None):
        """
        """
        if len(ngram) == 0:
            first_words = self._getStartingWords()
            return self._selectFirstWord(first_words)
        
        xk = np.arange(cfdist[ngram].B())
        pk = []
        candidates = []
        for next_word in cfdist[ngram]:
            candidates.append(next_word)
            pk.append(cfdist[ngram].freq(next_word))
        
        custm = stats.rv_discrete(values=(xk, pk))
        return candidates[custm.rvs()]
    
    
    def _loadFile(self, filepath):
        with codecs.open(filepath, 'r', encoding='utf-8') as f:
            return f.read().replace('\n', ' ')

    def generateText(self):
        """
        """
        if self.n < 1:
            return
        
        words = word_tokenize(self.text, language='french')
        # Extract [0-n]-grams
        all_igrams = {i:ngrams(words, i) for i in range(1, self.n+1)}
        # Compute conditional frequency distribution for each i-gram
        ngrams_cfd = {i:ConditionalFreqDist((igram[:-1], igram[-1]) for igram in igrams) for i, igrams in all_igrams.items()}
        
        i = 1
        new_word = ''
        frame = ()
        while new_word != '.':
            new_word = self._selectNextWord(frame, ngrams_cfd[i])
            frame += (new_word,)
            if i < self.n:
                i += 1
            elif i == self.n:
                frame = frame[1:]
            print(new_word, end=' ')

if __name__ == '__main__':
    ngramModel = NgramModel('../data/bible_fr.txt', 3)
    ngramModel.generateText()
