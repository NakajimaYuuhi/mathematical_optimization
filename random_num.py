import random
total = random.randrange(1,10+1)

def random_num_list_generate(num):
    list=[]
    while num != 0:
        i = random.randrange(1,num+1)
        num -= i
        list.append(i)

    return list

print(total)
print(random_num_list_generate(total))
print(random_num_list_generate(total))

