from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    length = len(nums) #nums의 length 저장
    for i in range(length): #모든 nums에 있는 값에 대해 
        for j in range(i+1, length): #현재 선택한 i의 뒷쪽만 확인
            if nums[i] + nums[j] == target: #두 숫자의 합이 target과 같으면
                return [i, j] #return index


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
