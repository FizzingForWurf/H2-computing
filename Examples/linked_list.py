
class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next
    
    def data(self):
        return self.data
    
    def next(self):
        return self.next

def get_list(head):
    probe = head
    while(probe != None):
        print(probe.data, end=' ')
        probe = probe.next
    print()
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

def main():
    head = None
    for i in range(2):
        head = Node(i, head)
    
    #head = insert(6, 3132, head)
    print(get_list(head))

main()
