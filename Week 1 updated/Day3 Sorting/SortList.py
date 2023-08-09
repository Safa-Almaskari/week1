"""
You are given a list of students, each represented as a
dictionary with the following attributes: name, age, and gpa.
Your task is to sort the list of students based on their GPA
in descending order using the Insertion Sort algorithm.

Example of a student dictionary:

students = [

{"name": "Alice", "age": 20, "gpa": 3.9},

{"name": "Bob", "age": 22, "gpa": 3.7},

{"name": "Charlie", "age": 21, "gpa": 4.0},

{"name": "David", "age": 19, "gpa": 3.5},

]
"""

def insertion_sort_dictionary(arr,stype):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1


        while j >= 0 and key[stype] > arr[j][stype]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        
def main():
    students = [

        {"name": "Alice", "age": 20, "gpa": 3.9},

        {"name": "Bob", "age": 22, "gpa": 3.7},

        {"name": "Charlie", "age": 21, "gpa": 4.0},

        {"name": "David", "age": 19, "gpa": 3.5},
    
        ]
    
    
    print("Original students:")
    for s in students: #to display each student in dictionary
        print(s)
    print('-----------------------------------')
    insertion_sort_dictionary(students, "name")
    print("Sorted Dictionary: ", students)
    
    #print("first: ",students[0]["gpa"])
    #x=list(students)
    #print(x)
    #insertion_sort_dictionary(students)
    #print(x)
    
    
main()
        
        






