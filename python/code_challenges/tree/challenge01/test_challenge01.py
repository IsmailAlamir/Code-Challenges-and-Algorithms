import pytest
from challenge01 import *


@pytest.fixture
def tree1():
    tree1=Tree()
    root=tree1.Construct_Tree([3,9,20,15,7],[9,3,15,20,7])
    return tree1.__str__(root)

@pytest.fixture
def tree2():
    tree2=Tree()
    root=tree2.Construct_Tree([-1],[-1])
    return tree2.__str__(root)

@pytest.fixture
def tree3():
    tree3=Tree()
    root=tree3.Construct_Tree([],[])
    return tree3.__str__(root)

@pytest.fixture
def tree4():
    tree4=Tree()
    root=tree4.Construct_Tree([1,2,3,4,5,6],[6,5,4,3,2,1])
    return tree4.__str__(root)

@pytest.fixture
def tree5():
    tree5=Tree()
    root=tree5.Construct_Tree([1,2,3,4,5,6],[6,5,4,2,1])
    return tree5.__str__(root)




def test_Construct_Tree1(tree1):
    actual = tree1
    expected ="3 ,9 ,20 ,15 ,7 ,"
    assert actual == expected
    
def test_Construct_Tree2(tree2):
    actual = tree2
    expected = "-1 ,"
    assert actual == expected

    
def test_Construct_Tree_empty(tree3):
    actual = tree3
    expected = ""
    assert actual == expected
    
def test_Construct_Tree_unbalance(tree4):
    actual = tree4
    expected = "1 ,2 ,3 ,4 ,5 ,6 ,"
    assert actual == expected

def test_Construct_Tree_not_equle_len(tree5):
    actual = tree5
    expected =""
    assert actual == expected