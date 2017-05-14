
import numpy as np

#---------------- list ------------------#
arr = [1, 2, 3, 4, 5]
print(arr)

nparr = np.array(arr)

# filter
print((nparr == 3))
filter = nparr == 3

print(nparr[filter])
print(nparr[~filter])

#---------------- 2d ------------------#
nparr = np.arange(12).reshape(4, 3)
print(nparr)
print(nparr[:, 0])
print(nparr[:, 1])
print(nparr[:, 2])

filter = nparr == 3
print(filter)

print(nparr[filter])
print(nparr[~filter])
