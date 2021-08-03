#   The Data
data = [2, 4, 65, 74, 83, 92, 106, 127, 149, 168
    , 182, 199, 204, 208, 248, 252]

#  The Limits
min_valid = 100
max_valid = 250

#   processing the lower values
stop = 0

for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop) #  for debugging purposes
del data[:stop]
print(data)

# processing the higher values
start = 0

for index in range(len(data) -1, -1, -1):
    if data[index] <= max_valid:
        # We Have The Index Of The Last Item To Keep
        # Set 'Start' To The Position Of The First
        # item to delete, which is 1 after 'index'.
        start = index + 1
        break

print(start) # For Debugging Purposes
del data[start:]
print(data)


