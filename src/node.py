class Node:
    
    def __init__(self, data=None):
        #  --------------
        # | data  | None |
        #  --------------
        if not data:
            raise ValueError('Node cant be init without value/data')
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)
