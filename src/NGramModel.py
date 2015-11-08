'''
Created on 7 nov. 2015

@author: Antonin Duroy
'''

import codecs
import numpy as np

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import ConditionalFreqDist
from nltk.util import ngrams
from nltk import FreqDist
from scipy import stats


class NgramModel:
    
    def __init__(self, filepath, lang='french'):
        self.text = self._loadFile(filepath)
        self.lang = lang
        self.sentences = sent_tokenize(self.text, language='french')
        self.starting_words = self._getStartingWords()
    
    def _loadFile(self, filepath):
        with codecs.open(filepath, 'r', encoding='utf-8') as f:
            return f.read().replace('\n', ' ')
    
    def _getStartingWords(self):
        """Extract the first words of the sentences in the text. They will become
        the entry point of the text generator.
        """
        return [word_tokenize(sentence, language='french')[0] for sentence in self.sentences]
    
    def _selectFirstWord(self):
        """
        """
        fdist = FreqDist(self.starting_words)
        x_k = np.arange(fdist.B())
        candidates = [word for word in fdist]
        p_k = [fdist.freq(word) for word in candidates]
        custm = stats.rv_discrete(values=(x_k, p_k))
        return candidates[custm.rvs()]
    
    def _selectNextWord(self, ngram, cfdist=None):
        """
        """
        if len(ngram) == 0:
            return self._selectFirstWord()
        
        xk = np.arange(cfdist[ngram].B())
        pk = []
        candidates = []
        for next_word in cfdist[ngram]:
            candidates.append(next_word)
            pk.append(cfdist[ngram].freq(next_word))
        
        custm = stats.rv_discrete(values=(xk, pk))
        return candidates[custm.rvs()]
    
    def generateText(self, n, nb_sents=None, nb_words=None):
        """
        """
        if n < 1:
            raise ValueError("n must be higher or equal than 1.")
        if nb_sents is None and nb_words is None:
            raise ValueError("nb_sents or nb_words must be set.")
        
        # None is set as the end of a sentence
        tok_sents = [word_tokenize(sentence, language='french')+[None] for sentence in self.sentences]
        words = []
        for tok_sent in tok_sents:
            words += tok_sent
        # Extract [0-n]-grams
        all_igrams = {i:ngrams(words, i) for i in range(1, n+1)}
        # Compute conditional frequency distribution for each i-gram
        ngrams_cfd = {i:ConditionalFreqDist((igram[:-1], igram[-1]) for igram in igrams) for i, igrams in all_igrams.items()}
        
        i = 1
        frame = ()
        gen_tokens = []
        nb_sents_gen = 0
        nb_gen_words = 0
        while True:
            new_word = self._selectNextWord(frame, ngrams_cfd[i])
            if new_word is None:
                nb_sents_gen += 1
                if nb_sents is not None and nb_sents_gen == nb_sents:
                    break
                frame = ()
                i = 1
                continue
            frame += (new_word,)
            if i < n:
                i += 1
            elif i == n:
                frame = frame[1:]
            gen_tokens.append(new_word)
        return gen_tokens

if __name__ == '__main__':
    ngramModel = NgramModel('../data/bible_fr.txt')
    text = ngramModel.generateText(3, nb_sents=5)
    print(' '.join(text))
