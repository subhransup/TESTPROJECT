from food import Food
food_item1 = Food('Sandwich', 5,100)
food_item2 = Food('Chocolate Cake', 4,200)
food_item3 = Food('Coffee', 3,300)
food_item4 = Food('Orange Juice', 2,400)

food_items = [food_item1, food_item2, food_item3, food_item4]

index = 0
for food_item in food_items:
	print(str(index) + '. ' + food_item.info())
	index += 1

print('--------------------')

order = int(input('Enter food item number: '))
selected_food_item = food_items[order]
print('Selected item: ' + selected_food_item.name)

count = int(input('Enter quantity (10% off for 3 or more): '))
result = selected_food_item.get_total_price(count)
print('Your total is $' + str(result))
