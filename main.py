# This is a sample Python script.
import cv2
import cv2 as cv
import numpy as np


def transform_perspective(pts, img):
    # Calculate the suitable size of image with new perspective
    # reference https://zhuanlan.zhihu.com/p/627965231
    (tl, tr, br, bl) = pts
    width1 = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    width2 = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    max_width = max(int(width1), int(width2))

    height1 = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    height2 = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    max_height = max(int(height1), int(height2))

    pts2 = np.array([[0, 0], [max_width, 0], [max_width, max_height], [0, max_height]], dtype="float32")

    # Get the four corners of the image base on image's size
    pts1 = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    pts1[0] = pts[np.argmin(s)]
    pts1[2] = pts[np.argmax(s)]
    diff = np.diff(pts, axis=1)
    pts1[1] = pts[np.argmin(diff)]
    pts1[3] = pts[np.argmax(diff)]
    pts1 = np.float32(pts1)

    # Change perspective
    M = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(img, M, (max_width, max_height))
    cv2.imwrite('Scanned.jpg', dst)


def read_img(name):
    img = cv.imread(name)
    if img is None:
        print(f"Error: Unable to open image '{name}'. Make sure the file exists.")
        return

    origin_img = img.copy()

    height, width, depth = img.shape
    ratio = img.shape[0] / 500.0
    img = cv.resize(img, (int(width / height * 500), 500))

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5, 5), 0)

    # Tune the maxVal and minVal of canny function.
    param1 = 0
    param2 = 0
    max_param1 = 400
    max_param2 = 400
    increment = 20
    screen_cnt = None
    while param1 < max_param1:
        while param2 < max_param2:
            canny = cv.Canny(blur, param1, param2)
            contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

            if contours:
                largest_contour = max(contours, key=cv.contourArea)

                peri = cv2.arcLength(largest_contour, True)

                # Perform polygon approximation to obtain the corner points of the polygon,
                # and the contour should be closed
                approx = cv2.approxPolyDP(largest_contour, 0.02 * peri, True)

                # If the fitted polygon corner point is 4, it can be considered as the outer contour we need
                if len(approx) == 4:
                    screen_cnt = approx
                    cv.drawContours(img, [screen_cnt], -1, (255, 0, 0), 2)
                    break

            param2 += increment

            if screen_cnt:
                break
        param1 += increment

    # cv.drawContours(img, contours, -1, (255, 0, 0), 1)
    # cv.imshow('img', img)
    # cv.imshow('canny', canny)
    # cv.waitKey(0)  # Waits indefinitely until a key is pressed
    # cv.destroyAllWindows()  # Destroys all the windows created

    return screen_cnt, ratio, origin_img


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    screen_cnt, ratio, origin_img = read_img("paper.jpg")
    pts = screen_cnt.reshape(4, 2) * ratio
    transform_perspective(pts, origin_img)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

