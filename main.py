# This is a sample Python script.
import cv2
import cv2 as cv
import numpy as np

def read_img(name):
    img = cv.imread(name)
    if img is None:
        print(f"Error: Unable to open image '{name}'. Make sure the file exists.")
        return

    height, width, depth = img.shape
    ratio = img.shape[0] / 500.0
    origin = img.copy()
    img = cv.resize(img, (int(width / height * 500), 500))

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    bit = cv.bitwise_not(gray)
    amtImage = cv.adaptiveThreshold(bit, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 35, 25)

    blur = cv.GaussianBlur(gray, (5, 5), 0)

    param1 = 0
    param2 = 0
    max_param1 = 400
    max_param2 = 400
    increment = 20
    while param1 < max_param1:
        while param2 < max_param2:
            canny = cv.Canny(blur, 350, 400)
            contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

            if contours:
                largest_contour = max(contours, key=cv.contourArea)
                cv.drawContours(img, [largest_contour], -1, (255, 0, 0), 2)

                peri = cv2.arcLength(largest_contour, True)
                approx = cv2.approxPolyDP(largest_contour, 0.02 * peri, True)  # 进行多边形逼近，得到多边形的角点，并且轮廓应该封闭

                # 如果拟合的多边形角点为4，则可以认为是我们需要的外轮廓
                if len(approx) == 4:
                    screen_cnt = approx



    # cv.drawContours(img, contours, -1, (255, 0, 0), 1)
    cv.imshow('img', img)
    cv.imshow('canny', canny)
    cv.waitKey(0)  # Waits indefinitely until a key is pressed
    cv.destroyAllWindows()  # Destroys all the windows created

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_img("paper.jpg")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

