file_builder = open('logger.txt', 'r+') # open() will create if it doesn't exist!

#file_builder.write('balance = 500')
for i in range(10):
    file_builder.write(f"There are {i + 1} kitties!\n")
    #write will overwrite all content
print('Kitties uploaded!')

file_builder.close()