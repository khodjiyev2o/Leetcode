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

6. Sets are unindexed collection of objects that are unique. Sets cannot be indexed, unlike tuple and list.
    Tuple can be indexed , but cannot be changed. List can be indexed and changed.

7. Dictionary is hash table under the hood.

8. Python has 3 types of  name-spaces: global, local and built-in.
    global name-space is created at the start of the execution of a module,
    the built-in name-space comes into existence when the interpeter is invoked,
    local name-space is created at the invocation of a function.
9. It is impossible to change the global scope variable value from local function, to do that
   we need to "global" keyword , before the variable name.
```
a = 2
def inc_a():
    global a
    a+=1
```
also , it is impossible to change the local scope variable value from local function, to do that
   we need to "nonlocal" keyword , before the variable name.
```
def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter
```