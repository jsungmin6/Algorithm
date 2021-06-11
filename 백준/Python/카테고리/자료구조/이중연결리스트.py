class Node:
    def __init__(self,data,prev = None,next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DList:
    def __init__(self,data):
        self.head = Node(data)
        self.tail = self.head

    #맨뒤에 데이터를 넣는다.
    def insert(self,data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            cur = self.head
            while cur.next:
                cur=cur.next
            new = Node(data)
            cur.next = new
            new.prev = cur
            self.tail = new

    def search_from_head(self,data):
        if self.head == None:
            return False
        cur = self.head

        while cur:
            if cur.data = data:
                return cur
            else:
                cur = cur.next
        
        return False

    def search_from_tail(self,data):
        if self.head == None:
            return False
        cur = self.tail

        while cur:
            if cur.data = data:
                return cur
            else:
                cur = cur.prev
        
        return False
    
    def insert_before(self,data,before_data):
        if self.head == None:
            self.haed = Node(data)
            return True
        else:
            cur = self.tail
            while cur.data != before_data:
                cur = cur.prev
                if cur == None:
                    return False
            new = Node(data)
            before_cur = cur.prev
            before_cur.next = new
            new.prev = before_cur
            new.next = cur
            cur.prev = new