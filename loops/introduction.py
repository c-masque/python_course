# for in loop # iterating over something
# 'iterator variable' = name in code below
for name in ['ryan', 'maud', 'leo', 'someone else']:
    print(name)

# while loop # need sentinel value # condition
sentinel_value = 0

while sentinel_value < 10:
    print('loop confirmed')
    sentinel_value += 1

#for loops have clearly defined start and stop
#while loops will not stop when it reaches the end of a list
#while loop explicitly has to be told when to stop
#this is why you wouldn't normally use them - infinite loops can crash, man
