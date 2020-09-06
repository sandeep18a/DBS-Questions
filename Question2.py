p=[]
length=int(input("Number elements in list"))
diff=int(input("enter difference"))
for each in range(0,length):
    ele=int(input("number"))
    p.append(ele)

def getPairs(p, diff):
    print(p)
    a=set()
    sublist=[]
    for each in p:
        #checking for an element with difference as 2
        if each-diff in p:
            sublist=[]
            tup=[]
            sublist.append(each-diff)
            sublist.append(each)
            tup=tuple(sublist)
            "adding  them to tuple"
            a.add(tup)
            # checking for an element with difference as 2 after adding
        elif each+diff in p:
            sublist = []
            tup = []
            sublist.append(each)
            sublist.append(each + diff)
            tup = tuple(sublist)
            a.add(tup)
        else:
            pass
    g=list(a)
    return g
print(getPairs(p,diff))