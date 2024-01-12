from list_person import *

name_1 = 'Family_1 01.02.1991'
name_2 = 'Family_2 05.06.1987'
name_3 = 'Family_3 07.11.1991'


def test_add_tail():
    # input
    lst = ListPerson()
    lst.add_tail(name_1)
    lst.add_tail(name_2)

    # output
    expect = ['Family_1 01.02.1991', 'Family_2 05.06.1987']
    actual = [lst.head.data, lst.head.next.data]

    assert expect == actual


def test_add_head():
    # input
    lst = ListPerson()
    lst.add_head(name_1)
    lst.add_head(name_2)

    # output
    expect = ['Family_2 05.06.1987', 'Family_1 01.02.1991']
    actual = [lst.head.data, lst.head.next.data]

    assert expect == actual


def test_add_index():
    # input
    lst_1 = ListPerson()
    lst_1.add_index(name_1, 0)
    lst_1.add_index(name_2, 1)
    lst_1.add_index(name_3, 2)

    lst_2 = ListPerson()
    lst_2.add_index(name_1, 4)

    # output
    expect_1 = ['Family_1 01.02.1991', 'Family_2 05.06.1987', 'Family_3 07.11.1991']
    expect_2 = 'Index out for the range'

    actual_1 = [lst_1.head.data, lst_1.head.next.data, lst_1.head.next.next.data]
    assert expect_1 == actual_1
    assert expect_2 == lst_2.add_index(name_1, 4)
