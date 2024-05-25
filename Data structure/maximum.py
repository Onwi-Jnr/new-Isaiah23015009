def find_max_min():
    number = input("Please enter some numbers: ").split()
    nums = [int(x) for x in number]

    if not number:
        print("No integer.")
        return None

    max_num = max(nums)
    min_num = min(nums)

    return max_num, min_num
result = find_max_min()
if result:
    max_num, min_num = result
    print(f"Maximum  is: {max_num}")
    print(f"Minimum  is: {min_num}")

