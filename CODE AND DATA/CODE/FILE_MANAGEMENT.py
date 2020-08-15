import json
import codecs
import pandas as pd
import csv

def retrieve_keys_from_file(path_of_key_list_json):
    categories =list()
    with open(path_of_key_list_json,"r") as cat_file:
        categories = cat_file.readlines()

    for i in range(len(categories)):
        cat_name = json.loads(categories[i])["category"]
        categories[i] = cat_name
    return categories

def recover_dict_list_values_from_files_in_dir(dir_of_split_category_files, list_of_category_names):
    try:
        iter(list_of_category_names)
    except TypeError as e:
        print(e.with_traceback)
        return None
    
    this_dict = dict()
    for category in list_of_category_names:
        with codecs.open(dir_of_split_category_files+category+".txt","r",'utf-8') as cat_specific_file:
            print(category)
            this_dict[category] = cat_specific_file.readlines()
    return this_dict

def recover_csv_to_pd_dataframe(file_path_csv):
    df = pd.read_csv(file_path_csv)
    return df

"""def recover_list_from_unsorted_json_file(file_path):
    with open(file_path,"r") as Original_Dataset:
        elements = Original_Dataset.readlines()
    return elements
"""
def save_dict_category_keys_to_json_file(this_dict, path_of_key_list_json):
    assert isinstance(this_dict, dict)
    for category_name in this_dict.keys():
        cat_list  = this_dict[category_name]

        with codecs.open(path_of_key_list_json,"a",'utf-8') as cat_file:
            #print(this_dict.keys[i])
            obj = {
                "category": category_name,
            }
            json_out = json.dumps(obj)
            cat_file.writelines(json_out+"\n")



def save_dict_lines_to_separate_txt_files(this_dict, directory):
    assert isinstance(this_dict, dict)
    for category_name in this_dict.keys():
        cat_list  = this_dict[category_name]
            
            
        for lines in cat_list:
            with codecs.open(directory+category_name+".txt","a",'utf-8') as cat_file:
                if "\n" not in lines:
                    lines+="\n"
                cat_file.writelines(lines)


def save_dict_as_csv(this_dict,path_of_file_csv, is_vocab=False):
    assert isinstance(this_dict,dict)
    if not is_vocab:
        with codecs.open(path_of_file_csv,'w', "utf-8") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(["line","category_name","category_id"])
            i =-1
            for category in this_dict.keys():
                i+=1
                for line in this_dict[category]:
                    row = [line,category,i]
                    csvwriter.writerow(row)
    else:
        with codecs.open(path_of_file_csv,"w","utf-8") as csvfile:
            csvwriter =csv.writer(csvfile)
            csvwriter.writerow(["word","count","id"])
            csvwriter.writerow(["<unseen_token>",0,0])
            i = len(this_dict.keys())+1
            for word in this_dict.keys():
                print(word)
                i-=1
                row = [word,this_dict[word],i]
                csvwriter.writerow(row)


