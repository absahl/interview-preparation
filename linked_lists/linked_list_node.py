class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.arbitrary = None

    def __repr__(self):
        return str(self.data)
