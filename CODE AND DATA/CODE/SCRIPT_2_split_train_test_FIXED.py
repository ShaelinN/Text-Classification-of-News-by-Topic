###split train test
from FILE_MANAGEMENT import retrieve_keys_from_file, recover_dict_list_values_from_files_in_dir

lemma_full_dict = recover_dict_list_values_from_files_in_dir(
    "DATA\SIMPLIFIED/LEMMATIZED_FIXED/",
    retrieve_keys_from_file("DATA\list_of_categories.json")
    )


from SPLIT import TRAIN_TEST_SPLIT as tts
from FILE_MANAGEMENT import save_dict_as_csv

# USE ORIGINAL SOURCE SIZE FOR EACH CATEGORY
    #USING EQUAL PROPORTIONS OF SAMPLES PER CATEGORY

# this script only produces a dataset to be used on the most accurate lemmatized model with the flawed lemmatizer. 
# this means that 60:40 and 70:30 splits are irrelevant
#80-20 is the only split made
ep_dict = tts.split_dict(lemma_full_dict,equalize_proportion_per_category=True,equalize_source_size_per_category=False, train_fraction=0.8)
save_dict_as_csv(ep_dict["TRAIN"],"DATA\TRAIN_TEST\TEXTUAL/equal_lemma_fixed_TRAIN_80.csv")
save_dict_as_csv(ep_dict["TEST"], "DATA\TRAIN_TEST\TEXTUAL/equal_lemma_fixed_TEST_20.csv")
