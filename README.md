# n-gram Text Generator
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
- Conditional probabilities are set for each word, given the `n-1` previous words
- Generation is made iteratively given the previous words and their relative probabilities

e.g.:

Given `n=3`, let `i` denote the index of the `ith` word `w`, its conditional probability is:
![n-gram representation](https://github.com/aduroy/NGramGenerator/blob/master/data/ngram_prob.png)

## Code samples

First, create an `NgramModel` instance by specifying the `path/to/your/dataset` and the language of your text, as follows:
```python
ngram_model = NgramModel('../data/bible_fr.txt', lang='french')
```

Then, set the frame size (`n`) and generate as many sentences as you wish:
```python
text1 = ngramModel.gen_text(2, nb_sents=3)
text2 = ngramModel.gen_text(4, nb_sents=3)
```
Print them in console:
```python
print('=== 2-gram ===')
print(text1)
print('=== 4-gram ===')
print(text2)
```
And get:
```
=== 2-gram ===
Nous ne viendras, vous êtes sincères, que Sara mentit, Rebecca dans le pays d'égypte, son séjour des
étrangers, premier-né de Béthel à ses frères de son du menu bétail, son père. Seulement, ils lui enfanta
une tunique de Canaan ; et ainsi : Fais comme les sept jours des vivres. Et Laban.

=== 4-gram ===
Ne crains point, car cet homme nous a dit : Vous me troublez, en me conservant la vie ; mais je ne puis
rien faire jusqu'à ce que tu l'envoies ? C'est le champ qu'Abraham a acheté d'éphron, le Héthien, comme
propriété sépulcrale, et qui me répondra : Bois, et je parlerai. Cham, père de Sichem, et sortirent.
```
And, same for `english`
```python
ngram_model = NgramModel('../data/bible_en.txt', lang='english')
text1 = ngramModel.gen_text(2, nb_sents=3)
text2 = ngramModel.gen_text(4, nb_sents=3)
```
It produces
```
=== 2-gram ===
And Herod, and the dead because of the flesh, who love of the day, and said, high mountain, "If God,
"Truly, who bewailed and one Simon of the city Jerusalem, and on the chief priests and release him,
and understand all liars, but they rested according to the saints according to the law might be his God,
but by a great multitude of God is dry? Then Jesus from the imperfect; and on the chief priests and the
sufferings of the flesh can not receive the redemption of God. To set the first fruits of God, but we do
not arrogant or nakedness, I am a child; but the commandment.
=== 4-gram ===
Who shall separate us from the love of Christ? So then, brethren, we are debtors, not to the flesh, to
live according to the will of him who subjected it in hope; because the creation itself will be set free
from its bondage to decay and obtain the glorious liberty of the children of God, his Chosen One!" And he
answered him, "You have said so."
```
## Realization

The process of realizing text consists in rendering concepts or expressions into a syntactically well-formed sequence of characters. That being said, languages does not necessarily share common rules, that's why the `lang` parameter is important, for 2 reasons:

- Split the dataset into sentences and words
- Organize produced words

### Examples of differences between French and English

Semicolon
```
French
(...) word ; word (...)
English
(...) word; word (...)
```
Colon
```
French
(...) word : word (...)
English
(...) word: word (...)
```
Exclamation mark
```
French
(...) word !
English
(...) word!
```
Question mark
```
French
(...) word ?
English
(...) word?
```
And so forth...
