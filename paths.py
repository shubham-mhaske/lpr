import os

YOLO_WEIGHT_PATH = os.getcwd()+'/model/yolov3.weights'
YOLO_CFG_PATH = os.getcwd()+'/model/yolov3.cfg'

LAPI_WEIGHT_PATH = os.getcwd()+'/model/lapi.weights'
LAPI_CFG_PATH = os.getcwd()+'/model/lapi.cfg'
LAPI_NAMES_PATH = os.getcwd()+'/model/lapi_class.names'

IMAGE_OUTPUT_DIR = os.getcwd()+'/op/img/'
VIDEO_OUTPUT_DIR = os.getcwd()+'/op/vid/'

TESSERACT_PATH = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

import random

random.seed(2)
RANDOM = str(random.random())



# Database paths
MASTER_DB_PATH = 'db/master.db'