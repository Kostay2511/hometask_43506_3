import fun
import numpy as np
#test array
array = [5,4,7,8,2,3,8.21,32,45,12,8.21,34,98,13,56,43,4,253,46,3,4]

print("input:",array)
# check on input value
if (fun.Check_array(array)):
    # sort array
    array=np.array(array, float)
    fun.sort(array, 0, len(array) - 1)
    print("output: [", ','.join(str(i) for i in array),"]")
print("end")