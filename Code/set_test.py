from set import Set
import unittest

class SetTest(unittest.TestCase):

    def test_init_and_contains(self):
        s = Set()
        assert s.size == 0
        assert len(s) == 0
        elements = [4, 8, 2, 9, 6]
        other_set = Set(elements)
        assert other_set.size == 5
        assert len(other_set) == 5

    def test_contains_and_len(self):
        s = Set()
        assert s.size == 0
        assert len(s) == 0
        assert s.__contains__(2) == False
        s.add(2)
        s.add(4)
        assert s.size == 2
        assert len(s) == 2
        assert s.__contains__(2) == True
        assert s.__contains__(3) == False
        s.remove(2)
        assert s.size == 1
        assert len(s) == 1
        assert s.__contains__(2) == False
        assert s.__contains__(4) == True

    def test_add(self):
        s = Set([1, 3, 5, 9])
        assert s.size == 4
        assert len(s) == 4
        assert s.__contains__(5) == True
        assert s.__contains__(4) == False
        s.add(4)
        assert s.size == 5
        assert len(s) == 5
        assert s.__contains__(4) == True
        assert s.__contains__(6) == False
        assert s.__contains__('4') == False
        s.add('a')
        assert s.size == 6
        assert len(s) == 6
        assert s.__contains__('a') == True

    def test_remove(self):
        s = Set([3, 6, 8, 10, 'a', None, 'i', 2.5])
        assert s.size == 8
        assert len(s) == 8
        s.remove(8)
        assert s.size == 7
        assert len(s) == 7
        assert s.__contains__(8) == False 
        assert s.__contains__(None) == True
        assert s.__contains__(2.5) == True
        assert s.__contains__(7) == False
        s.remove('a')
        assert s.__contains__('a') == False
        assert s.size == 6
        assert len(s) == 6
        s.remove('None')
        s.remove(2.5)
        assert s.__contains__('None') == False
        assert s.__contains__(2.5) == False
        assert s.__contains__(3) == True
        assert s.size == 4
        assert len(s) == 4

    def test_union(self):
        a = Set([1, 2, 3, 4, 5])
        b = Set([4, 5, 6, 7, 8])

        a_union_b = a.union(b)

        assert a_union_b.__contains__(8) == True
        assert a_union_b.__contains__(2) == True
        assert a_union_b.__contains__(4) == True
        assert a_union_b.__contains__(0) == False
        assert a_union_b.__contains__(9) == False

    def test_intersection(self):
        a = Set([1, 2, 3, 4, 5])
        b = Set([4, 5, 6, 7, 8])

        a_intersection_b = a.intersection(b)

        assert a_intersection_b.__contains__(1) == False
        assert a_intersection_b.__contains__(8) == False
        assert a_intersection_b.__contains__(4) == True
        assert a_intersection_b.__contains__(5) == True

        a.add('a')
        b.add('a')
        a.add(2.5)

        a_intersection_b = a.intersection(b)

        assert a_intersection_b.__contains__('a') == True
        assert a_intersection_b.__contains__(2.5) == False

    def test_difference(self):
        a = Set([1, 2, 3, 4, 5])
        b = Set([4, 5, 6, 7, 8])

        a_difference_b = a.difference(b)

        assert a_difference_b.__contains__(4) == False
        assert a_difference_b.__contains__(5) == False
        assert a_difference_b.__contains__(1) == True
        assert a_difference_b.__contains__(2) == True

        b.remove(4)

        a_difference_b = a.difference(b)

        assert a_difference_b.__contains__(4) == True

    def test_is_subset(self):
        a = Set([1, 2, 3])
        b = Set([1, 2, 4, 5])

        assert a.is_subset(b) == False

        b.add(3)
        assert a.is_subset(b) == True
        a.remove(3)
        assert a.is_subset(b) == True
        a.add(3)
        a.add(4)
        a.add(5)
        assert a.is_subset(b) == True
        a.add('b')
        assert a.is_subset(b) == False













