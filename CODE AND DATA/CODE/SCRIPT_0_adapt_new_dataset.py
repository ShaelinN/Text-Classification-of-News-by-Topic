#this script formats the original data to the format needed by later modules
# each record for a category is a sentence from the articles

file_structure = [
    ("business",510),
    ("entertainment",386),
    ("politics",417),
    ("sport",511),
    ("tech",401),
]

sent_dict = dict()
from nltk.tokenize import sent_tokenize
for category in file_structure:
    directory="DATA/ORIGINAL/"+category[0]+"/"
    sent_dict[category[0]] = list()

    for i in range(category[1]):
        filepath = directory+'{:03d}'.format(i+1)+".txt"

        new_lines = list()
        with open(filepath) as current_file:
            new_lines = current_file.readlines()

        sentences = list()
        for line in new_lines:
            new_sents = sent_tokenize(line)
            sentences+=new_sents

        sent_dict[category[0]]+= sentences



from FILE_MANAGEMENT import save_dict_category_keys_to_json_file,save_dict_as_csv, save_dict_lines_to_separate_txt_files

save_dict_category_keys_to_json_file(sent_dict,"DATA/list_of_categories.json")
save_dict_lines_to_separate_txt_files(sent_dict,"DATA/ADAPTED/")