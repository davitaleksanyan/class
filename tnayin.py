# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#number 1 bubble sort
def bubbleSort(list):
	n = len(list)
	for i in range(n):
		for j in range(0, n-i-1):
			if list[j] > list[j+1] :
				list[j], list[j+1] = list[j+1], list[j]

puchik = [-1, 100, 16, 2, 0]
puchik1 = [0, -5, 8, 2, 23]
bubbleSort(puchik)
print("Sorted list by Bubble sort method")
print(puchik)
puchik1.sort()
print("Sorted list by sort method")
print(puchik1)


# number2 Concatenate two lists index-wise.
list1 = ["M", "na", "i", "Ke", "0"]
list2 = ["y", "me", "s", "lly"]
list3 = []

def sum_of_list(list1=[], list2=[]) :
    for i in range(0, len(list2), 1) :
        list3.append(list1[i] + list2[i])
    print(list3)

sum_of_list(list1, list2)

# number 3 and 4
# Given a Python list of numbers. Turn every item of a list into its square
# Write a program that will calculate sum of lists members
list_1 = [1, 2, 3, 4]
list_2 = []
sum = 0
for i in range(0, len(list_1), 1):
    list_2.append(list_1[i]**2)
    sum = sum + list_1[i] + list_2[i]
print(list_2)
print("sum of elements equal to: " + str(sum))













