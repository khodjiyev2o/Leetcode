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