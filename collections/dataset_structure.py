tags = {
    'python',
    'coding',
    'tutorials'
}

#data sets require unique values - will not show duplicates but will show the last instance it is valued

# print(tags)

# print(tags[0]) # NOPE

# test = list(tags) # BAD PRACTICE

# print(test)

query_one = 'ruby' in tags
query_two = 'python' in tags

#returns True or False for these tag queries
# print(query_one)
# print(query_two)

###########COMBINING DATA SETS############

tags_again = {
    'ruby',
    'coding',
    'tutorials',
    'development'
}

# Merged tags
merged_tags = tags | tags_again # PIPE MAGIC
print(merged_tags)

# tags in tags_one but not in tags_two
exclusive_to_tags = tags - tags_again
print(exclusive_to_tags)

#data sets can have math used on them like numbers outright...
'''
math_set = {
    1,
    2,
    3
}

math_set2 = {
    4,
    5,
    6
}

math_together = math_set - math_set2
print(math_together)
'''

#tags found in both tags and tags_again
universal_tags = tags & tags_again
print(universal_tags)