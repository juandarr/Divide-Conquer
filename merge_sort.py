'''
This program implements merge sort to sort an array of length n
Author: Juan Ríos
'''

def read_file(path):
    File = open(path,'r')
    content = File.read()
    array = content.split('\n')
    tmp = []
    for i in array:
        tmp.append(int(i))
    return tmp


def merge(b_array, c_array):
    n = len(b_array)+len(c_array)
    d_array = []
    i = 0
    j = 0
    for k in range(n):
        if b_array[i]<c_array[j]:
            d_array.append(b_array[i])
            i+=1
            if i==len(b_array):
                d_array += c_array[j:]
                break
        else:
            d_array.append(c_array[j])
            j+=1
            if j==len(c_array):
                d_array += b_array[i:]
                break
    return d_array

def merge_sort(array):
    n = len(array)
    if n==1:
        return array
    b_array = merge_sort(array[:n//2])
    c_array = merge_sort(array[n//2:])
    return merge(b_array, c_array)

example = read_file('IntegerArray.txt')
print(example[0:10])
print(merge_sort(example)[0:10])