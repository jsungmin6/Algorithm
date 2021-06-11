class Queue:
    def __init__(self):
        self.items = []
    
    def en_queue(self,data):
        self.items.append(data)
    
    def de_queue(self):
        result = self.items[0]
        del self.items[0]
        return result
    
    def is_empty(self):
        return not self.items