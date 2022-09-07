class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)


# How to create a linked list
llist1 = LinkedList()
print(llist1)

first_node = Node("a")
llist1.head = first_node
print(llist1)

second_node = Node("b")
third_node = Node("c")
first_node.next = second_node
second_node.next = third_node
print(llist1)

# How to traverse a linked list
llist2 = LinkedList(["a", "b", "c"])
print(llist2)

for node in llist2:
    print(node)

# How to insert a new node. Inserting at the beginning
llist2.add_first(Node("aa"))
print(llist2)

# How to insert a new node. Inserting at the end
llist2.add_last(Node("d"))
print(llist2)

# How to insert a new node. Inserting between two nodes
llist2.add_after("aa", Node("aaa"))
print(llist2)

# How to remove a node
llist2.remove_node("aa")
llist2.remove_node("aaa")
print(llist2)
