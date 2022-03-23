# -*- coding: utf-8 -*-
"""
author:tinsir888
"""
class MaxSubarraySum():
    """docstring here"""
    #初始化
    def __init__(self,array_numbers):
        self.array_numbers=array_numbers
    def max_subarray_sum_1d(self):
        """
        一维数组求最大子数组之和，算法的时间复杂度为 O(N)，采用动态规划算法
        递推公式是 d_p[j]=max{d_p[j-1]+array_numbers[j], array_numbers[j]}
        d_p[j] 指的是从0开始到j的最大子段和
        """
        array_numbers=self.array_numbers
        max_subarray_sum = array_numbers[0]
        tmp_sum = 0
        for cur_num in array_numbers:
            if tmp_sum < 0:
                tmp_sum = cur_num
            else:
                tmp_sum += cur_num
            max_subarray_sum = max(tmp_sum, max_subarray_sum)
        return max_subarray_sum
    def max_subarray_sum_2d(self,r_size,c_size):
        '''
        二维数组求最大子数组之和
        二位数字d_p[i][j]用来记录各位置的前缀和，
        d_p[i][j]+=d_p[i-1][j]+d_p[i][j-1]-d_p[i-1][j-1]
        创建变量Max用来记录所求的最大子矩阵和。即
        max_sum=max(max_sum,d_p[i][j]-d_p[i-x][j]-d_p[i][j-y]+d_p[i-x][i-y])
        对ijxy四个变量进行枚举，最终max_sum的值即所求最大子矩阵和。
        该方法时间复杂度为 O(m*m*n*n)，m和n分别为矩阵的长和宽。
        该算法可以被优化一下，用双重循环i j枚举行数，然后用一次线性时间复杂度
        计算从i到j行累加的数组的最大子数组和。
        最终时间复杂度为 O(m*n*n)，m和n分别为矩阵的长和宽。
        '''
        array_numbers=self.array_numbers
        # 生成一个全 0 的矩阵
        d_p=[[0]*c_size for i_0 in range(r_size)]
        if r_size<=0 or c_size<=0:
            print("Invalid input: r_size or c_size!")
            return 0
        # d_p 数组预处理
        for i_1 in range(r_size):
            for j_1 in range(c_size):
                d_p[i_1][j_1]=array_numbers[i_1][j_1]
                if i_1!=0:
                    d_p[i_1][j_1]+=d_p[i_1-1][j_1]
                if j_1!=0:
                    d_p[i_1][j_1]+=d_p[i_1][j_1-1]
                if i_1!=0 and j_1!=0:
                    d_p[i_1][j_1]-=d_p[i_1-1][j_1-1]
        #MaxSubarraySum=array_numbers[0][0]
        max_sum=int(-1e9)
        if c_size==1:# if column size is 1 do as 1D array.
            for i_2 in range(r_size):
                for j_2 in range(i_2,r_size):
                    if i_2==0:
                        temp = d_p[j_2][c_size-1]
                    else:
                        temp = d_p[j_2][c_size-1]-d_p[i_2-1][c_size-1]
                    max_sum=max(max_sum,temp)
        else:# if column size is greater than 1, deal as 2D array.
            for i_3 in range(r_size):
                for j_3 in range(i_3,r_size):
                    if i_3==0:
                        temp=d_p[j_3][c_size-1]-d_p[j_3][c_size-2]
                    else:
                        temp=d_p[j_3][c_size-1]-d_p[j_3][c_size-2]
                        temp=temp-d_p[i_3-1][c_size-1]+d_p[i_3-1][c_size-2]
    				#k=c_size-2
                    for k in range(c_size-2,-1,-1):
                        temp=max(temp,0)
                        temp+=d_p[j_3][k]
                        if i_3!=0:
                            temp-=d_p[i_3-1][k]
                        if k!=0:
                            temp-=d_p[j_3][k-1]
                        if i_3!=0 and k!=0:
                            temp+=d_p[i_3-1][k-1]
                        max_sum=max(max_sum,temp)
        return max_sum
if __name__ == '__main__':
    input_type=int(input('Please choose input as file: 1/ in console:2.\n'))
    #文件作为输入
    if input_type==1:
        arr_dimension=int(input('Please choose type of array to input: 1D array(1);2D array(2)\n'))
        if arr_dimension==1:
            input_file_path=input('Please input data file path:')
            with open(input_file_path, 'r') as input_file:
                array_input_as_string = input_file.read()
                array1D = [int(x) for x in array_input_as_string.split(' ')]
                assert len(array1D) < 100000 #异常处理
                L1=MaxSubarraySum(array1D)
                print('The max sum of 1D subarray is: ',L1.max_subarray_sum_1d())
        elif arr_dimension==2:
            input_file_path=input('Please input data file path:')
            input_file = open(input_file_path, 'r')
            array_2D_rows =input_file.readlines()
            array2D = []
            ARRAY_2D_ROWS_LEN=len(array_2D_rows)
            #print(ARRAY_2D_ROWS_LEN)
            for i_4 in range(ARRAY_2D_ROWS_LEN):
                column_list = array_2D_rows[i_4].strip().split(" ")
                #print(column_list)
                array2D.append(column_list)# 在末尾追加到list_source
            ARRAY_2D_COL_LEN=len(array2D[0])
            for i_5 in range(ARRAY_2D_ROWS_LEN):
                for j_4 in range(ARRAY_2D_COL_LEN):
                    array2D[i_5][j_4]=int(array2D[i_5][j_4])
                    #print(array2D[i_5][j_4])
            input_file.close()
            ROW_SIZE=int(len(array2D))
            column_size=int(len(array2D[0]))
            assert ROW_SIZE*column_size < 100000 #异常处理
            #print(array2D)
            L2=MaxSubarraySum(array2D)
            print('Maxsum of 2Dsubarray is:',L2.max_subarray_sum_2d(ROW_SIZE,column_size))
        else:
            print('Error input!\n')# 错误处理
    #控制台作为输入
    elif input_type==2:
        #print()
        e=int(input('Please choose type of array to test: 1D array(1); 2D array(2)\n'))
        if e==1:
            array_size=input('Please input size of 1D array:')
            readline_array = input("Please input {} elements' values:".format(array_size))
            assert array_size < 100000 #异常处理
            #输入一个一维数组，每个数之间使空格隔开
            num = [int(array_size) for array_size in readline_array.split()]
            #将输入每个数以空格键隔开做成数组
            L3=MaxSubarraySum(num)
            print('The maxsum of 1D subarray is: ',L3.max_subarray_sum_1d())
        elif e==2:
            nums = []
            rows = int(input("Please input number of rows:"))
            columns = int(input("Please input number of columns:"))
            assert rows*columns < 100000 #异常处理
            #print("请输入第{}个元素的值：".format(rows*columns))
            CUR_INPUT_NO=1
            for row in range(rows):
                nums.append([])
                #append精确插入一个元素，可以是元组也可以是序列。不可以超过一个或为空
                for column in range(columns):
                    num = int(input("Please input no.{} element value:".format(CUR_INPUT_NO)))
                    nums[row].append(num)
                    CUR_INPUT_NO=CUR_INPUT_NO+1
            #print(nums)
            L4=MaxSubarraySum(nums)
            print('The maxsum of 1D subarray is: ',L4.max_subarray_sum_2d(rows,columns))#打印二维数组
        else:
            print('Error input!\n')# 错误处理
    else:
        print('Error input!\n')# 错误处理
