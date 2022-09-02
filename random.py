import random
n= random.randint(5, 10)
print(n)
mylist=['cse','ece','mech','civil','eee']
print(random.choice(mylist))
random.shuffle(mylist)
myset={'hkv','madhusudan','venky','subbu'}
print(random.choice(list(myset)))
mydict={'CSE':'HKV','MECH':'SUBBU','EEE':'ROBIN','ECE':'RAMBABU'}
print(random.choice(list(mydict)))