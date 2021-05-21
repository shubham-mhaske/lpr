import os
from typing import re

from flask import Flask, render_template, request, Markup,url_for, redirect
import cv2

import Database
import paths
from Vehicle_detect import detect_img
import numpy as np
from paths import *
import Database as db
from PIL import Image

app = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static'

@app.route('/')
def index():
    return render_template('index.html',static_url_path='/static')

@app.route('/details')
def render_details():
        return render_template('details.html')

@app.route('/showhistory')
def render_history():
        return render_template('showhistory.html')

@app.route('/vehicleinfo', methods=['GET', 'POST'])
def render_vehicle_info():
    if request.method == 'POST':
        id = request.form['vehicle_id']
        Database.create_connection(MASTER_DB_PATH)
        img = Database.get_data(id)
        return render_template('viewinfo_image.html')
    return render_template('viewinfo.html')

@app.route('/addavehicle', methods=['GET', 'POST'])
def render_addavehicle():
    if request.method == 'POST':
        id = request.form['vehicleno']
        name = request.form['name']
        contact_no = request.form['contactno']
        address = request.form['address']

        #loaded image from temp dir
        image = Image.open('static/detected.png')
        blob_val = open('static/detected.png','rb').read()
        db.create_connection(paths.MASTER_DB_PATH)
        db.insert_data(id,name,contact_no,address,blob_val)
        db.close_db()

        #deleting unknown vehicle from temp dir after storing to db
        image.close()
        os.remove('static/detected.png')

    return render_template('addavehicle.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file1():
    return render_template('vehicle.html', type2='', tab="")

@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # read image file string data
        filestr = request.files['file'].read()
        # convert string data to numpy array
        npimg = np.fromstring(filestr, np.uint8)
        # convert numpy array to image
        img = cv2.imdecode(npimg, cv2.IMREAD_LOAD_GDAL)
        text, image = detect_img(image=img, cnt=0)
        #stat , msg = get_from_db(text)
        msg='<h1> Text from Image: '+text+'</h1>'

        if len(text)<1:
            #store the unknown vehivle to temp dir for using it to while storing to db
            cv2.imwrite('static/' + 'detected.png', image)
            return render_template('warningnew.html' ,static_url_path='/static')
        cv2.imwrite(IMAGE_OUTPUT_DIR+'detected_'+paths.RANDOM+'.jpg', image)
        return render_template('vehicle.html', type2='', tab=Markup(msg))

app.run()
