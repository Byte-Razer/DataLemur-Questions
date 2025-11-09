def longest_consecutive(nums):
    nums=list(set(nums))
    nums=sorted(nums)
    print("Array: ",nums)
    if len(nums)==0 or len(nums)==1:
     maxcount=0
    else:
        length=len(nums)
        print("Length: ",length)
        count=1
        countlist=[]
        for i in range(length):
          if (nums[i]+1)==(nums[i+1]):
            count=count+1
            countlist.append(count)
          else:
            count=1
          if i+2==length:
            break
        maxcount=max(countlist)
        print(countlist)
    return maxcount
nums = [100, 4, 200, 1, 3, 2]
#Test cases:
#[100, 4, 200, 1, 3, 2]
#[3, 2]
#[1,2,0,1]
#[9,1,4,7,3,-1,0,5,8,-1,6]
#[-1,-1,-1]
print(longest_consecutive(nums))