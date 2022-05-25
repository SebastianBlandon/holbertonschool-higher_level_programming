#!usr/bin/python3
""" This is the Node method class

    defines a node of a singly linked list
"""


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not type(value) is int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not (value is None or type(value) is Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


""" This is the class Singly Linked List

    defines a singly linked list
"""


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def __repr__(self):
        temp = self.__head
        str_out = ""
        while temp:
            str_out += "{:d}".format(temp.data)
            temp = temp.next_node
            if temp:
                str_out += "\n"
        return str_out

    def sorted_insert(self, value):
        if not self.__head:
            self.__head = Node(value)
        else:
            temp = self.__head
            prev = None
            while temp and temp.data < value:
                prev = temp
                temp = temp.next_node
            if not temp:
                prev.next_node = Node(value)
            elif temp is self.__head and not prev:
                self.__head = Node(value, temp)
            else:
                prev.next_node = Node(value, temp)
