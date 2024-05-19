from captureImage import *
from main import *

def translate_image(number_of_pages):
  for i in range(number_of_pages):
    screen_cnt, ratio, origin_img = read_img(f"captured_image{i}.jpg")
    pts = screen_cnt.reshape(4, 2) * ratio
    transform_perspective(pts, origin_img, f"captured_image{i}_scanned")

translate_image(4)