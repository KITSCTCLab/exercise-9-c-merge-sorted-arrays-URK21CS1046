from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
  x = nums1[0:m]
  y = nums2[0:n]
  nums1 = x+y
  nums1 = merge_sort(nums1)
  return nums1

def merge_sort(list) -> None:
  if len(list)>1:
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]
    
    merge_sort(left)
    merge_sort(right)
    
    i,j,k =0,0,0
    
    while i<len(left) and j<len(right):
      if left[i] <= right[j]:
        list[k] = left[i]
        i+=1
      else:
        list[k] = right[j]
        j+=1
       
      k+=1
       
    while i<len(left):
      list[k] = left[i]
      i+=1
      k+=1
      
    while j<len(right):
      list[k] = right[j]
      j+=1
      k+=1
      
  return list 

# Do not change the following code
nums1 = []
nums2 = []
for item in input().split(', '):
  nums1.append(int(item))
for item in input().split(', '):
  nums2.append(int(item))
m = int(input())
n = int(input())

print(merge(nums1, m, nums2, n))
