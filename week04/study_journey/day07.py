# 双指针-移动零
def move_zero(nums:list):
    i = 0
    j = 0
    for num in nums:
        if num != 0:
            nums[i],nums[j] = nums[j],nums[i]
            j += 1
        i += 1
    return nums

# 哈希表-两数之和
def find_target_index(nums:list,target:int):
    hashmap = {}
    for i,n in enumerate(nums):
        if target - n in hashmap:
            return [i,hashmap[target - n]]
        hashmap[n] = i
    return 

if __name__ == '__main__':
    n1 = [0,1,2,3,4]
    n2 = [0,0,0,5,4,0]
    n3 = [3,3]
    t1 = 6
    n4 = [3,2,4]
    t2 = 6
    print(move_zero(n1))
    print(move_zero(n2))
    print(move_zero(n3))
    print(move_zero(n4))
    print(find_target_index(n3,t1))
    print(find_target_index(n4,t2))