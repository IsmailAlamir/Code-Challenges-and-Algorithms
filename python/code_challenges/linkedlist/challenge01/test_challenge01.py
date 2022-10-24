# Write your test here
import pytest
from challenge01 import *

@pytest.fixture
def linkedList1():
    linkedList1 = LinkedList()
    node1 = Node(4)
    node2 = Node(5)
    node3 = Node(1)
    node4 = Node(9)
    linkedList1.append(node1)
    linkedList1.append(node2)
    linkedList1.append(node3)
    linkedList1.append(node4)
    delete_node = delete(linkedList1.get(5))

    return delete_node

@pytest.fixture
def linkedList2():
    linkedList2 = LinkedList()
    node1 = Node(4)
    node2 = Node(5)
    node3 = Node(1)
    node4 = Node(9)
    linkedList2.append(node1)
    linkedList2.append(node2)
    linkedList2.append(node3)
    linkedList2.append(node4)
    delete_node=delete(linkedList2.get(1))

    return delete_node



def test_delete_1(linkedList1):
    actual = linkedList1
    expected = None
    assert actual == expected
    
def test_delete_1(linkedList2):
    actual = linkedList2
    expected = None
    assert actual == expected
    