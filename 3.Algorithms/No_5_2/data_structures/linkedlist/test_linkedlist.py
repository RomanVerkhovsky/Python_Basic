from linkedlist import *


def test_is_empty():
    # input
    linkedlist_1 = LinkedList()
    linkedlist_1.add(1)

    linkedlist_2 = LinkedList()

    # output
    expect_1 = False
    expect_2 = True

    actual_1 = linkedlist_1.is_empty()
    actual_2 = linkedlist_2.is_empty()

    assert expect_1 == actual_1
    assert expect_2 == actual_2


def test_get_size():
    # input
    linkedlist_1 = LinkedList()
    linkedlist_1.add(5)

    linkedlist_2 = LinkedList()

    # output
    expect_1 = 1
    expect_2 = 0

    actual_1 = linkedlist_1.get_size()
    actual_2 = linkedlist_2.get_size()

    assert expect_1 == actual_1
    assert expect_2 == actual_2


def test_add():
    # input
    linkedlist_1 = LinkedList()
    linkedlist_1.add(1)

    linkedlist_2 = LinkedList()
    linkedlist_2.add('a')
    linkedlist_2.add(3)

    # output
    expect_1 = 1, 1
    expect_2 = 3, 2

    actual_1 = linkedlist_1.peek_index(0), linkedlist_1.get_size()
    actual_2 = linkedlist_2.peek_index(1), linkedlist_2.get_size()

    assert expect_1 == actual_1
    assert expect_2 == actual_2


def test_add_head():
    # input
    linkedlist_1 = LinkedList()
    linkedlist_1.add_head(1)

    linkedlist_2 = LinkedList()
    linkedlist_2.add_head(1)
    linkedlist_2.add_head('a')

    # output
    expect_1 = 1, 1
    expect_2 = 'a', 2

    actual_1 = linkedlist_1.peek_index(0), linkedlist_1.get_size()
    actual_2 = linkedlist_2.peek_index(0), linkedlist_2.get_size()

    assert expect_1 == actual_1
    assert expect_2 == actual_2


def test_insert():
    # input
    linkedlist_1 = LinkedList()
    linkedlist_1.insert(1, 0)

    linkedlist_2 = LinkedList()
    linkedlist_2.insert(1, 0)
    linkedlist_2.insert(2, 1)

    # output
    expect_1 = 1, 1
    expect_2 = 1, 2, 2

    actual_1 = linkedlist_1.peek_index(0), linkedlist_1.get_size()
    actual_2 = linkedlist_2.peek_index(0), linkedlist_2.peek_index(1), linkedlist_2.get_size()

    assert expect_1 == actual_1
    assert expect_2 == actual_2


def test_insert_value():
    # input
    linkedlist_1 = LinkedList()
    linkedlist_1.add(1)
    linkedlist_1.insert_value(2, 1)

    # output
    expect_1 = 1, 2, 2

    actual_1 = linkedlist_1.peek_index(0), linkedlist_1.peek_index(1), linkedlist_1.get_size()

    assert expect_1 == actual_1


def test_pop():
    # input
    linkedlist_1 = LinkedList()
    linkedlist_1.add(1)

    linkedlist_2 = LinkedList()
    linkedlist_2.add(1)
    linkedlist_2.add(2)

    # output
    expect_1 = 1, 0
    expect_2 = 2, 1, 0

    actual_1 = linkedlist_1.pop(), linkedlist_1.get_size()
    actual_2 = linkedlist_2.pop(), linkedlist_2.pop(), linkedlist_2.get_size()

    assert expect_1 == actual_1
    assert expect_2 == actual_2


def test_pop_head():
    # input
    linkedlist_1 = LinkedList()
    linkedlist_1.add(1)

    linkedlist_2 = LinkedList()
    linkedlist_2.add(1)
    linkedlist_2.add(2)

    # output
    expect_1 = 1, 0
    expect_2 = 1, 2, 0

    actual_1 = linkedlist_1.pop_head(), linkedlist_1.get_size()
    actual_2 = linkedlist_2.pop_head(), linkedlist_2.pop_head(), linkedlist_2.get_size()

    assert expect_1 == actual_1
    assert expect_2 == actual_2


def test_pop_index():
    # input
    linkedlist_1 = LinkedList()
    linkedlist_1.add(1)

    linkedlist_2 = LinkedList()
    linkedlist_2.add(1)
    linkedlist_2.add(2)

    # output
    expect_1 = 1, 0
    expect_2 = 1, 2, 0

    actual_1 = linkedlist_1.pop_index(0), linkedlist_1.get_size()
    actual_2 = linkedlist_2.pop_index(0), linkedlist_2.pop_index(0), linkedlist_2.get_size()

    assert expect_1 == actual_1
    assert expect_2 == actual_2


def test_pop_value():
    # input
    linkedlist_1 = LinkedList()
    linkedlist_1.add(1)

    linkedlist_2 = LinkedList()
    linkedlist_2.add(1)
    linkedlist_2.add(2)

    # output
    expect_1 = 1, 0
    expect_2 = 1, 2, 0

    actual_1 = linkedlist_1.pop_value(1), linkedlist_1.get_size()
    actual_2 = linkedlist_2.pop_value(1), linkedlist_2.pop_value(2), linkedlist_2.get_size()

    assert expect_1 == actual_1
    assert expect_2 == actual_2


def test_peek_index():
    # input
    linkedlist_1 = LinkedList()
    linkedlist_1.add(1)

    linkedlist_2 = LinkedList()
    linkedlist_2.add(1)
    linkedlist_2.add(2)

    # output
    expect_1 = 1, 1
    expect_2 = 1, 2, 2

    actual_1 = linkedlist_1.peek_index(0), linkedlist_1.get_size()
    actual_2 = linkedlist_2.peek_index(0), linkedlist_2.peek_index(1), linkedlist_2.get_size()

    assert expect_1 == actual_1
    assert expect_2 == actual_2
