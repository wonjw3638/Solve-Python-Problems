import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

cnt = 0

def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        global cnt
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            elif arr[l] > arr[h]:
                temp.append(arr[h])
                cnt += (mid - l)
                h += 1
            else:
                temp.append(arr[l])
                temp.append(arr[h])
                l += 1
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, N)

merge_sort(arr)
print(cnt)