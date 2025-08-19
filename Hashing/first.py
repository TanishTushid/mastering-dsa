
def hash(n,m ):

    hash_list = [0] * 11

    for num in n:
        if 0 <= num <= 10:
            hash_list[num] += 1

    for nums in m:
        if nums <1 or nums > 10:
            print(0)
        else:
            print(hash_list[nums])

n = [5,3,2,2,0,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

hash(n,m)