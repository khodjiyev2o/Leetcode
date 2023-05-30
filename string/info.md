1. Strings are immmutable type, once created they cannot be modified.
2. Strings  support sequence type operations except assignment due to their immutability.
```

name = 'obiesie'
name[1]

```
3. Strings can be concatenated to create new strings as shown in the following example
```

name = 'obiesie'
surname = " Ike-Nwosu"
full_name = name + surname

```
4. Python Enumerat
```
names = ["Joe", "Obi", "Chris", "Jamie"]
for index, name in enumerate(names):
    print("{}. {}".format(index, name))
```

5. Tuples: These are also another type of sequence structures. A tuple consists of a number of comma
    separated objects for example.
```

companies = "Google", "Microsoft", "Tesla"
>>> companies
('Google', 'Microsoft', 'Tesla')
    
```
Tuples are integer indexed just like lists but are immutable; once created 
    the contents cannot be changed by any means such as by assignment.

However, if the object in a tuple is a mutable object such as a list, such object 
    can be changed as shown in the following example:
```

>>> companies = (["lockheedMartin", "Boeing"], ["Google", "Microsoft"])
>>> companies
    (['lockheedMartin', 'Boeing'], ['Google', 'Microsoft'])
>>> companies[0].append("SpaceX")
>>> companies
    (['lockheedMartin', 'Boeing', 'SpaceX'], ['Google', 'Microsoft'])
```
