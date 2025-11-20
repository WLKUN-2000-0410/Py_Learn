import numpy as np

data = [1, 2, 3, 4, 5] #长得就和矩阵一样
arr = np.array(data)
print(arr)

data_2d = [[1,2,3],[4,5,6]]
arr_2d = np.array(data_2d)
print(arr_2d)

print(arr_2d.shape)
print(arr_2d.size)
print(arr_2d.ndim)
print(arr_2d.dtype)

img = np.array([0,128,255],dtype=np.uint8)
print(img.dtype)

img_float = img.astype(np.float32)
print(img_float.dtype)

img_normalized = img_float / 255.0
print(img_normalized)

img_zeros = np.zeros((3,4),dtype=np.uint8)#因为是纯黑色,所以不用指定颜色
print(img_zeros)

img_ones = np.ones((3,4),dtype=np.uint8)#因为是纯白..
print(img_ones)

grey_img = np.full((3, 3), 66, dtype=np.uint8)#因为颜色自定义
print(grey_img)

noise_img = np.random.randint(0, 256, (3, 3), dtype=np.uint8)
print(noise_img)

arr = np.array([0,10,20,30,40,50])
print(arr[2])
print(arr[2:5])

img = np.array([[0,10,20],[30,40,50]]) #创建一个2x3的矩阵
print(img[0,1])
print(img[1,2]) #索引

crop = img[0:2,1:3] #取0-1行,1-2列
print(crop)

img_color = np.random.randint(0,255,(5,2,3))
print(img_color)
