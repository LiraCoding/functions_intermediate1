# 1
x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
print(x)

# 2
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
print(students)

# 3
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

# 4
z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z)

# 5
children = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(children_List):
    for x in range(0, len(children_List)):
        print(children_List[x])
    iterateDictionary(children_List)

# 6
def iterateDictionary2(first_name_List):
    first = {
        'first_name':  'Michael', 'first_name' : 'John', 'first_name' : 'Mark','first_name' : 'KB'
        }
    for things in first:
        print(things)
        iterateDictionary2(first_name_List)

def iterateDictionary2(last_name_List):
    last = {
        'last_name': 'Jordan', 'last_name' : 'Rosales', 'last_name' : 'Guillen','last_name' : 'Tonel'
        }
    for name in last:
        print(name)
        iterateDictionary2(last_name_List)


# 7
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(var):
    for map in var:
        print(len(var[map]), map.upper())
        for value in var.get(map):
            print(value)
printInfo(dojo)
