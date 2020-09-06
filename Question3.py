data=[("username1","phone_number1", "email1"),
 ("usernameX","phone_number1", "emailX"),
 ("usernameZ","phone_numberZ", "email1Z"),
 ("usernameY","phone_numberY", "emailX"),("usernameY","phone_numberP", "emailP"),("usernameQ","phone_numberQ", "emailQ")]

def getsubindices(data):
    listdata=[]
    finalset=set()
    for each in data:
       listdata.append(list(each))
    print(listdata)
    for j in range(0,len(listdata[0])) :
        for i in range(0,len(listdata)-1):
                k=1
                while k <len(listdata)-i:
                    #comparing the element with the next element
                    if(listdata[i + k][j] == listdata[i][j]):
                        # adding to set to avoid duplicates
                        finalset.add(i)
                        finalset.add(i+k)
                        k=k+1
                    else:
                        k=k+1
    duplicate=list(finalset)
    finallist=[]
    finallist.append(duplicate)
    unique=[]
    for x in range(0,len(listdata)):
     if x in duplicate:
         pass
     else:
         unique.append(x)
    finallist.append(unique)
    return finallist
print(getsubindices(data))
