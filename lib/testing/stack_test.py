import pytest
from Stack import Stack

class TestStack:
    def test_init(self):
        stk = Stack([1, 2, 3, 4, 5])
        assert stk.items == [1, 2, 3, 4, 5]

    def test_push(self):
        stk = Stack([1, 2, 3, 4, 5])
        stk.push(0)
        assert stk.items == [1, 2, 3, 4, 5, 0]

    def test_pop(self):
        stk = Stack([1, 2, 3, 4, 5])
        stk.pop()
        assert stk.items == [1, 2, 3, 4]

    def test_size(self):
        stk = Stack([1, 2, 3, 4, 5])
        assert stk.size() == 5

    def test_empty(self):
        stk = Stack()
        assert stk.isEmpty()
        assert stk.size() == 0
        with pytest.raises(IndexError):
            stk.pop()
        stk.push(1)
        assert not stk.isEmpty()
        assert stk.size() == 1
        assert stk.pop() == 1

    def test_full(self):
        stk = Stack([1], 1)
        assert stk.full()
        assert stk.size() == 1
        assert stk.pop() == 1
        stk.push(1)
        with pytest.raises(OverflowError):
            stk.push(2)

    def test_search(self):
        stk = Stack([5, 6, 7, 8, 9, 10])
        assert stk.search(5) == 5
        assert stk.search(6) == 4
        assert stk.search(7) == 3
        assert stk.search(8) == 2
        assert stk.search(9) == 1
        assert stk.search(10) == 0
        assert stk.search(15) == -1
