def tribonacci(num):
    trib = [1, 1, 2]
    if num == 1:
        print(1)
        return
    elif num == 2:
        print("1 1")
        return
    elif num == 3:
        print("1 1 2")
        return

    for _ in range(3, num):
        next_num = trib[-1] + trib[-2] + trib[-3]
        trib.append(next_num)

    print(" ".join(str(x) for x in trib))


n = int(input())
tribonacci(n)