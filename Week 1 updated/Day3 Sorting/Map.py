import re
a = ["dog", "cat", "wildcat", "thundercat", "cow", "hooo"]
#compile the re
r=re.compile(".*cat")
nList=list(filter(r.match,a))
print(n  List)


newList= list(filter(lambda v: re.match(".*cat",v),a))
length=list(map(lambda a: len(a) ,newlist))
print(newList)
print(length)