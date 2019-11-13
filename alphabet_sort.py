string = input()
arr = []
temp = []
indices = []

for i in range(len(string)):
    
    if ord(string[i]) >= 65 and ord(string[i]) <= 90:
        indices.append([string[i],i])

    arr.append(string[i])

for i in range(len(arr)):
    
    arr[i] = arr[i].lower()
    arr = sorted(arr)

print(arr)
for i in range(len(indices)):

    arr[indices[i][1]] = arr[indices[i][1]].upper()

print(arr)
##print(indices)
##print(arr)
##print(temp)

##for char in arr:
##    print(char)
##    result.append(char.lower())
##    
##print(arr)
##print(result)
##
##result = sorted(result)
##
##for char in result:
##    if char.upper() in arr:
##        result.replace()
