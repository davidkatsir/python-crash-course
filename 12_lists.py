#                       -5     -4    -3   -2   -1  <== Indexes from end
#          0    1        2      3     4    5    6   <== Members indexes
my_list = [1, True, [3, 4, 10], 5, "Alex", 7, "Alex"]
print(my_list.index(5))  # Output: 3 ⇐ Return index of member who is 5
print(my_list)  # Output: [1, True, [3, 4, 10], 5, 'Alex', 7, 'Alex']
print(my_list[1])  # Output: True
print(my_list[0:4])  # Output: [1, True, [3, 4, 10], 5]
print(my_list[0:5])  # Output: [1, True, [3, 4, 10], 5, 'Alex']
print(my_list[0:5:2])  # Output: [1, [3, 4, 10], 'Alex'] ⇐ Same as the one before but in steps of 2
print(
    my_list[-4:-1])  # Output: [5, 'Alex', 7] ⇐ Slice the list and return a sublist from index -4 till -1 not inclusive
print(my_list[-4:])  # Output: [5, 'Alex', 7, 'Alex'] ⇐ From -4 till the end
print(my_list[::-1])  # Output: ['Alex', 7, 'Alex', 5, [3, 4, 10], True, 1]   ⇐ Returns the whole list in reverse
print(my_list[2][2])  # Output: 10

# my_list = [10, 5, 4, 1, 1000]
print(my_list)  # Output: [1, True, [3, 4, 10], 5, 'Alex', 7, 'Alex']
print(my_list.pop())  # Output: Alex <== Removes the last member of the list and returns it
print(my_list)  # Output: [1, True, [3, 4, 10], 5, 'Alex', 7]
print(
    my_list.pop(2))  # Output: [3, 4, 10] <== Removes the member in index 2 of the list and returns the list without it
print(my_list)  # Output: [1, True, 5, 'Alex', 7]
print(my_list.count("Alex"))  # Output: 1
print(my_list)
my_list.append("Komanov")
print(my_list)  # Output: [1, True, 5, 'Alex', 7, 'Komanov']
my_list += 53, 53
print(my_list)  # Output: [1, True, 5, 'Alex', 7, 'Komanov', 53, 53]
my_list.reverse()
print(my_list)  # Output: [53, 53, 'Komanov', 7, 'Alex', 5, True, 1]

my_list = [10, 5, 4, 1, 1000]
my_list.sort()
print(my_list)  # Output: [1, 4, 5, 10, 1000]
my_list.sort(reverse=True)
print(my_list)  # Output: [1000, 10, 5, 4, 1]
