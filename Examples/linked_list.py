
class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next

def get_list(head):
    probe = head
    while(probe != None):
        print(probe.data, end=' ')
        probe = probe.next
    print()

def length(head):
    probe = head
    count = 0
    while(probe != None):
        probe = probe.next
        count += 1
    
    return count

def insert(index, new_item, head):
    probe = head
    prev = None
    
    for i in range(index-1):
        prev = probe
        probe = probe.next
    
    if prev == None:
        head = Node(new_item, head)
    else:
        item = Node(new_item, probe)
        prev.next = item
    
    return head

def delete(index, head):
    probe = head
    prev = None

    for i in range(index-1):
        prev = probe
        probe = probe.next

    if prev == None:
        head = Node(probe.next.data, probe.next.next)
    else:
        prev.next = probe.next
        
    return head

def main():
    head = None
    for i in range(6):
        head = Node(i, head)
    
    get_list(head)
    head = delete(6, head)
    get_list(head)

main()
