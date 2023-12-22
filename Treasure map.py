row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

#I split

# coord=list(position)
# coord[0]=int(coord[0])-1
# coord[1] = int(coord[1])-1
# map[coord[1]][coord[0]]="x"

horizontal = int(position[1]) - 1
vertical = int(position[0]) - 1
map[horizontal][vertical] = "X"


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")