class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def to_array(self):
        arr = []
        if self.head is None:
            return arr

        node = self.head
        while node:
            arr.append(node.data)
            node = node.next_node
        return arr

    def print_list(self):
        list_string = ''
        node = self.head
        if node is None:
            print('None')
            return
        while node:
            list_string += node.data + ' '
            node = node.next_node

        list_string += "None"
        print(list_string)

    def insert_front(self, data):
        if self.last_node is None:
            self.head = Node(data, None)
            self.last_node = self.head

        else:
            new_node = Node(data, self.head)
            self.head = new_node

    def insert_end(self, data):
        if self.head is None:
            self.insert_front(data)
            return

        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node

    def get_user(self, user_id):
        node = self.head
        while node:
            if node.data["id"] is int(user_id):
                return node.data
            node = node.next_node
        return node

