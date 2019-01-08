from PIL import Image, ImageDraw
import numpy as np
import random

w = {-5: (7, 7, 7), -4: (7, 7, 7), -3: (150, 165, 150), -2: (200, 165, 150), -1: (200, 190, 170), 0: (150, 165, 200),
     1: (7, 7, 7), 2: (31, 7, 7), 3: (47, 15, 7), 4: (87, 23, 7), 5: (103, 31, 7), 6: (119, 17, 7),
     7: (143, 39, 7), 8: (159, 47, 7), 9: (175, 63, 7), 10: (191, 71, 7), 11: (199, 71, 7),
     12: (233, 79, 7), 13: (223, 87, 7), 14: (223, 87, 7), 15: (215, 103, 15), 16: (207, 111, 15),
     17: (207, 119, 15), 18: (207, 127, 15), 19: (207, 135, 23), 20: (199, 135, 23), 21: (199, 143, 23),
     22: (199, 151, 23), 23: (191, 159, 31), 24: (191, 159, 31), 25: (191, 167, 39), 26: (191, 167, 39),
     27: (191, 175, 47), 28: (183, 175, 47), 29: (183, 183, 47), 30: (183, 183, 55), 31: (207, 207, 111),
     32: (223, 223, 159), 33: (239, 239, 199), 34: (255, 255, 255), }

arr_stat = np.ones((801, 402))
for i in range(800):
    for j in range(401):
        arr_stat[i, j - 1] = 34

image = Image.new("RGB", (801, 401))
image.save("img.png")
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()

arr_bool = np.ones(801)

for i in range(801):
    for j in range(1, 401):
        if arr_stat[i, j - 2] < 34 and j < 5:
            stat = arr_stat[i, j - 2] - random.randint(-1, 1)
        elif arr_stat[i, j - 2] < 34 and j < 30:
            stat = arr_stat[i, j - 2] - random.randint(0, 1)
            if stat < 17:
                stat = random.randint(18, 27)
        else:
            stat = arr_stat[i, j - 2] - random.randint(0, 1)
        if stat <= 1:
            stat = 1
            arr_bool[i] = j
        arr_stat[i, j - 1] = stat

for i in range(1, 800):
    for j in range(1, 400):
        stat = (arr_stat[i, j - 1] + arr_stat[i - 1, j] + arr_stat[i + 1, j] + arr_stat[i, j + 1]) // 4
        arr_stat[i, j] = stat

for i in range(width):
    for j in range(height):
        draw.point((i - 1, j - 1), w[int(arr_stat[i - 1, j - 1])])
        print(w[arr_stat[i, j]])
image.transpose(Image.ROTATE_180).save("img.png")
print(arr_stat)
