def find_common_elements(list1, list2):
    # Convert both lists to sets to find common elements
    set1 = set(list1)
    set2 = set(list2)
    # Find the intersection of both sets
    common_elements = list(set1.intersection(set2))
    return common_elements

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common_elements = find_common_elements(list1, list2)
print(f"Common elements: {common_elements}")
