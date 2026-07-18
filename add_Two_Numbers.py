# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        arr2 = []
        while l1 is not None:
            if l1 is not None:
                arr.append(l1.val)
                l1 = l1.next
            
        while l2 is not None:
            if l2 is not None:
                arr2.append(l2.val)
                l2 = l2.next

        delimiter = ""
        nums1 = map(str, arr)
        nums2 = map(str, arr2)
        joinsNums1 = int(str(delimiter.join(nums1)[::-1]))
        joinsNums2 = int(str(delimiter.join(nums2)[::-1]))
        suma = str(joinsNums1 +joinsNums2)
        sumaInvertida = suma[::-1] 
        cabeza = ListNode(int(sumaInvertida[0]))

        actual = cabeza
        for i in range(1,len(sumaInvertida)):
            actual.next = ListNode(int(sumaInvertida[i]))
            actual = actual.next
        return cabeza