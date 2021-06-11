class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

class SList:
    def __init__(self,data):
        self.head = Node(data)
    
    #추가
    def append(self,data):
        cur = self.haed
        while cur.next:
            cur = cur.next
        cur.next = Node(data)

    #삭제
    def delete(self,data):
        # 헤드가 없을경우 방어
        if not self.head:
            return
        # 타깃이 헤드일경우
        if self.head.data == data:
            temp = self.data
            self.head = self.head.next
            del temp
        # 타깃이 헤드가 아닐경우
        else:
            cur = self.head
            while cur.next:
                if cur.next.data = data:
                    temp = cur.next.data
                    cur.next = cur.next.next
                    del temp
                else:
                    cur= cur.next