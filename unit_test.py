import unittest
#from max_subarray_solve import max_subarray_sum_1d,max_subarray_sum_2d
from max_subarray_solve import MaxSubarraySum as test_obj_cls
class test_unit(unittest.TestCase):
    def test_normal_1d(self):
        num1 = [-2,  11, -4, 13, -5, -2]
        num2 = [1, 2, 3]
        num3 = [-1, -2]
        num4 = [1]
        m=test_obj_cls(num1)
        self.assertEqual(m.max_subarray_sum_1d(), 20)
        m=test_obj_cls(num2)
        self.assertEqual(m.max_subarray_sum_1d(), 6)
        m=test_obj_cls(num3)
        self.assertEqual(m.max_subarray_sum_1d(), -1)
        m=test_obj_cls(num4)
        self.assertEqual(m.max_subarray_sum_1d(), 1)
    def test_normal_2d(self):
        numbers1=[[1,2,-1,-4,-20],[-8,-3,4,2,1],[3,8,10,1,3],[-4,-1,1,7,-6],[-1,-2,-3,1,-4]]
        numbers2=[[1,1,1,1,1],[1,2,3,4,5],[5,4,2,1,3],[3,4,7,5,8],[3,5,9,6,1]]
        numbers3=[[0,0,0,0,0],[0,0,0,0,0],[-1,-1,-1,-1,-1],[-2,3,3,3,-2],[-3,3,3,3,-2]]
        numbers4=[[0,-1,-1,-2,-3],[-4,-5,-6,-7,-9],[-3,-4,-9,-6,-2],[-3,-4,-8,-3,-2],[-2,-5,-6,-7,-2]]
        numbers5=[[-1],[-1]]
        numbers6=[[-2,  11, -4, 13, -5, -2]]
        m=test_obj_cls(numbers1)
        self.assertEqual(m.max_subarray_sum_2d(5,5), 29)
        m=test_obj_cls(numbers2)
        self.assertEqual(m.max_subarray_sum_2d(5,5), 86)
        m=test_obj_cls(numbers3)
        self.assertEqual(m.max_subarray_sum_2d(5,5), 18)
        m=test_obj_cls(numbers4)
        self.assertEqual(m.max_subarray_sum_2d(5,5), 0)
        m=test_obj_cls(numbers5)
        self.assertEqual(m.max_subarray_sum_2d(2,1),-1)
        m=test_obj_cls(numbers6)
        self.assertEqual(m.max_subarray_sum_2d(1,6),20)
if __name__ == '__main__':
    unittest.main()