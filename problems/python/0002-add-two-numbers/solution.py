# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()  # Dummy node to simplify code
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            sum_val = carry
            
            if l1:
                sum_val += l1.val
                l1 = l1.next
            
            if l2:
                sum_val += l2.val
                l2 = l2.next
            
            carry = sum_val // 10
            current.next = ListNode(sum_val % 10)
            current = current.next
        
        return dummy.next

# Helper function to create a linked list from a list of integers
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert linked list to list for easy printing
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test the solution
def main():
    solution = Solution()
    
    # Test case 1: l1 = [2,4,3], l2 = [5,6,4] -> [7,0,8]
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    result = solution.addTwoNumbers(l1, l2)
    print(f"Test 1: Input l1 = [2,4,3], l2 = [5,6,4], Output = {linked_list_to_list(result)}")  # Expected: [7, 0, 8]
    
    # Test case 2: l1 = [0], l2 = [0] -> [0]
    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    result = solution.addTwoNumbers(l1, l2)
    print(f"Test 2: Input l1 = [0], l2 = [0], Output = {linked_list_to_list(result)}")  # Expected: [0]
    
    # Test case 3: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9] -> [8,9,9,9,0,0,0,1]
    l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = create_linked_list([9, 9, 9, 9])
    result = solution.addTwoNumbers(l1, l2)
    print(f"Test 3: Input l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9], Output = {linked_list_to_list(result)}")  # Expected: [8, 9, 9, 9, 0, 0, 0, 1]

if __name__ == "__main__":
    main()