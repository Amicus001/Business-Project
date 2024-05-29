from flask import redirect, flash, Blueprint, render_template, request, jsonify,url_for, send_file
import cv2
import shutil
import os
import sys


# detect.py 파일이 있는 디렉토리 경로
# c:\Users\kdp\KDT-5\wk_Project\WEB
root_dir = os.path.dirname(os.path.dirname(__file__))


detect_dir = os.path.join(root_dir, 'static', 'model', 'yolov5')

# sys.path에 detect.py가 있는 디렉토리 경로를 추가
sys.path.append(detect_dir)

# 이제 detect.py를 import 할 수 있음
from detect import *



#bp instance
databp = Blueprint(name='DATA',
                   import_name= __name__,
                   static_folder= 'templates',
                   url_prefix='/input')


# 라우팅
@databp.route('/') #http://127.0.0.1:5000/input
def input_data():
    return  render_template('input.html')



@databp.route('/upload/', methods=['POST'])
def upload_file():

    # 저장할 디렉토리
    upload_directory = os.path.join(root_dir, 'static', 'upload')
    if not os.path.exists(upload_directory):
        os.makedirs(upload_directory)

    if 'file' not in request.files:
        flash('파일 부분이 없습니다')
        return render_template('input.html')
    
    file = request.files['file']
    if file.filename == '':
        flash('선택된 파일이 없습니다')
        return render_template('input.html')
    
    if file and allowed_file(file.filename):
        # 업로드된 파일의 이름을 유지하고 지정된 디렉토리에 저장
        file_path = os.path.join(upload_directory, 'upload_vedio.mp4')
        # 파일 존재하면 삭제
        if os.path.exists(file_path):
            os.remove(file_path)
            
        file.save(file_path)

        # YOLO 모델 실행 및 결과 파일 경로 가져오기
        result_path = run_yolo_detection(file_path)
        
        # 결과 파일 경로를 URL에 인코딩하여 리다이렉트
        return redirect(url_for('output', result=result_path))
    else:
        flash('mp4 파일만 허용됩니다')
        return render_template('input.html')

# mp4 형식만 허용하는 함수
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'mp4'}

# YOLO 모델 실행
def run_yolo_detection(file_path):
    name = 'de_id'

    download_directory = os.path.join(root_dir, 'static', 'download')
    if not os.path.exists(download_directory):
        os.makedirs(download_directory)

    # YOLOv5 모델 실행
    run(
        weights=os.path.join(root_dir, 'static', 'model', 'yolov5', 'runs', 'train', 'face_16k', 'weights', 'best.pt'),
        source=file_path,
        hide_conf=True,
        hide_labels=True,
        line_thickness=0,
        mosaic_type=4,
        name=name,
        conf_thres=0.5,
    )

    # 결과 파일 경로 반환
    result_filename = f"{name}.mp4"
    result_path = os.path.join(download_directory, result_filename)
    return result_path


@databp.route('/output/', methods=['GET'])
def output():
    result_path = request.args.get('result')

    if result_path:
        # 결과 동영상 파일을 다운로드할 수 있도록 함
        return render_template('output.html', result=result_url)
    else:
        return  flash('결과를 찾을 수 없습니다')







