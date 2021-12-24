# Problem 1
def least_exp_store(ingred_price_dict, ingred1, ingred2):
    '''
    Arguments:
        ingred_price_dict: a dict of price_lists
        ingred1, ingred2: 2 strings representing ingredients

    Returns:
        A list containing two elements: a string representing the least
        expensive store to purchase ingred1 and ingred2 at, and the total cost
        of the two ingredients at that store. If there is a tie for lowest
        cost, returns the store with the higher index.
    '''
    # creating new lists and variables
    ingred_1 = ingred_price_dict[ingred1]
    ingred_2 = ingred_price_dict[ingred2]
    new_lst = []
    index = []
    result = []
    # storing the added value of two stores
    for i in range(len(ingred_1)):
        new_lst.append(ingred_1[i] + ingred_2[i])
    # comparing the number until we find the minium
    for i in range(len(ingred_1)):
        if ingred_1[i] + ingred_2[i] == min(new_lst):
            index.append(i)
    # sorting the index order by using list slice
    store_variable = 'Store ' + str(index[-1])
    least_price = min(new_lst)
    result.append(store_variable)
    result.append(least_price)
    return result


def test_least_exp_store():
    ingred_price_dict = {"Flour": [1, 2, 3], "Sugar": [20, 19, 24],
                         "Butter": [2, 3, 4], "Molasses": [6, 7, 5]}

    assert least_exp_store(ingred_price_dict,
                           "Butter", "Molasses") == ["Store 0", 8]
    assert least_exp_store(ingred_price_dict,
                           "Flour", "Sugar") == ["Store 1", 21]
    assert least_exp_store(ingred_price_dict,
                           "Butter", "Sugar") == ["Store 1", 22]
    assert least_exp_store(ingred_price_dict,
                           "Flour", "Butter") == ["Store 0", 3]

    ingred_price_dict2 = {"Flour": [10], "Sugar": [30]}

    assert least_exp_store(ingred_price_dict2,
                           "Flour", "Sugar") == ["Store 0", 40]

    ingred_price_dict3 = {"Flour": [10, 10, 10], "Sugar": [2, 1, 2],
                          "Butter": [10, 10, 10], "Molasses": [16, 2, 4]}

    assert least_exp_store(ingred_price_dict3,
                           "Butter", "Molasses") == ["Store 1", 12]
    assert least_exp_store(ingred_price_dict3,
                           "Flour", "Sugar") == ["Store 1", 11]
    assert least_exp_store(ingred_price_dict3,
                           "Butter", "Sugar") == ["Store 1", 11]
    assert least_exp_store(ingred_price_dict3,
                           "Flour", "Butter") == ["Store 2", 20]
    # print("test_least_exp_store passed.")


# Problem 2
def customer_loyalty(visit_tracker):
    '''
    Arguments:
        visit_tracker: a dictionary mapping customer names to a list of
        their visits to bubble tea stores

    Returns:
        a dictionary mapping stores to a set of their loyal customers.
        If a store does not have any loyal customers, it is not
        included in the returned dictionary. If the visit_tracker is empty
        or if there are no loyal customers, return an empty dictionary.
    '''
    # the purpose is to store the value
    cus_loy = {}
    # traversing the variables in the dictionary
    for (people, tea_stores) in visit_tracker.items():
        # loyal customer can not visit more than two stores
        if len(set(tea_stores)) <= 2:
            # finding the number of times the customer visted the store
            value_dic = {}
            for diff__tea_store in tea_stores:
                value = value_dic.get(diff__tea_store, 0)
                value_dic[diff__tea_store] = value + 1
            for store, value in value_dic.items():
                # visit the store >=3 defined as the loyal customer
                if value >= 3:
                    cus_loy[store] = cus_loy.get(store, set())
                    cus_loy[store].add(people)
    return cus_loy


def test_customer_loyalty():
    visit_tracker1 = {"Evan": ["Ding Tea", "Ding Tea", "Yi Fang",
                               "Ding Tea", "Ding Tea"],
                      "Izzy": ["Boba Up", "Ding Tea", "Boba Up",
                               "Boba Up", "Ding Tea", "Ding Tea", "Ding Tea"]}

    assert customer_loyalty(visit_tracker1) == {"Boba Up": {"Izzy"},
                                                "Ding Tea": {"Evan", "Izzy"}}

    visit_tracker2 = {"Jackie": ["DIY Tea", "DIY Tea", "DIY Tea"],
                      "Evan": ["Yum Tea", "Ding Tea",
                               "Yi Fang", "Yum Tea", "Yum Tea"]}

    assert customer_loyalty(visit_tracker2) == {"DIY Tea": {"Jackie"}}

    visit_tracker3 = {"Jackie": ["DIY Tea", "DIY Tea", "DIY Tea"],
                      "Evan": ["Yum Tea", "Ding Tea",
                               "Yum Tea", "Yum Tea"]}

    assert customer_loyalty(visit_tracker3) == {"DIY Tea": {"Jackie"},
                                                "Yum Tea": {"Evan"}}

    visit_tracker4 = {"Iris": ["A", "A", "A", "B", "C"],
                      "DING": ["A", "A", "B",
                               "B", "B", "B", "C"]}
    assert customer_loyalty(visit_tracker4) == {}
    # print("test_customer_loyalty passed.")


# Problem 3
def never_win(match_tuples):
    '''
    Arguments:
        match_tuples: a list of tuples that are size 2 representing matches
        played. Each tuple is in the form (string, boolean), which represents
        the champion played for the match and whether the match was won
        (True for won, False for lost). Assume match_tuples is not empty.

    Returns: a list of the unique champions that have no matches won in
        match_tuples, sorted in alphabetical order. Returns an empty list if
        there are no champions with zero matches won.
    '''
    # creating the new win set and lose set of character
    win = set()
    lose = set()
    for tuple in match_tuples:
        # losing the game by using the character
        if tuple[1] is False:
            lose.add(tuple[0])
        # wining the game by using the character
        else:
            win.add(tuple[0])
        # return the sorted never_win charcter
        # sorted by alphabetical order
    return sorted(list(lose - win))


def test_never_win():
    win_list1 = [("Ezreal", False), ("Yasuo", False), ("Teemo", False),
                 ("Jinx", True), ("Ezreal", True), ("Teemo", False)]
    assert never_win(win_list1) == ["Teemo", "Yasuo"]
    assert never_win([('Ezreal', True), ('Yasuo', True),
                      ('Jinx', False), ('Jinx', True)]) == []
    win_list2 = [("Ezreal", False), ("Yasuo", False), ("Teemo", False)]
    assert never_win(win_list2) == ["Ezreal", "Teemo", "Yasuo"]

    win_list3 = [("C", True), ("B", False), ("C", False), ("C", False)]
    assert never_win(win_list3) == ["B"]
    # print("test_never_win passed.")


def main():
    test_least_exp_store()
    test_customer_loyalty()
    test_never_win()
    # print("All test passed.")


if __name__ == "__main__":
    main()