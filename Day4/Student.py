import pandas as pd

stu=pd.read_csv('Info.csv')
print(stu)

df=pd.DataFrame(stu)

gli=df['GPA'].tolist()
print(gli)

avg= sum(gli)/len(gli)
print(avg)

newgpa= float(input("Enter new gpa: "))
gli.insert(2,newgpa)
print(gli)