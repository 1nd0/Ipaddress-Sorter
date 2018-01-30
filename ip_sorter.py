
# Function that will check an item in and see if it has seen it before, If it has it will not produce it again.
def uniqify(iterable):
    seen = set()
    for item in iterable:
        if item not in seen:
            seen.add(item)
            yield item

#prompt for file you want imput
filename = input("What is the file of ip addresses you want Sorted: ")

#declaring a list to be used to store the results of the function
results = []

# Opens the iplist.txt file and stores it in test. Then it sorts the file and puts it in ascending order
with open(filename, 'r') as test:
    iplist = sorted([i.strip() for i in test.readlines()], key=lambda x: int(''.join((lambda a: lambda v: a(a, v))(lambda s, x: x if len(x) == 3 else s(s, '0' + x))(i) for i in x.split('.'))))

# Calls the function on the sorted values in iplist
for unique_item in uniqify(iplist):
    # Appends the value from the function into the results list
    results.append(str(unique_item))

# Creates a new file called results.txt and makes it writeable and stores it as outfile
with open("results.txt", "w") as outfile:
    # Creates a new line and loops the values stored in the results list
    outfile.write("\n".join(i for i in results))