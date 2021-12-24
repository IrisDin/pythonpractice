## Problem 1

You are running a bakery, and need to buy two ingredients. You can only visit one store, so your job is to determine which of several stores will result in the __lowest total cost for purchasing the two ingredients__. Write a function least_exp_store(ingred_price_dict, ingred1, ingred2), where ingred_price_dict is a dictionary, where each key is an ingredient name (String) and each corresponding value is a list of prices for that ingredient at several stores. You may assume that ingred1 and ingred2 are not identical and are valid keys into ingred_price_dict. You can assume that each key maps to a list with at least one price and all values are lists of the same length. All costs will be integers greater than zero.


For example, when ingred_price_dict =
        {"Flour": [1, 2, 3], "Sugar": [20, 19, 24],
         "Butter": [2, 3, 4], "Molasses": [6, 7, 5]}


The prices for Flour are: 1 at store 0, 2 at store 1, and 3 at store 2.

The prices for Sugar are: 20 at store 0, 19 at store 1, and 24 at store 2.

The prices for Butter are: 2 at store 0, 3 at store 1, and 4 at store 2.

The prices for Molasses are: 6 at store 0, 7 at store 1, and 5 at store 2.

least_exp_store should return a list of the form: ["Store X", total_cost] where X is the index of the store with the lowest cost, and total_cost is the total cost for buying both ingredients at that store. If there is a tie in lowest price between several stores, select the store with the highest index. For example:


least_exp_store(ingred_price_dict, "Butter", "Molasses") should return ["Store 0", 8] because the total cost at Store 0 is 2 + 6 = 8, at Store 1 is 3 + 7 = 10, and at Store 2 is 4 + 5 = 9.


least_exp_store(ingred_price_dict, "Flour", "Sugar") should return ["Store 1", 21] because the total cost at Store 0 is 1 + 20 = 21, at Store 1 is 2 + 19 = 21, and at Store 2 is 3 + 24 = 27, and Store 1 has a higher store number than Store 0  (i.e. 1 > 0).

## Problem 2:

Write a function __customer_loyalty(visit_tracker)__ where visit_tracker is a dictionary mapping the name of each person to a list of the bubble tea places they have visited. There may be duplicates in the lists - indicating the customer has visited that location multiple times. customer_loyalty should return a dictionary which maps each store to a set of its loyal customers. A loyal customer is defined as a person who visited that store at least 3 times and did not visit more than one other store. A person may be considered a loyal customer to multiple stores. If a store has no loyal customers, it should not be included in the result dictionary.


__For example, when visit_tracker1 =
{"Evan": ["Ding Tea", "Ding Tea", "Yi Fang", "Ding Tea", "Ding Tea"],
"Izzy": ["Boba Up", "Ding Tea", "Boba Up", "Boba Up", "Ding Tea", "Ding Tea", "Ding Tea"]}__


__customer_loyalty(visit_tracker1) should return  
{"Boba Up": {"Izzy"}, "Ding Tea": {"Evan", "Izzy"}} because Izzy visited both "Boba Up" and "Ding Tea" three times, and did not visit any other locations. Evan visited "Ding Tea" four times and only visited one other location.__


__When visit_tracker2 =
{"Jackie": ["DIY Tea", "DIY Tea", "DIY Tea"],
"Evan": ["Yum Tea", "Ding Tea", "Yi Fang", "Yum Tea", "Yum Tea"]}__


customer_loyalty(visit_tracker2) should return  {"DIY Tea": {"Jackie"}} because Jackie visited both "DIY Tea" three times, and did not visit any other locations. Evan visited "Yum Tea" three times, but visited a total of three different locations.

## Problem 3:

You are a dedicated player of the game League of Legends. You would like to know which champions (characters) you never win with.


Let __match_tuples__ be a list of tuples. Each tuple in match_tuples contains two elements, and represents a match you played. The first element in each tuple is a string of the name of the champion you played as in that match. The second element is a boolean, where True means you won that match and False means you lost that match.


Create a function called never_win(match_tuples) that returns a list of strings with all of the unique champions that have zero matches won in match_tuples.  The list should be sorted in ascending alphabetical order. The strings are case sensitive: ‘AA’ is a different champion than ‘aa’.


For example,


never_win([("Ezreal", False), ("Yasuo", False), ("Teemo", False), ("Jinx", True), ("Ezreal", True), ("Teemo", False)])


Should return __["Teemo", "Yasuo"]__, since no matches were won by "Teemo" and "Yasuo". Although "Ezreal" lost one match, they also won a match, so are not included.


Assume that match_tuples is not empty. Return an empty list if there are no champions with zero wins.
