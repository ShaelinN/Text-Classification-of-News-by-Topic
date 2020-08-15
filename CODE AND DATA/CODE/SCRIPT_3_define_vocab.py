#DEFINE VOCAB based on training data
from FILE_MANAGEMENT import recover_csv_to_pd_dataframe
import pandas as pd

def create_vocab(file_train_source,file_destination):
    train_df = recover_csv_to_pd_dataframe(file_train_source)

    from nltk.tokenize import word_tokenize
    voc_dict = dict()

    for line in train_df["line"]:
        word_tok = word_tokenize(line)
        for word in word_tok:
            if word not in voc_dict.keys():
                voc_dict[word] = 1
            else:
                voc_dict[word] +=1
    ##full vocab by counts built
    ##sort by count
    sorted_dict = {k: v for k, v in sorted(voc_dict.items(), key=lambda item: item[1])}


    from FILE_MANAGEMENT import save_dict_as_csv
    save_dict_as_csv(sorted_dict,file_destination,is_vocab=True)


create_vocab(
    "DATA/TRAIN_TEST/TEXTUAL/equal_lemma_TRAIN_70.csv",
    "DATA/TRAIN_TEST/equal_lemma_VOCAB.csv",
    )

create_vocab(
    "DATA/TRAIN_TEST/TEXTUAL/equal_stem_TRAIN_70.csv",
    "DATA/TRAIN_TEST/equal_stem_VOCAB.csv",
    )
