from FILE_MANAGEMENT import recover_dict_list_values_from_files_in_dir,retrieve_keys_from_file
######################
# LEMMATIZED VERSION
#####################
working_dict_lemma = recover_dict_list_values_from_files_in_dir(
    "DATA\ADAPTED/",
    retrieve_keys_from_file("DATA\list_of_categories.json")
    )

assert isinstance(working_dict_lemma, dict)

#PERFORM STEMMING BASED SIMPLIFICATION ON ALL SAMPLES
from PREPROCESSING import simplify
for category in working_dict_lemma: #for each category
    for i in range(len(working_dict_lemma[category])):#for each entry of that category
        working_dict_lemma[category][i] = simplify(working_dict_lemma[category][i], lemma_or_stem="lemma")

from FILE_MANAGEMENT import save_dict_lines_to_separate_txt_files
save_dict_lines_to_separate_txt_files(working_dict_lemma,'DATA/SIMPLIFIED/LEMMATIZED/')


###################
#STEMMED VERSION
###################
working_dict_stem = recover_dict_list_values_from_files_in_dir(
    "DATA\ADAPTED/",
    retrieve_keys_from_file("DATA\list_of_categories.json")
    )

assert isinstance(working_dict_stem, dict)

#PERFORM STEMMING BASED SIMPLIFICATION ON ALL SAMPLES
from PREPROCESSING import simplify
for category in working_dict_stem: #for each category
    for i in range(len(working_dict_stem[category])):#for each entry of that category
        working_dict_stem[category][i] = simplify(working_dict_stem[category][i], lemma_or_stem="stem")

from FILE_MANAGEMENT import save_dict_lines_to_separate_txt_files
save_dict_lines_to_separate_txt_files(working_dict_stem,'DATA/SIMPLIFIED/STEMMED/')




