from stack import *


def test_push():
    # input
    stack_1 = Stack()
    stack_1.push(7)

    stack_2 = Stack()
    stack_2.push(7)
    stack_2.push(8)

    # output
    expect_1 = 7
    expect_2 = 8

    actual_1 = stack_1.peek()
    actual_2 = stack_2.peek()

    assert expect_1 == actual_1
    assert expect_2 == actual_2


def test_pop():
    # input
    stack_1 = Stack()
    stack_1.push(7)
    stack_1.push(8)

    stack_2 = Stack()

    # output
    expect_1 = 8, 7
    expect_2 = None

    actual_1 = stack_1.pop(), stack_1.pop()
    actual_2 = stack_2.pop()

    assert expect_1 == actual_1
    assert expect_2 == actual_2


def test_peek():
    stack_1 = Stack()
    stack_1.push(5)
    stack_1.push(8)

    stack_2 = Stack()

    # output
    expect_1 = 8, 8
    expect_2 = None

    actual_1 = stack_1.peek(), stack_1.peek()
    actual_2 = stack_2.peek()

    assert expect_1 == actual_1
    assert expect_2 == actual_2


def test_is_empty():
    # input
    stack_1 = Stack()

    # output
    expect_1 = True
    actual_1 = stack_1.is_empty()

    assert expect_1 == actual_1
