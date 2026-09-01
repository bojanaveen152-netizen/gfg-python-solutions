x = int(input())
store=""

for i in range(0,x+1):
    decreasing=(x-i)
    store=store+str(decreasing)+" "
print(store)
