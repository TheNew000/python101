zombie0 = {
    'speed': 10,
    'power': 6,
    'hunger': 5,
    'name': 'Joe'
}

# print zombie0
# print zombie0['speed']

# add properties like javascript
zombie0['weapon'] = 'axe'
zombie0['position_x'] = 23
# print zombie0

# delete with del
zombie0['huh'] = "pointless"
# print zombie0
del zombie0['huh']
# print zombie0

# for loops through dict start with prop placeholder followed by key-value
for key, value in zombie0.items():
    print "The key is:'",key,"'with a value of:",value
    print zombie0[key]
    print zombie0.has_key('name')

# eliminate value and get value from dict[key]
for key in zombie0:
    print zombie0[key]

# sort dictionary in natural order
for key in sorted(zombie0):
    print key + ':' + str(zombie0[key])

zombies = []
zombies.append({
    'speed': 10,
    'power': 6,
    'hunger': 5,
    'name': 'Joe'
})
zombies.append({
    'speed': 15,
    'power': 9,
    'hunger': 3,
    'name': 'Hambone'
})
zombies.append({
    'speed': 5,
    'power': 16,
    'hunger': 9,
    'name': 'Hank'
})

for zombie in zombies:
    print zombie['name']

# just like JS you can assign a list to a dictionary
zombies[0]['victims'] = ['Jane', 'Zane', 'Bill']
print zombies

# just like JS you can assign a dictionary to a dictionary
zombies[0]['super_mode'] ={
    # At night...
    'power': 23,
    'hunger': 20,
    'weapon': 'bat'
}

print zombies[0]['super_mode']['weapon']
