# 데이터 저장 / 출력 관련 웹 페이지 라우팅 처리 블루프린트
# URL : /index   *prefix
#       /index/input
#       /index/completed

from flask import Blueprint, render_template, request


#bp instance
databp = Blueprint(name='DATA',
                   import_name= __name__,
                   static_folder= 'templates',
                   url_prefix='/input')


save_file_dir = '../static/model/data'
# routing functions

@databp.route('/') #http://127.0.0.1:5000/input
def input_data():
    return  render_template('input.html')

# 동영상 파일 업로드 처리
@databp.route('/upload/', methods = ['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        if f:
        #저장할 경로 + 파일명
            file_path = save_file_dir + f.filename
            f.save(file_path)
        # yolo 모델 호출
        yolo_res = run_yolo_model(file_path)
            

    # yolo 모델에 넣어서 예측값 반환
    
    

    return






