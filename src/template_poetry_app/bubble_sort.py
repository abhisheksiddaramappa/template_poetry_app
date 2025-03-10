def bubble_sort(arr):
    """Sorts an array of integers using the bubble sort algorithm.

    Args:
        arr (list): The list of integers to sort.
    
    Returns:
        None: The function modifies the list in place.
    """
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
