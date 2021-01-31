shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)

for item in shopping_list:
    if item == "spam":
        continue

    print("Buy " + item)
print("-------------------")

# break
for item in shopping_list:
    if item == "spam":
        break

    print("Buy " + item)
print("-------------------")

# searching
item_to_find = "spam"
found_at = None

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break
print("Item found at position {}".format(found_at))
