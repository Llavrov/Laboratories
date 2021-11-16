def F(n):
    if n == -1:
        return 0
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n > 1:
        return F(n - 1) * F(n - 2) + F(n - 3)


print(F(6))


# import matplotlib.pyplot as plt
# import warnings; warnings.filterwarnings(action='once')
# import seaborn as sns
# import pylab as plt
# from matplotlib_venn import venn3, venn3_circles
# from matplotlib_venn import venn2, venn2_circles
# import numpy as np
#
#
#
# class math:
#
#     def __init__(self, list1 = [], list2 = []):
#         self.list1 = list1
#         self.list2 = list2
#     def summ(self):
#         self.result = []
#         result = self.list1.set.add(self.list2)
#         return result
#
#     def disg(self):
#         self.result = []
#         result = self.list1.set.disgard(self.list2)
#         return result
#
#     def setL(self):
#         self.result = []
#         result = self.list1.set(self.list2)
#         return result
#
#
# # Значения вычисления
# # ax = plt.subplots(figsize=(16,10), dpi= 80)
# # x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 17]
# # y = [1, 1, 2, 3, 3, 5, 5, 8, 9, 6, 9, 9, 11, 11, 17]
# # sns.stripplot(x, y, jitter=0.25, size=8, ax=ax, linewidth=0.5)
# # plt.show()
#
#
# # Значения множества
# index = set([0,1,2,3,4,5,8])
# values = set([5,7,3,4,6,9])
# values2 = set([5,6,3,1,2,0])
#
# # plt.subplots(2, 2)
# # figure, axes = plt.subplots(2, 2,)
# # venn2(subsets={'10': 1, '01': 0.5, '11': 1}, set_labels = ('A', 'B'), ax=axes[0][0])
# # venn2(subsets={'10': 1, '01': 1, '11': 1}, set_labels = ('A', 'B'), ax=axes[0][1])
# # # venn2_circles((1, 2, 3), ax=axes[0][1])
# # # venn3(subsets=(1, 1, 1, 1, 1, 1, 1), set_labels = ('A', 'B', 'C'), ax=axes[1][0])
# # # venn3_circles({'001': 10, '100': 20, '010': 21, '110': 13, '011': 14}, ax=axes[1][1])
# # plt.show()
#
# # venn3([index, values, values2], ('Set1', 'Set2', 'Set3'))
# # plt.show()
# index = [0,1,2,3,4]
# values = [5,7,3,4,6]
# plt.bar(index, values)
# plt.show()
#
# # if __name__ == '__main__':
# #     a = 1