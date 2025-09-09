def insertion_sort(arr):
    """
    Sorts the array using Insertion Sort algorithm.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key

if __name__ == "__main__":
    data = [5, 2, 9, 1, 5, 6]
    print("Original list:", data)
    insertion_sort(data)
    print("Sorted list:", data)
