import cv2
import numpy as np

# 读取图片
img = cv2.imread("D:\opencv-project\opencv-test\cv_img_1.jpg")

# 创建窗口
cv2.namedWindow("美化调整")

# 三个参数
light = 0      # 亮度
color = 100    # 色彩
clear = 0      # 清晰度

def update():
    result = img.copy()
    
    # 调亮度
    result = cv2.convertScaleAbs(result, beta=light)
    
    # 调色彩
    hsv = cv2.cvtColor(result, cv2.COLOR_BGR2HSV)
    hsv[:,:,1] = hsv[:,:,1] * (color/100.0)
    result = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    
    # 加清晰度
    if clear == 1:
        kernel = np.array([[0, -1, 0],
                          [-1, 5, -1],
                          [0, -1, 0]])
        result = cv2.filter2D(result, -1, kernel)
    
    cv2.imshow("美化调整", result)
    return result

# 创建滑块
cv2.createTrackbar("light", "美化调整", 50, 100, 
                   lambda v: [globals().__setitem__('light', v-50), update()])
cv2.createTrackbar("color", "美化调整", 100, 200,
                   lambda v: [globals().__setitem__('color', v), update()])
cv2.createTrackbar("clear ", "美化调整", 0, 1,
                   lambda v: [globals().__setitem__('clear', v), update()])

# 显示
update()

print("调整滑块，按任意键保存")
cv2.waitKey(0)

# 保存
final = update()
cv2.imwrite("调整后.jpg", final)
print("✅ 已保存")

cv2.destroyAllWindows()
