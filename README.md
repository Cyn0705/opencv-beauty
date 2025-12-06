# opencv-beauty
opencv美化图片
整体功能

这是一个图片美化工具，用OpenCV实现，通过滑块实时调整图片的亮度、色彩和清晰度。

---


1. 导入库

```python
import cv2        # OpenCV库，处理图像
import numpy as np # NumPy库，处理数组和数学运算
```

2. 读取图片

```python
img = cv2.imread("")  # 从文件读取图片

```

· img 是一个三维数组，包含图片的所有像素信息

3. 创建显示窗口

```python
cv2.namedWindow("美化调整")  # 创建一个名为"美化调整"的窗口
```

4. 定义三个调整参数

```python
light = 0      # 亮度：-50到50（通过滑块映射）
color = 100    # 色彩饱和度：0到200（100是原始效果）
clear = 0      # 清晰度：0=关闭，1=开启
```

5. 核心函数：update()

```python
def update():
    result = img.copy()  # 复制原图，避免修改原图
```

a) 调整亮度

```python
result = cv2.convertScaleAbs(result, beta=light)
```

· beta=light：light 控制亮度
· light > 0：图片变亮
· light < 0：图片变暗

b) 调整色彩饱和度

```python
hsv = cv2.cvtColor(result, cv2.COLOR_BGR2HSV)  # BGR转HSV颜色空间
hsv[:,:,1] = hsv[:,:,1] * (color/100.0)       # 调整饱和度通道
result = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR) # HSV转回BGR
```

· HSV颜色空间：H=色调，S=饱和度，V=亮度
· 调整第2个通道（:,:,1]）就是调整饱和度
· color=200：饱和度翻倍（颜色更鲜艳）
· color=50：饱和度减半（颜色更淡）

c) 调整清晰度（锐化）

```python
if clear == 1:
    kernel = np.array([[0, -1, 0],
                      [-1, 5, -1],
                      [0, -1, 0]])
    result = cv2.filter2D(result, -1, kernel)
```

· 这是一个锐化滤波器
· 中间像素权重5，周围像素-1
· 效果：增强边缘对比度，让图片更清晰

6. 创建滑块控制

```python
cv2.createTrackbar("亮度", "美化调整", 50, 100, 
                   lambda v: [globals().__setitem__('light', v-50), update()])
```

滑块说明：

· "亮度"：滑块显示的名称
· "美化调整"：滑块所在的窗口名
· 50：初始值
· 100：最大值
· 回调函数：滑块变化时执行

回调函数的解释：

```python
lambda v: [globals().__setitem__('light', v-50), update()]
```

· v：滑块当前值（0-100）
· v-50：映射到 -50~50
· globals().__setitem__('light', v-50)：更新全局变量 light
· update()：立即更新图片显示

7. 显示和保存


cv2.destroyAllWindows()  # 关闭所有窗口
```
