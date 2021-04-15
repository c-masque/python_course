tags = [
    'apple',
    'frosting',
    'sugar',
    'lemon',
    'egg'
]

print(tags[1:4:2]) #three potential arguments - explicit version of slice object

slice_obj = slice(1, 4, 2) #best way to store slice in varaiable - three potential arguments - where start, how far it goes, how much it skips

print(slice_obj.start) #start tells me first index
print(slice_obj.stop) #start tells me last index
print(slice_obj.step) #start tells me step index

print(tags[slice_obj])