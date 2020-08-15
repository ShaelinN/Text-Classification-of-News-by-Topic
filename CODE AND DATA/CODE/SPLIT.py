use_shortest_len = dict()
import math,random
class TRAIN_TEST_SPLIT:

    @staticmethod
    def split_single_list(unsplit_list, train_fraction=0.7):
        print("splitting train and test data from list")
        print(unsplit_list.__class__.__name__)
        assert isinstance(unsplit_list,list)

        random.shuffle(unsplit_list)
        max_index = len(unsplit_list)
        train_test_border_index = math.ceil(train_fraction*max_index)

        train_list = unsplit_list[0:train_test_border_index]
        test_list   = unsplit_list[train_test_border_index:max_index]

        return train_list, test_list


    @staticmethod
    def equalize_count_per_class(unsplit_dict_of_lists, dict_of_indvidual_lengths =use_shortest_len):
        #dict of individual lengths is to allow manual assignment of sample numbers. 
        # this may be necessary if a category is too broad even with equal samples
        if not dict_of_indvidual_lengths== use_shortest_len:
            assert isinstance(dict_of_indvidual_lengths, dict)
            assert isinstance(unsplit_dict_of_lists, dict)
            for category in dict_of_indvidual_lengths:
                assert cat in unsplit_dict_of_lists.keys()
                assert isinstance(dict_of_indvidual_lengths[category], int)
                assert len(unsplit_dict_of_lists[category])<= dict_of_indvidual_lengths[category]

        else:#CUT ALL DOWN TO THE SHORTEST LENGTH
            shortest_len = 0
            for category in unsplit_dict_of_lists:
                if len(unsplit_dict_of_lists[category])<shortest_len or shortest_len == 0:
                    shortest_len = len(unsplit_dict_of_lists[category])
            
            for category in unsplit_dict_of_lists:
                dict_of_indvidual_lengths[category] = shortest_len

        ###SHUFFLE THE LISTS SO THAT PICKING THE EARLIEST SUBSET IS STILL RANDOM 
        for category in unsplit_dict_of_lists:
            random.shuffle(unsplit_dict_of_lists[category])

        equalised_dict = dict()
        for category in unsplit_dict_of_lists:
            current_list = unsplit_dict_of_lists[category]
            current_max_index = dict_of_indvidual_lengths[category]
            current_list = current_list[:current_max_index+1]
            equalised_dict[category] = current_list

        return equalised_dict

#BROKEN METHOD: DO NOT CALL
    @staticmethod
    def split_dict_disproportionately(unsplit_dict_of_lists, train_fraction = 0.7):
        test = dict(   (category, list()) for category in unsplit_dict_of_lists.keys())

        tot_len = 0
        assert isinstance(unsplit_dict_of_lists,dict)
        for category in unsplit_dict_of_lists:
            random.shuffle(unsplit_dict_of_lists[category])
            tot_len+=len(unsplit_dict_of_lists[category])

        tot_test = math.ceil((1-train_fraction)*tot_len)

        current_test  = 0
        avail_categories = list(unsplit_dict_of_lists.keys())

        while current_test < tot_test:
            current_category = random.choice(avail_categories)
            print(current_category)
            print("before checking empty, len=", end=" ")
            print(len(unsplit_dict_of_lists[current_category]))
            
            cur_list = unsplit_dict_of_lists[current_category]
            if len(cur_list)>0:
                print("list not empty. len=",end=" ")
                print(len(cur_list))
                current_line = cur_list.pop()   ##popping removes the element form the list
                
                print("list popped NEW len=",end=" ")
                print(len(cur_list))
                unsplit_dict_of_lists[category] = cur_list
                (test[category]).append(current_line)
                current_test +=1
            else:
                print("EMPTY")
                avail_categories.remove(current_category)


        #since testing data was popped off already
        train = unsplit_dict_of_lists  

        return train,test


    @staticmethod
    def split_dict_proportionately(unsplit_dict_of_lists, train_fraction = 0.7):
        assert isinstance(unsplit_dict_of_lists,dict)
        train = dict()
        test = dict()
        for category in unsplit_dict_of_lists:
            curr_train_test = TRAIN_TEST_SPLIT.split_single_list(unsplit_dict_of_lists[category],train_fraction)
            train[category] = curr_train_test[0]
            test[category] =  curr_train_test[1]

        return train, test


    @staticmethod
    def split_dict(unsplit_dict_of_lists, train_fraction = 0.7, equalize_source_size_per_category = False, equalizing_counts_dict=use_shortest_len, equalize_proportion_per_category=True):
        #
        assert isinstance(unsplit_dict_of_lists, dict)
        operational = unsplit_dict_of_lists

        if equalize_source_size_per_category:
            operational = TRAIN_TEST_SPLIT.equalize_count_per_class(operational,equalizing_counts_dict)

        #train, test = dict()

        if equalize_proportion_per_category:
            train,test = TRAIN_TEST_SPLIT.split_dict_proportionately(operational, train_fraction)
        else:
            train,test = TRAIN_TEST_SPLIT.split_dict_disproportionately(operational , train_fraction)

        return {"TRAIN":train,"TEST":test}