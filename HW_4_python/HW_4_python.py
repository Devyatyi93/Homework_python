count = 0
range_count = 10
for_count = 0
run = True

# while run:
#     print("Hello Cycle")
# while run:
#     print("Step =", count)
# while count<range_count:
#     print("Step=", count)
#     count+=1
# while count<range_count:
#     print("Step=", count)
#     count+=1
#     if count==3:
#         print("Step=", count, 'If body')
# while run:
#     print("Step=", count)
#     count+=1
#     if count==range_count:
#         print("STOP", count)
#         break
# for item in range(for_count, range_count):
#     print('Step=', item)

# for item in range(0, 30):
#     print('Step=', item)
#     if item == 5:
#         print('Item=', item)
#     elif item == 10:
#         print('Item=', item)
#     elif item < 4:
#         print('Item <', item)
#     elif item >= 27:
#         print('Item >=', item)

# for item in range(0, range_count + 1):
#     print('Step=', item)
#     if item == 7:
#         inner_count = 0
#         print('-- inner_count =', inner_count)
#         for inner_item in range(0, item):
#             print('-------- Inner_Step=', inner_item)
#             if inner_item == 5:
#                 inner_count = inner_item
#         print('-- inner_count=', inner_count)


for item in range(0,20):
    print('Step =', item)
    if 7<item<12:
        print('If_item =', item)
        continue
