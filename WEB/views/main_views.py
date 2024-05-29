from flask import redirect, flash, Blueprint, render_template, request, jsonify,url_for, send_file
import cv2
import shutil
import os
import sys
from flask import Flask, render_template, send_file
import subprocess

# detect.py 파일이 있는 디렉토리 경로
# c:\Users\kdp\KDT-5\wk_Project\WEB
root_dir = os.path.dirname(os.path.dirname(__file__))


detect_dir = os.path.join(root_dir, 'static', 'model', 'yolov5')

# sys.path에 detect.py가 있는 디렉토리 경로를 추가
sys.path.append(detect_dir)

# 이제 detect.py를 import 할 수 있음
from detect import *



# #bp instance
databp = Blueprint(name='DATA',
                   import_name= __name__,
                   static_folder= 'templates',
                   url_prefix='/input')

# upload 폴더, download 폴더 삭제
upload_directory = os.path.join(root_dir, 'static', 'upload')
download_directory = os.path.join(root_dir, 'static', 'download')
if os.path.exists(upload_directory):
    shutil.rmtree(upload_directory)
if os.path.exists(download_directory):
    shutil.rmtree(download_directory)

# 라우팅
@databp.route('/') #http://127.0.0.1:5000/input
def input_data():
    return  render_template('input.html')


@databp.route('/upload/loading/')
def loading():
    return render_template('loading.html')


@databp.route('/upload/', methods=['POST'])
def upload_file():

    # 저장할 디렉토리
    upload_directory = os.path.join(root_dir, 'static', 'upload')
    
    # 디렉토리 다시 생성
    os.makedirs(upload_directory)
    
    file = request.files['file']
    file_path = os.path.join(upload_directory, 'video.mp4')

    file.save(file_path)
    # YOLO 모델 실행 및 결과 파일 경로 가져오기
    result_path = run_yolo_detection(file_path) 
    # 결과 파일 경로를 URL에 인코딩하여 리다이렉트
    return redirect(url_for('DATA.output', result=result_path))

# 비디오 인코딩  
def encode_video(input_path, output_path):
    command = [
        'ffmpeg', '-y', '-i', input_path,
        '-c:v', 'libx264', '-c:a', 'aac', '-strict', 'experimental',
        output_path
    ]
    subprocess.run(command, check=True)

# YOLO 모델 실행
def run_yolo_detection(file_path):
    name = 'de_id'
    # YOLO 결과 파일 경로: 파일 존재하면 삭제
    download_directory = os.path.join(root_dir, 'static', 'model', 'yolov5', 'runs', 'detect', name)
    if os.path.exists(download_directory):
        shutil.rmtree(download_directory)

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

    save_path = os.path.join(root_dir, 'static', 'model', 'yolov5', 'runs', 'detect', name, 'video.mp4')

    # YOLO 결과 파일 경로
    download_path = os.path.join(root_dir, 'static', 'download', 'de_video.mp4')
    # download 폴더 생성
    os.makedirs(os.path.dirname(download_path), exist_ok=True)

    # 비식별화 비디오 인코딩
    encode_video(save_path, download_path)

    return download_path






@databp.route('/result/', methods=['GET'])
def output():
    result_path = request.args.get('result')
    if result_path and os.path.exists(result_path):
        # 파일 다운로드 링크를 생성하여 템플릿에 전달
        return render_template('result.html', result=result_path)
    else:
        flash('결과를 찾을 수 없습니다')
        return render_template('result.html', result=None)

@databp.route('/download/<path:filename>', methods=['GET'])
def download(filename):
    # 다운로드할 파일 경로
    file_path = os.path.join(root_dir, 'static', 'download', filename)
    # 파일 다운로드
    return send_file(file_path, as_attachment=True)



