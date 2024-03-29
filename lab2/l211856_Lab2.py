#
#
# # Question 1
# def return_string(number):
#     if int(number)>=10:
#         return "Number of chickens: many "
#     else:
#         return "Number of chickens " + str(number)
#
# user_input=input("Enter the number of chickens ")
# print(return_string(user_input))
#
# #Question 2
# def return_string(user_input):
#     if len(user_input)<3:
#         return " "
#     else:
#         return user_input[:3]+user_input[-3:]
#
# user_input=input("Enter the string  ")
#
# print("returned string is ",return_string(user_input))
#
# #Question 3
# def return_string(user_input):
#     user_changed=user_input[1:]
#     s=user_input[0]
#     user_changed=user_changed.replace(s.lower(),"@")
#     user_changed = user_changed.replace(s.upper(), "@")
#     return s+user_changed
#
# user_input=input("Enter the string  ")
# print("returned string is ",return_string(user_input))
#
# #Question 4
# def return_string(input1,input2):
#     a=input1[:2]
#     b=input2[:2]
#     input1 = b + input1[2:]
#     input2=a+input2[2:]
#     return input1+" "+input2
#
# user_input=input("Enter the string 1  ")
#
# user_input1=input("Enter the string 2  ")
#
# print("returned string is ",return_string(user_input,user_input1))
#
# #Question 5
# def return_count(list_of_strings):
#     counter=0
#     for i in range(0,len(list_of_strings)):
#         for j in range(0,len(list_of_strings)):
#             if j==i:
#                 break
#             else:
#                 if(list_of_strings[i][0]==list_of_strings[j][0]) and list_of_strings[i][-1]==list_of_strings[j][-1]:
#                     counter=counter+1
#     return counter
# list_of_strings = ['apple', 'aanane', 'mango']
#
# print("Number of matches in list are",return_count(list_of_strings))
#
#
# #Question 6
# def return_list(list_):
#     return sorted(list_)
#
# list_of_strings = ['apple', 'aanane', 'mango']
# print(return_list(list_of_strings))
#
#
# #Question 7
# def sort_by_last_element(data):
#  return sorted(data, key=lambda x: x[-1])
#
# data = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
# sorted_data = sort_by_last_element(data)
# print(sorted_data)
#
# #Question 8
# def my_function(x):
#   return x[::-1]
# print("Enter a string")
# string_a=input()
#
# reversed = my_function(string_a)
#
# if(string_a==reversed):
#     print("String is palindrome")
# else:
#     print("String is not a palindrome")
#
#
#
# #Question 9
# def flatten(list_):
#  flat_list = []
#  for row in list_:
#     flat_list.extend(row)
#  return flat_list
#
# list_=[[1,2,3],[4,5]]
#
# print(flatten(list_))
#
# #Question 10
# def ret_intersection(list1,list2):
#
#     set1=set(list1)
#     set2=set(list2)
#
#     common_elements=set1.intersection(set2)
#
#     return list(common_elements)
#
# list1=[1,2,2,2,3]
# list2=[4,2,6]
#
# print("Intersection is",ret_intersection(list1,list2))
#
# #Question 11
# def check_anagram(str1, str2):
#   str1 = str1.lower()
#   str2 = str2.lower()
#
#   if sorted(str1) == sorted(str2):
#         return True
#   else:
#         return False
#
#
# str1 = "cinema"
# str2 = "iceman"
# print("Result is ",check_anagram(str1,str2))
#
#
# #Question 12
# def binary_search(sorted_list, target):
#   start = 0
#   end = len(sorted_list) - 1
#
#   while start <= end:
#     mid = (start + end) // 2
#
#     if sorted_list[mid] == target:
#       return mid
#
#     elif sorted_list[mid] < target:
#       start = mid + 1
#
#     else:
#       end = mid - 1
#
#   return -1
#
# sorted_list = [1, 3, 5, 7, 9]
# target = 7
# index = binary_search(sorted_list, target)
# print("Target found at index",index)
#
#
# #Question 13
# def merge_sort(data):
#   if len(data) <= 1:
#     return data
#
#   mid = len(data) // 2
#   left = merge_sort(data[:mid])
#   right = merge_sort(data[mid:])
#   return merge(left, right)
#
# def merge(left, right):
#   merged = []
#   i = 0
#   j = 0
#   while i < len(left) and j < len(right):
#     if left[i] < right[j]:
#       merged.append(left[i])
#       i += 1
#     else:
#       merged.append(right[j])
#       j += 1
#
#   merged += left[i:]
#   merged += right[j:]
#   return merged
#
# data = [6, 5, 3, 1, 8, 7, 2, 4]
# sorted_data = merge_sort(data)
# print("Sorted list is as: ",sorted_data)
#
# #Question 14
# def quicksort(arr):
#   if len(arr) <= 1:
#     return arr
#   else:
#     pivot = arr[0]
#     less = [x for x in arr[1:] if x <= pivot]
#     greater = [x for x in arr[1:] if x > pivot]
#     return quicksort(less) + [pivot] + quicksort(greater)
#
#
# my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# sorted_list = quicksort(my_list)
# print("Sorted list is as: ",sorted_list)
#
# #Question 15
# def count_frequency(list_):
#   dictionary = {}
#   for x in list:
#     if x in dictionary:
#       dictionary[x] += 1
#     else:
#       dictionary[x] = 1
#   return dictionary
#
#
#
# list = [1, 2, 2, 3, 4, 2]
# result = count_frequency(list)
# print("Dictionary is as:",result)
#
# #Question 16
# def return_count(list):
#   set1=set(list)
#   return len(set1)
#
# list=[1,2,2,3,4,2]
# print("No of distinct elements in list are ",return_count(list))
#
# #Question 17
# def return_tuple(set1, set2):
#   union = set1.union(set2)
#   intersection= set1.intersection(set2)
#   return union, intersection
#
#
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# result_tuple = return_tuple(set1, set2)
# print("Union:", result_tuple[0])
# print("Intersection:", result_tuple[1])
#
# #Question 18
# def unique_values(input_dict):
#   list_=set(input_dict.values())
#   return list_
#
# dict = {"a": 10, "b": 20, "c": 10, "d": 30}
# result_list = unique_values(dict)
# print("Unique values are",result_list)
#
#
# #Question 19
# def most_frequent_keys(input_dict):
#   frequency_dict = {}
#   max_frequency = 0
#
#
#   for key, value in input_dict.items():
#     if value in frequency_dict:
#       frequency_dict[value].append(key)
#     else:
#       frequency_dict[value] = [key]
#
#     max_frequency = max(max_frequency, len(frequency_dict[value]))
#
#   result_keys = []
#   for key_list in frequency_dict.values():
#     if len(key_list) == max_frequency:
#       result_keys.extend(key_list)
#
#   return result_keys
#
# my_dict = {"a": 10, "c":10,"b": 20, "c": 10, "d": 30, "e": 20}
# result_keys = most_frequent_keys(my_dict)
# print("Resukt keys are: ", result_keys)
#
#
# #Question 20
#
# def merge_dict(d1, d2):
#   result_dict = d2.copy()
#   result_dict.update(d1)
#   return result_dict
#
# d1 = {"a": 10, "b": 20, "c": 30}
# d2 = {"b": 25, "c": 35, "d": 40}
# merged_dictionary = merge_dict(d1, d2)
# print("Merged Dictionary is:",merged_dictionary)
#
# #Question 21
# def filter_dict(list_of_dicts, target_key):
#   filtered_ = []
#   for x in list_of_dicts:
#     if target_key in x:
#       filtered_.append(x)
#   return filtered_
#
# list_of_dicts = [
#   {"name": "Alice", "age": 25, "city": "New York"},
#   {"name": "Bob", "age": 30, "city": "San Francisco"},
#   {"name": "Charlie", "age": 22}
# ]
#
# target_key = "city"
# filtered_list = filter_dict(list_of_dicts, target_key)
# print("Filtered list is as : ",filtered_list)
#
# #Question 22
# def ret_duplicates(list_):
#   ret_list=[]
#   for i in range(0,len(list_)):
#     for j in range(0,len(list_)):
#       if i==j:
#         break;
#       else:
#         if list[i]==list[j]:
#           ret_list.append(list[i])
#   list1=set(ret_list)
#   return list1
#
# list=[1,2,2,3,4]
# print("returned list of duplciates is ",ret_duplicates(list))