line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇


# Write your code above this row 👆
val = position[0].lower()
abc = ["a", "b", "c"]
val_index = abc.index(val)
num_index = int(position[1]) - 1
map[num_index][val_index] = "X"
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
