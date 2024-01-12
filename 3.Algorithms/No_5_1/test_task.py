from task import *


def test_near_target():
    # input
    array_1 = [1, 3, 5, 7, 9, 4]
    array_2 = [-1, -3, -5, -7, -9, -4]
    array_3 = [7, 7]
    array_4 = [2, 4, 6, 8, 10]

    target_1 = 3
    target_2 = -3
    target_3 = 7
    target_4 = 5

    # output
    expect_1 = 3
    expect_2 = -3
    expect_3 = 7
    expect_4 = 4 or 6

    actual_1 = near_target(array_1, target_1)
    actual_2 = near_target(array_2, target_2)
    actual_3 = near_target(array_3, target_3)
    actual_4 = near_target(array_4, target_4)

    assert actual_1 == expect_1, 'error array #1'
    assert actual_2 == expect_2, 'error array #2'
    assert actual_3 == expect_3, 'error array #3'
    assert actual_4 == expect_4, 'error array #4'


def test_num_original_words():
    # input
    text_1 = 'hello world hello universe'
    text_2 = ''
    text_3 = 'apple apple apple apple apple'

    # output
    expect_1 = 3
    expect_2 = 0
    expect_3 = 1

    actual_1 = num_original_words(text_1)
    actual_2 = num_original_words(text_2)
    actual_3 = num_original_words(text_3)

    assert actual_1 == expect_1, 'error text #1'
    assert actual_2 == expect_2, 'error text #2'
    assert actual_3 == expect_3, 'error text #3'


def test_count_customers():
    # input
    path_1 = 'list_customers_typical.txt'
    path_2 = 'list_customers_uncorrected.txt'
    path_3 = 'list_customers_boundary.txt'

    # output
    expect_1 = 1
    expect_2 = 0
    expect_3 = 0

    actual_1 = count_customer(path_1)
    actual_2 = count_customer(path_2)
    actual_3 = count_customer(path_3)

    assert actual_1 == expect_1, 'error text #1'
    assert actual_2 == expect_2, 'error text #2'
    assert actual_3 == expect_3, 'error text #3'
