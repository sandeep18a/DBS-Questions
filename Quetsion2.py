//quest 2
def getPairs(p,diff):
    p.sort()
    print(p)
    i=0
    r=[]
    print(len(p))
    for i in range(0,len(p))  :
      print("loop started")
      k=1
      sublist=[]
      while k<(len(p)-i):
          print(diff)
          # print(i)
          # print(k)
          if p[i+k]-p[i] ==diff:
            print(p[i])
            print(p[i+k])
            sublist.append(p[i])
            sublist.append(p[i+k])
            r.append(sublist)
            k = k + 1
          else:
              # print(i)
              # print(k)
              print("in else")
              pass
              k=k+1
    return r

p=[]
length=int(input("elements in list"))
diff=int(input("enter difference"))
for each in range(0,length):
    ele=int(input("number"))
    p.append(ele)
print(getPairs(p,diff))

