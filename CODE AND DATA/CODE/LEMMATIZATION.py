import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import wordnet

def __get_wordnet_pos__(treebank_tag):
    """
    https://stackoverflow.com/questions/15586721/wordnet-lemmatization-and-pos-tagging-in-python

    answered Mar 23 '13 at 18:15
    by
    Suzana
    """

    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN


lemmatizer = WordNetLemmatizer()
def lemmatize_string(this_string):
    assert isinstance(this_string,str)
    this_string = this_string.lower()
    words = word_tokenize(this_string)
    #print(words)

    tagged_words = nltk.pos_tag(words)
    #print(tagged_words)
    
    out = ""
    for tag_word_pair in tagged_words:
        this_lemma = lemmatizer.lemmatize(tag_word_pair[0], pos=__get_wordnet_pos__(tag_word_pair[1]))
        out += this_lemma
        out += " "
    #print(out)
    out = out.strip()
    return out


def lemmatize_list(list_of_str):
    lem_list = list()
    for item in list_of_str:
        assert isinstance(item, str)
        lem_list.append(__lemmatize_string__(item))

    return lem_list