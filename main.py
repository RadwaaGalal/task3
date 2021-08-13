def check_divisible(list, n):
    list_nums = []
    for ctr in range(list):
        nums = int(input("enter items of list"))
        list_nums.append(nums)
    print("the number in", list_nums,"that are divisible by", n, "are:")
    for check in list_nums:
        if check % n == 0:
            print(check)


num = int(input("enter numbers of items of list"))
div = int(input("enter divisible number"))
check_divisible(num, div)

