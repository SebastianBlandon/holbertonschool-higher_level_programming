#!/usr/bin/python3
"""
This is the "Single Linked List" module.

Class Node takes in integer values as data within each node,
and a next attribute which points to the next node or to None.

Class SinglyLinkedList initializes a default head of None.

Method sorted_insert handles all nodes created and adds them to
the linked list sorted by the int value stored within.
"""


class Node:
    """ Class Node with attributes:

    """
    def __init__(self, data, next_node=None):
        """ __init__ initializes attributes of class
            data (int): data of node
            next_node (Node): next_node of a Node

        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ data property to retrieve of the data

        """
        return self.__data

    @data.setter
    def data(self, value):
        """ data property setting of the data
            value (int): value to set

        """
        if not type(value) is int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ next_node property to retrieve the next_node

        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ next_node property to setting of the next_node
            value (Node): pointer of Node

        """
        if not (value is None or type(value) is Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


""" This is the class Singly Linked List

    defines a singly linked list
"""


class SinglyLinkedList:
    """ Class SinglyLinkedList

    """
    def __init__(self):
        """ __init__ initializes of attributes

        """
        self.__head = None

    def __repr__(self):
        """ __repr__ Returns a String with a representation of the state
        of the object and this String must be interpreted without errors
        by Python.

        """
        temp = self.__head
        str_out = ""
        while temp:
            str_out += "{:d}".format(temp.data)
            temp = temp.next_node
            if temp:
                str_out += "\n"
        return str_out

    def sorted_insert(self, value):
        """ sorted_insert insert the value in a new node

            value (int): value to insert in node

        """
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
