class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Base case: empty list or single node
        if not head or not head.next:
            return head
        
        # Recursively reverse the rest of the list
        reversed_head = self.reverseList(head.next)
        
        # Reverse the links
        head.next.next = head  # Point the next node's next to current node
        head.next = None       # Break the original link
        
        return reversed_head  # Return the new head (original tail)

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

# Test the recursive solution
if __name__ == "__main__":

    input_values = [11, 2, 3, 4, 5]
    head = create_linked_list(input_values)
    
    print("Original linked list:")
    print_linked_list(head) 
    
    solution = Solution()
    reversed_head = solution.reverseList(head)
    
    print("Reversed linked list (recursive):")
    print_linked_list(reversed_head) 