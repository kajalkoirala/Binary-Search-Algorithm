def binary_search(arr, target):
    # Initialize pointers to the start and end of the list
    low = 0
    high = len(arr) - 1

    # Loop until the search range is valid
    while low <= high:
        # Find the middle index
        mid = (low + high) // 2

        # If the middle element is the target, return its index
        if arr[mid] == target:
            return mid

        # If the target is greater than the middle element, search in the right half
        elif arr[mid] < target:
            low = mid + 1

        # If the target is smaller, search in the left half
        else:
            high = mid - 1

    return -1



user_input = input("Enter a sorted list of numbers: ")
sorted_list = list(map(int, user_input.split(',')))


target = int(input("Enter the number to search for: "))


result = binary_search(sorted_list, target)


if result != -1:
    print(f"Target found at index {result}")
else:
    print("Target not found")
