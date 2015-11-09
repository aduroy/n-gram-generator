'''
Created on 7 nov. 2015

@author: Antonin Duroy
'''

import codecs
import numpy as np

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import ConditionalFreqDist
from nltk.util import ngrams
from scipy import stats

from utils import get_none_tuple, get_none_list
from realizer import Realizer

class NgramModel:
    
    def __init__(self, filepath, lang='english'):
        self.text = self._load_file(filepath)
        self.lang = lang
        self.sentences = sent_tokenize(self.text, language=self.lang)
    
    def _load_file(self, filepath):
        with codecs.open(filepath, 'r', encoding='utf-8') as f:
            return f.read().replace('\n', ' ')
    
    def _select_nextword(self, ngram, cfdist=None):
        """
        """
        xk = np.arange(cfdist[ngram].B())
        pk = []
        candidates = []
        for next_word in cfdist[ngram]:
            candidates.append(next_word)
            pk.append(cfdist[ngram].freq(next_word))
        
        custm = stats.rv_discrete(values=(xk, pk))
        return candidates[custm.rvs()]
    
    def gen_text(self, n, nb_sents=None, nb_words=None):
        """
        """
        if n < 1:
            raise ValueError("n must be higher or equal than 1.")
        if nb_sents is None and nb_words is None:
            raise ValueError("nb_sents or nb_words must be set.")
        
        tok_sents = [get_none_list(n-1)+word_tokenize(sentence, language=self.lang) for sentence in self.sentences]
        words = []
        for tok_sent in tok_sents:
            words += tok_sent
        words += [None] # None is set as the end of a sentence
        
        # Compute conditional frequency distribution for each n-gram
        ngrams_ = ngrams(words, n)
        ngrams_cfd = ConditionalFreqDist((ngram[:-1], ngram[-1]) for ngram in ngrams_)
        
        frame = get_none_tuple(n-1)
        gen_tokens = []
        nb_sents_gen = 0
        while True:
            new_word = self._select_nextword(frame, ngrams_cfd)
            
            if new_word is None:
                nb_sents_gen += 1
                if nb_sents is not None and nb_sents_gen == nb_sents:
                    break
                frame = get_none_tuple(n-1)
                continue
            
            frame += (new_word,)
            frame = frame[1:]
            gen_tokens.append(new_word)
        
        realizer = Realizer(lang=self.lang)
        return realizer.realize(gen_tokens)

if __name__ == '__main__':
    ngramModel = NgramModel('../data/bible_fr.txt', lang='french')
    text = ngramModel.gen_text(4, nb_sents=3)
    print(text)