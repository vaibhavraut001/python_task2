List1=["vaibhav","sachin","rohit",33.44,True]
print(List1[0])
List1[0]="Amar"
print(List1)

List2=["vaibhav","raut",33,True,"ram"]
List2[0]="Arc"
print(List2)
List2.append("vaibhav")
print(List2)

List3=[33,44,44.4,55,1,4]
List3.sort()
print(List3)

List4=["vaibhav","subhash","raut","lal","king"]
List4.sort()
print(List4)

list5=["raj",90,26,44.55,True,"amir"]
print(len(list5))

list6=["mumbai","samudrapur","math","king","chemistry"]
list6.sort(reverse=True)
print(list6)

list7=["manthan","mumbai","vaibhav","dharma","arjun"]
list7.append("Arc")
list7.sort()
print(len(list7))

list8=["vaibhav","sangram","arc",True,33.90]
list8.reverse()
print(list8)

list9=[22,33,56,"vaibhav","ram"]
list9.insert(0,73)  #(index,value)
print(list9)

list10=[22,33,56,"vaibhav","ram"]
list10.remove(22)
print(list10)

# list11=[22,33,56,"vaibhav","ram"]
# list11.pop(0)
# print(list11)
