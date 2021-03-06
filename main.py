import colorsys
import random
import time
import numpy as np
import sys

from openrazer.client import DeviceManager
from openrazer.client import constants as razer_constants

device_manager = DeviceManager()
device_manager.sync_effects = False

counter = 0
counter_limit = 100

def init_matrix():
    global matrix
    matrix = np.random.randint(2, size=(6, 22))

def parse_matrix():
    global matrix
    global counter

    counter += 1
    if counter >= counter_limit:
        counter = 0
        init_matrix()

    temp_matrix = np.copy(matrix)

    for x in range(0, 6):
        for y in range(0, 22):
            temp = 0

            try:
                temp += temp_matrix[x][y-1]
            except: pass

            try:
                temp += temp_matrix[x][y+1]
            except: pass

            try:
                temp += temp_matrix[x-1][y]
            except: pass

            try:
                temp += temp_matrix[x+1][y]
            except: pass

            try:
                temp += temp_matrix[x-1][y-1]
            except: pass

            try:
                temp += temp_matrix[x+1][y+1]
            except: pass

            try:
                temp += temp_matrix[x-1][y+1]
            except: pass

            try:
                temp += temp_matrix[x+1][y-1]
            except: pass

            if temp_matrix[x][y] == 1 and temp < 2 or temp > 3:
                matrix[x][y] = 0

            if temp_matrix[x][y] == 0 and temp == 3:
                matrix[x][y] = 1


def random_color():
    rgb = colorsys.hsv_to_rgb(random.uniform(0, 1), random.uniform(0.5, 1), 1)
    return tuple(map(lambda x: int(256 * x), rgb))

if __name__ == "__main__":

    init_matrix()

    if "reset" in sys.argv:
        for device in device_manager.devices:
            try:
                rows, cols = device.fx.advanced.rows, device.fx.advanced.cols

                for row in range(rows):
                    for col in range(cols):
                        cell = [200, 200, 200]
                        device.fx.advanced.matrix[row, col] = cell

                device.fx.advanced.draw()
            except:
                pass
        exit()

    while True:
        for device in device_manager.devices:
            try:
                rows, cols = device.fx.advanced.rows, device.fx.advanced.cols

                parse_matrix()

                for row in range(rows):
                    for col in range(cols):
                        if matrix[row][col] == 1:
                            cell = random_color()
                        else:
                            cell = [0, 0, 0]
                        device.fx.advanced.matrix[row, col] = cell

                device.fx.advanced.draw()
            except:
                pass
        time.sleep(0.075)
