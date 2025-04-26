class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next  # Parallel assignment
        return prev

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to print a linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()

# Test the code
if __name__ == "__main__":
    # Example input: 1 -> 2 -> 3 -> 4 -> 5
    input_values = [1, 2, 3, 4, 5]
    head = create_linked_list(input_values)
    
    print("Original linked list:")
    print_linked_list(head)  # Output: 1 -> 2 -> 3 -> 4 -> 5
    
    # Reverse the linked list
    solution = Solution()
    reversed_head = solution.reverseList(head)
    
    print("Reversed linked list:")
    print_linked_list(reversed_head)  # Output: 5 -> 4 -> 3 -> 2 -> 1