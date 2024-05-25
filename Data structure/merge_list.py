def merge_lists():
    item1 = input("Please enter the first item : ").split()
    item2 = input("Please enter  the second item,: ").split()

    merged_list = list(set(item1 + item2))
    merged_list.sort()
    return merged_list


print(merge_lists())
