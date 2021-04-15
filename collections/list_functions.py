#example blog tags #one of the most common bugs is 'off by one error' and it's due to using index/len interchangeably
tags = ['soda', 'cake', 'orange', 'tutorial']

'''
number_of_tags = len(tags) #how to get a count of list
last_item = tags[-1] #how to get a value of last item
index_last_item = tags.index(last_item) #returns us the index value of last item

print(number_of_tags)
print(last_item)
print(index_last_item)
'''

#how to sort lists

print(tags)

tags.sort() #alphabetically sorted my got dang list
tags.sort(reverse=True) #reverse alphabetized 

print(tags)

dates = ['1995', '1964', '1988']

dates.sort()

print(dates)

#sort does not return a value so...
''' 
li = ['1', '2', '3']
sorted_list = li.sort()

print(sorted_list)
print(li)
'''