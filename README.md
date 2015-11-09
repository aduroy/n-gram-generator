# n-gram text generator
n-gram models are widely used in computational linguistics, such as text generation. In this field, an n-gram model
is a probabilistic model for predicting words given the previous ones, using Markov chains.
Here, `gram` means `word`, and grams are collected from a corpus of sentences.

## Requirements
- Python 3.4
- Scipy 0.16.0
- Numpy 1.10.0
- NLTK 3.0.5

## Under the hood

- Text is tokenized into words
- Markov model is trained using sequences of `n` words
- Conditional probability of each word is set, given the `n-1` previous words
- Iteration is made in order to generate words given the previous ones and their relative probabilities

Credits: [NLTK](http://www.nltk.org/ "NLTK")

## Code samples
