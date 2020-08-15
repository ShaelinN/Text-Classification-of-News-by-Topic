# drop stopwords
# stem or lemmatize
# drop_punctuation and numerics

from nltk.tokenize import word_tokenize

from nltk.corpus import stopwords
eng_stop_words = stopwords.words('english')

def replace_stopwords(string):
    word_list = word_tokenize(string)
    new =''
    for word in word_list:
        if word not in eng_stop_words:

            new+= word+' '
    return new


from nltk.stem import SnowballStemmer
stemmer = SnowballStemmer('english', ignore_stopwords=True)
def stem(string):
    word_list = word_tokenize(string)
    result=''
    for word in word_list:
        result+= stemmer.stem(word)+' '
    return result


from LEMMATIZATION import lemmatize_string
def lemmatize(string):
    return lemmatize_string(string)


def simplify(string, lemma_or_stem="stem"):
    string = string.lower()

    if lemma_or_stem == "lemma":
        #when lemmatizing replace stopwords after to allow successful POS tagging
        string = lemmatize(string)
        string = replace_stopwords(string)

    else:
        #when stemming replace stopwords first to increase speed
        string = replace_stopwords(string)
        string = stem(string)



    new = ""
    for char in string:
        if char.isalpha() or char==" ":
            new+=char

    new = new.strip()


    print(new)
    return new