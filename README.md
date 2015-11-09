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
- Conditional probabilities are set for each word, given the `n-1` previous words
- Generation is made iteratively given the previous words and their relative probabilities

Let `n=3` and `i` the index of the `ith` word `w`, its conditional probability is:
![n-gram representation](https://github.com/aduroy/NGramGenerator/blob/master/data/ngram_prob.png)

## Code samples

First, create an `NgramModel` instance by specifying the `path/to/your/dataset` and the language of your text, as follows:

        ngram_model = NgramModel('../data/bible_fr.txt', lang='french')

Then, set the frame size (`n`) and generate as many sentences as you wish:

        text1 = ngramModel.gen_text(2, nb_sents=3)
        text2 = ngramModel.gen_text(4, nb_sents=3)

Print them in console:

        print('== 2-gram ===')
        print(text1)
        print('== 4-gram ===')
        print(text2)

And get:

        == 2-gram ===
        Nous ne viendras, vous êtes sincères, que Sara mentit, Rebecca dans le pays d'égypte, son séjour des
        étrangers, premier-né de Béthel à ses frères de son du menu bétail, son père. Seulement, ils lui enfanta
        une tunique de Canaan ; et ainsi : Fais comme les sept jours des vivres. Et Laban.
        == 4-gram ===
        Ne crains point, car cet homme nous a dit : Vous me troublez, en me conservant la vie ; mais je ne puis
        rien faire jusqu'à ce que tu l'envoies ? C'est le champ qu'Abraham a acheté d'éphron, le Héthien, comme
        propriété sépulcrale, et qui me répondra : Bois, et je parlerai. Cham, père de Sichem, et sortirent.
