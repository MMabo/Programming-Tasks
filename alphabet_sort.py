string = input()
arr = []
indices = []

for i in range(len(string)):
    
    if ord(string[i]) >= 65 and ord(string[i]) <= 90:
        indices.append([string[i],i])

    arr.append(string[i])

for i in range(len(arr))
    arr[i] = arr[i].lower()
    
arr = sorted(arr)

for i in indices:
    index = arr.index(i[0].lower())
    arr[index] = arr[index].upper()
    

print(''.join(arr))
