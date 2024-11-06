import random

# pick two recipes everytime running the codes
food_list = ["lasagne", "bolognese", "fajita", "tacos", "burritos", "salmon and mashed potatoes", "meatball soup",
             "swedish meatball with mashed potatoes", "gammon with roasted vegs", "tuna-mayo pasta",
             "marinated meat BBQ with chips", "fried chicken", "cottage/shepherds pie", "lamb mint with rice",
             "bacon + hakusai soup", "burger with chips", "potato dauphinoise", "bibimbap", "fish and chips",
             "paprikas csirke", "porkort with rice", "szekeykaposta", "pizza", "gulyas with krumplis pogacsa",
             "pork meatball soup", "onigiri", "california rolls", "korma curry with paratha", "laksa soup",
             "green curry with rice", "stir-fried jumbo king prawns", "japanese curry with rice", "duck with rice/mashed potato",
             "pork belly with rice", "ramen", "lecso - vegetable stew", "hamburgu with cheese toppings (like bikkuri-donky)"]

add_food = input("Do you want to add any meals into food_list? Y or N: ")
# if add_food == "Y":
#     food_list.append(add_food)
# else:
#     pass

suggested_meals = [random.sample(food_list, 2)]
print(suggested_meals)

for i in range(2):
    food_list.remove(suggested_meals[0][i])

print(food_list)
