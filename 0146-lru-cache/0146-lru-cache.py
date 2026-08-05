class LL:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        head = LL(-1, -1)
        tail = LL(-1, -1)
        head.next = tail
        tail.prev = head

        self.head = head
        self.tail = tail
        self.cap = capacity
        self.mpp = {}

    def del_N(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        head = self.head
        node.next = head.next
        node.prev = head
        head.next.prev = node
        head.next = node

    def get(self, key: int) -> int:
        mpp = self.mpp
        if key not in mpp:
            return -1
        node = mpp[key]
        self.del_N(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        mpp = self.mpp
        cap = self.cap

        if key in mpp:
            node = mpp[key]
            node.val = value
            self.del_N(node)
            self.insert(node)
        else:
            if len(mpp) == cap:
                lru = self.tail.prev
                self.del_N(lru)
                del mpp[lru.key]

            node = LL(key, value)
            mpp[key] = node
            self.insert(node)
