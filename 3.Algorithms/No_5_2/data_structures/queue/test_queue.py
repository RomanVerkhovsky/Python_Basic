from queue import *


def test_enqueue():
    # input
    queue_1 = Queue()
    queue_1.enqueue(5)
    queue_1.enqueue(6)

    queue_2 = Queue()
    queue_2.enqueue(-7)

    queue_3 = Queue()
    queue_3.enqueue('h')

    # output
    expect_1 = 5
    expect_2 = -7
    expect_3 = 'h'

    actual_1 = queue_1.peek()
    actual_2 = queue_2.peek()
    actual_3 = queue_3.peek()

    assert expect_1 == actual_1
    assert expect_2 == actual_2
    assert expect_3 == actual_3


def test_dequeue():
    # input
    queue_1 = Queue()
    queue_1.enqueue(5)
    queue_1.enqueue(7)

    queue_2 = Queue()

    queue_3 = Queue()
    queue_3.enqueue(8)

    # output
    expect_1 = 5
    expect_2 = None
    expect_3 = 8

    actual_1 = queue_1.dequeue()
    actual_2 = queue_2.dequeue()
    actual_3 = queue_3.dequeue()

    assert expect_1 == actual_1
    assert expect_2 == actual_2
    assert expect_3 == actual_3


def test_peek():
    # input
    queue_1 = Queue()
    queue_1.enqueue(5)
    queue_1.enqueue(8)

    queue_2 = Queue()

    queue_3 = Queue()
    queue_3.enqueue(7)

    # output
    expect_1 = 5
    expect_2 = None
    expect_3 = 7

    actual_1 = queue_1.peek()
    actual_2 = queue_2.peek()
    actual_3 = queue_3.peek()

    assert expect_1 == actual_1
    assert expect_2 == actual_2
    assert expect_3 == actual_3


def test_is_empty():
    # input
    queue_1 = Queue()

    # output
    expect_1 = True
    actual_1 = queue_1.is_empty()

    assert expect_1 == actual_1
