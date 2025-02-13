def find_missing(arr):
    d = (arr[-1] - arr[0]) // len(arr)
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] != d:
            return arr[i - 1] + d