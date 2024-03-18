def get_sum(nums,step):
    sum_list = []
    temp = 0
    # the pointer called i is actually the right pointer,the left pointer's value is i-step+1
    for i in range(len(nums)):
        if i < step - 1:
            temp += nums[i]
        elif i == step-1:
            temp += nums[i]
            sum_list.append(temp)
        else:
            temp -= nums[i-step]
            temp += nums[i]
            sum_list.append(temp)
    return sum_list

nums = [1,2,3,4,5,6,7]
print(get_sum(nums,3))