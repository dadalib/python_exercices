my_list = [1, 3.5, "TEST"]
my_list.append(4)
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
my_list.insert(1, "inserted")
print(my_list)
del my_list[0]
print(my_list)
my_list.remove("inserted")

def loop_list(lst):
    for item in lst:
        print(item)

def second_loop_list(lst):
    item = 0 
    while item < len(lst):
        print(lst[item])
        item += 1
print ("Looping through the list:")
loop_list(my_list)
second_loop_list(my_list)
def use_enumerate(lst):
    for index, item in enumerate(lst):
        print(f"Index: {index}, Item: {item}")
print("Enumerate")
use_enumerate(my_list)
