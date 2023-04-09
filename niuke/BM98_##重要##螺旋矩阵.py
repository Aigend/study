BM98_##重要##螺旋矩阵

描述
给定一个m x n大小的矩阵（m行，n列），按螺旋的顺序返回矩阵中的所有元素。

输入：
[[1,2,3],[4,5,6],[7,8,9]]
返回值：
[1,2,3,6,9,8,7,4,5]

输入：
[]
返回值：
[]

方向数组方法求解螺旋矩阵。

fx为方向数组，根据螺旋遍历的顺序进行定义
condition数组为根据数组边界定义的边界数组
总体循环次数为移动次数: m*n
使用影子变量x_, y_ 临时保存每次移动的结果，若超出condition数组则判定本次移动超出边界，需要进行掉头操作，回退并进行下一个方向的遍历，同时更新condition边界数组
方向改变每四次一次轮换， (dt+1) % 4

class Solution:
    def spiralOrder(self , matrix: List[List[int]]) -> List[int]:
        # write code here
        li = matrix
        if not li:
            return []
        m = len(li)
        n = len(li[0])
        if m == 1:
            return li[0]
        fx = [[0,1], [1,0], [0,-1],[-1,0]]
        condition = [0, n-1, m-1, 0]
        x, y, dt = 0, 0, 0
        ret = []
        for i in range(m*n):
            ret.append(li[x][y])
            x_, y_ = x + fx[dt][0], y + fx[dt][1]
            if x_ < condition[0] or x_ > condition[2] or y_ < condition[3] or y_ > condition[1]:
                if dt in (1,2):
                    condition[dt] -= 1
                else:
                    condition[dt] += 1
                dt = (dt+1) % 4
                x_, y_ = x + fx[dt][0], y + fx[dt][1]
            x, y = x_, y_
        return ret
             
