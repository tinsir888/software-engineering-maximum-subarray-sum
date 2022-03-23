import profile

from max_subarray_solve import MaxSubarraySum as test_obj_cls
m=test_obj_cls([10,2,3,5,2,6,4,8,-11,-20,3,6,7,9,3,-79,7])
profile.run("m.max_subarray_sum_1d()")
m=test_obj_cls([[2,8,4,1,3],[-377,1,-1,-3,-6],[2,7,3,-68,2],[10,2,6,-20,-1],[-59,-2,6,-1,-6]])
profile.run("m.max_subarray_sum_2d(5,5)")