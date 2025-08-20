dict = {
    'i': 2, 'love': 3, 'roblox': 2, 'rivals': 7, 'and': 2, 'minecraft': 4
}

print("The actual dictionary: " + str(dict))

freq = 2
hi = 0

for key in dict:
    if (dict[key] == freq):
        hi += 1
    
print("Frequency of k is: ", str(hi))