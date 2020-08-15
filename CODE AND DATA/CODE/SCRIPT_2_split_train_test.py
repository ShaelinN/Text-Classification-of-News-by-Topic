###split train test
from FILE_MANAGEMENT import retrieve_keys_from_file, recover_dict_list_values_from_files_in_dir

lemma_full_dict = recover_dict_list_values_from_files_in_dir(
    "DATA\SIMPLIFIED/LEMMATIZED/",
    retrieve_keys_from_file("DATA\list_of_categories.json")
    )

stem_full_dict = recover_dict_list_values_from_files_in_dir(
    "DATA\SIMPLIFIED/STEMMED/",
    retrieve_keys_from_file("DATA\list_of_categories.json")
    )



from SPLIT import TRAIN_TEST_SPLIT as tts
from FILE_MANAGEMENT import save_dict_as_csv

# USE ORIGINAL SOURCE SIZE FOR EACH CATEGORY
    #USING EQUAL PROPORTIONS OF SAMPLES PER CATEGORY
    #60-40
ep_dict = tts.split_dict(lemma_full_dict,equalize_proportion_per_category=True,equalize_source_size_per_category=False, train_fraction=0.6)
save_dict_as_csv(ep_dict["TRAIN"],"DATA\TRAIN_TEST\TEXTUAL/equal_lemma_TRAIN_60.csv")
save_dict_as_csv(ep_dict["TEST"], "DATA\TRAIN_TEST\TEXTUAL/equal_lemma_TEST_40.csv")

ep_dict = tts.split_dict(stem_full_dict,equalize_proportion_per_category=True,equalize_source_size_per_category=False,train_fraction=0.6)
save_dict_as_csv(ep_dict["TRAIN"],"DATA\TRAIN_TEST\TEXTUAL/equal_stem_TRAIN_60.csv")
save_dict_as_csv(ep_dict["TEST"], "DATA\TRAIN_TEST\TEXTUAL/equal_stem_TEST_40.csv")

   #70-30
ep_dict = tts.split_dict(lemma_full_dict,equalize_proportion_per_category=True,equalize_source_size_per_category=False, train_fraction=0.7)
save_dict_as_csv(ep_dict["TRAIN"],"DATA\TRAIN_TEST\TEXTUAL/equal_lemma_TRAIN_70.csv")
save_dict_as_csv(ep_dict["TEST"], "DATA\TRAIN_TEST\TEXTUAL/equal_lemma_TEST_30.csv")

ep_dict = tts.split_dict(stem_full_dict,equalize_proportion_per_category=True,equalize_source_size_per_category=False,train_fraction=0.7)
save_dict_as_csv(ep_dict["TRAIN"],"DATA\TRAIN_TEST\TEXTUAL/equal_stem_TRAIN_70.csv")
save_dict_as_csv(ep_dict["TEST"], "DATA\TRAIN_TEST\TEXTUAL/equal_stem_TEST_30.csv")

    #80-20
ep_dict = tts.split_dict(lemma_full_dict,equalize_proportion_per_category=True,equalize_source_size_per_category=False, train_fraction=0.8)
save_dict_as_csv(ep_dict["TRAIN"],"DATA\TRAIN_TEST\TEXTUAL/equal_lemma_TRAIN_80.csv")
save_dict_as_csv(ep_dict["TEST"], "DATA\TRAIN_TEST\TEXTUAL/equal_lemma_TEST_20.csv")

ep_dict = tts.split_dict(stem_full_dict,equalize_proportion_per_category=True,equalize_source_size_per_category=False,train_fraction=0.8)
save_dict_as_csv(ep_dict["TRAIN"],"DATA\TRAIN_TEST\TEXTUAL/equal_stem_TRAIN_80.csv")
save_dict_as_csv(ep_dict["TEST"], "DATA\TRAIN_TEST\TEXTUAL/equal_stem_TEST_20.csv")

#USING RANDOM PROPORTIONS OF SAMPLES PER CATEGORY
#DROPPED FROM PROJECT: RANDOM PROPORTION SPLIT FUNCTION IS BROKEN
"""
rp_dict = tts.split_dict(lemma_full_dict,equalize_proportion_per_category=False,equalize_source_size_per_category=False, train_fraction=0.6)
save_dict_as_csv(rp_dict["TRAIN"],"DATA\TRAIN_TEST\TEXTUAL/rand_lemma_TRAIN_70.csv")
save_dict_as_csv(rp_dict["TEST"], "DATA\TRAIN_TEST\TEXTUAL/rand_lemma_TEST_30.csv")

rp_dict = tts.split_dict(stem_full_dict,equalize_proportion_per_category=False,equalize_source_size_per_category=False, train_fraction=0.6)
save_dict_as_csv(rp_dict["TRAIN"],"DATA\TRAIN_TEST\TEXTUAL/rand_stem_TRAIN_70.csv")
save_dict_as_csv(rp_dict["TEST"], "DATA\TRAIN_TEST\TEXTUAL/rand_stem_TEST_30.csv")

rp_dict = tts.split_dict(lemma_full_dict,equalize_proportion_per_category=False,equalize_source_size_per_category=False, train_fraction=0.7)
save_dict_as_csv(rp_dict["TRAIN"],"DATA\TRAIN_TEST\TEXTUAL/rand_lemma_TRAIN_70.csv")
save_dict_as_csv(rp_dict["TEST"], "DATA\TRAIN_TEST\TEXTUAL/rand_lemma_TEST_30.csv")

rp_dict = tts.split_dict(stem_full_dict,equalize_proportion_per_category=False,equalize_source_size_per_category=False, train_fraction=0.7)
save_dict_as_csv(rp_dict["TRAIN"],"DATA\TRAIN_TEST\TEXTUAL/rand_stem_TRAIN_70.csv")
save_dict_as_csv(rp_dict["TEST"], "DATA\TRAIN_TEST\TEXTUAL/rand_stem_TEST_30.csv")

rp_dict = tts.split_dict(lemma_full_dict,equalize_proportion_per_category=False,equalize_source_size_per_category=False, train_fraction=0.8)
save_dict_as_csv(rp_dict["TRAIN"],"DATA\TRAIN_TEST\TEXTUAL/rand_lemma_TRAIN_70.csv")
save_dict_as_csv(rp_dict["TEST"], "DATA\TRAIN_TEST\TEXTUAL/rand_lemma_TEST_30.csv")

rp_dict = tts.split_dict(stem_full_dict,equalize_proportion_per_category=False,equalize_source_size_per_category=False, train_fraction=0.8)
save_dict_as_csv(rp_dict["TRAIN"],"DATA\TRAIN_TEST\TEXTUAL/rand_stem_TRAIN_70.csv")
save_dict_as_csv(rp_dict["TEST"], "DATA\TRAIN_TEST\TEXTUAL/rand_stem_TEST_30.csv")

"""