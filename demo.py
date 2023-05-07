# 插入排序

def inserttion(arr):
    for i in range(len(arr[1:])):
        curr = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > curr:
            arr[j + 1] = arr[j]
            j -= 1
    arr[j + 1] = curr


    return arr

if __name__ == '__main__':
    arr = [1, 6, 7, 90, 99]
    arr1 = inserttion(arr)
    print(arr1)
