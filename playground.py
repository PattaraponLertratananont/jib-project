a = 1
b = 'string'
c = True
d = b + ' hello'
print(a,b,c,d)

# python version 3.6 up can use f string for show something 
print(f'c is {c}',f'a is {a}')

# LIST
l = [1,'2',3,'4']
print(f'list is {l}')

#Tuple is immutable, can't delete, change value
t = (1,'2',3,'4')
print(f'Tuple is {t}')

# Dict
dt = {
    'name':'Ball',
    'team':'Odds',
}
print(dt.items())
print(dt.keys())
print(dt.values())

print(f'l at index 0 : {l[0]}')
print(f't at index 1 : {t[1]}')
print(f'dt at key team : {dt["team"]}')

# if

a = 2
if a == 1:
    print(a)
    print('hello')
elif a == 2:
    print('equal 2')
else:
    print('not 1')

# For
l = [1,2,3,4,5]
for item in l:
    print(item)
    if item == 1:
        print('yeah')