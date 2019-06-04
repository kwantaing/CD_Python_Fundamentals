#1 Update Values in Dictionary and Lists

x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

def updateVals(x,z, students,sports_directory):
    x[1][0] = 15
    students[0]['last_name'] = 'Bryant'
    sports_directory['soccer'][0] = "Andres"
    z[0]['y']=30
    print(x)
    print(students)
    print(sports_directory)
    print(z)

updateVals(x,z,students,sports_directory)

#2 Iterate Through List of Dictionaries

def iterateDictionary(some_list):
    for dictionary in some_list:
        for k,v in dictionary.items():
            print(k+"-"+v)
            
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 

#3 Iterate Through a Dictionary with List Values

#switch case if "first_name", execute a, if "last_name", execute b
def iterateDictionary2(key_name,some_list):
    if(key_name =="first_name"):
        for dictionary in some_list:
            for key_name in dictionary:
                if("first_name"==key_name):
                    print(dictionary[key_name])
    else:
        for dictionary in some_list:
            for key_name in dictionary:
                if("last_name"==key_name):
                    print(dictionary[key_name])

iterateDictionary2("first_name",students)
iterateDictionary2("last_name",students)

#4 Iterate through a dictionary with list values

def printInfo(some_dict):
    for k, v in some_dict.items():
        print(str(len(some_dict[k])),k.upper())
        for i in some_dict[k]:
            print(i)
        print("\n")


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)