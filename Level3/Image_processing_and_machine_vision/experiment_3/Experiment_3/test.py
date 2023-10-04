import numpy as np

# 假设 new_img 和 s 是 NumPy 数组
new_img = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

s = np.array([10, 20, 30])

# 使用 NumPy 的向量化操作更新 new_img，确保不越界
new_img = np.clip(s[new_img], 0, np.max(s))

print(new_img)
