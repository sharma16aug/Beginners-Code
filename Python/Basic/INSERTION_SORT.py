def insertsort(arr,n):
    for i in range(1,n):
        key = arr[i]
        j=i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key
if __name__ == "__main__":
    n = input()
    arr = map(int,raw_input().split(' '));
    insertsort(arr,n);
    print arr