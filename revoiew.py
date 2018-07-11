class A:
    def __init__(self,x):
        self.x = x

    def show(self):
            print(self.x)

class B(A):
    def show(self):
        print("aAAAAAAAAAAAAASDSD")

    def noshow(self):
        print("DICKS")

a = A('a')
b = B('b')

a.show()

b.show()


class _Node:
    """A node in a linked list.

    Note that this is considered a "private class", one
    which is only meant to be used in this module by the
    LinkedList class, but not by client code.

    === Attributes ===
    @type item: object
        The data stored in this node.
    @type next: _Node | None
        The next node in the list, or None if there are
        no more nodes in the list.
    """
    def __init__(self, item):
        """Initialize a new node storing <item>, with no next node.

        @type self: _Node
        @type item: object
        @rtype: None
        """
        self.item = item
        self.next = None  # Initially pointing to nothing


class LinkedList:
    """A linked list implementation of the List ADT.

    === Private Attributes ===
    @type first: _Node | None
       The first node in the list, or None if the list is empty.
    """

    def __init__(self, items):
        """Initialize a new linked list containing the given items.

        The first node in the linked list contains the first item
        in <items>.

        @type self: LinkedList
        @type items: list
        @rtype: None
        """
        if len(items) == 0:  # No items, and an empty list!
            self._first = None
        else:
            self._first = _Node(items[0])
            curr = self._first
            for item in items[1:]:
                curr.next = _Node(item)
                curr = curr.next


    def insert_second(self,item):
        if self._first is None:
            raise IndexError

        else:
            new_node = _Node(item)
            self._first.next = new_node

lst = LinkedList([1,2,3])
lst.insert_second(10)

print(lst._first.item)