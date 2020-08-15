from FILE_MANAGEMENT import recover_csv_to_pd_dataframe

import pandas as pd

from nltk.tokenize import word_tokenize
def encode_train_and_test(vocab, train_source,test_source,train_dest,test_dest):
    vocab_df = recover_csv_to_pd_dataframe(vocab)
    #convert vocab to a dict
    vocab_dict = dict()
    for i in range(len(vocab_df.word)):
        vocab_dict[vocab_df.word[i]] = vocab_df.id[i]
        #print(id)


    #TRAIN
    train_df = recover_csv_to_pd_dataframe(train_source)
    encoded_train_df = pd.DataFrame(columns=('line','category_id'))

    for i in range(len(train_df.line)):
        #split str to list
        working_line = word_tokenize(train_df.line[i])
        encoded_line = list()

        #populate encoded list
        for word in working_line:
            str_word = str(word)
            if str_word=='nan':
                print("wtf")
            print(str_word)
            #bodged fix: if numeric (therefore represented as #) dont encode
            if word in vocab_dict.keys() and vocab_dict[str_word]==1:
                #print(str(word))
                a=1
                #encoded_line.append(0) 
            else:
                encoded_line.append(vocab_dict[str_word])

        #add new row for this line
        encoded_train_df.loc[i] = [encoded_line]+[ train_df.category_id[i]]
    #save csv
    encoded_train_df.to_csv(train_dest)


    #TEST
    test_df = recover_csv_to_pd_dataframe(test_source)
    encoded_test_df = pd.DataFrame(columns=('line', 'category_id'))

    for i in range(len(test_df.line)):
        #split str to list
        working_line = word_tokenize(test_df.line[i])
        encoded_line = list()

        #populate encoded list
        for word in working_line:

            #if not in vocab dont add to encoding
            #bodged fix: if numeric (therefore represented as #) dont encode
            if word not in vocab_dict.keys():
                print(str(word))
                #encoded_line.append(0) 
            elif vocab_dict[str(word)]==1:
                    print(str(word))
            else:
                encoded_line.append(vocab_dict[str(word)])

        #add new row for this line
        encoded_test_df.loc[i] = [encoded_line]+[test_df.category_id[i]]
    #save csv
    encoded_test_df.to_csv(test_dest)



#for lemmatized

encode_train_and_test(
    vocab="DATA\TRAIN_TEST\equal_lemma_VOCAB.csv",

    train_source="DATA\TRAIN_TEST\TEXTUAL\equal_lemma_TRAIN_70.csv",
    test_source="DATA\TRAIN_TEST\TEXTUAL\equal_lemma_TEST_30.csv",

    train_dest="DATA\TRAIN_TEST\ENCODED\equal_lemma_TRAIN_70.csv",
    test_dest="DATA\TRAIN_TEST\ENCODED\equal_lemma_TEST_30.csv",
    )

#for stemmed
encode_train_and_test(
    vocab="DATA\TRAIN_TEST\equal_stem_VOCAB.csv",

    train_source="DATA\TRAIN_TEST\TEXTUAL\equal_stem_TRAIN_70.csv",
    test_source="DATA\TRAIN_TEST\TEXTUAL\equal_stem_TEST_30.csv",

    train_dest="DATA\TRAIN_TEST\ENCODED\equal_stem_TRAIN_70.csv",
    test_dest="DATA\TRAIN_TEST\ENCODED\equal_stem_TEST_30.csv",
    )


