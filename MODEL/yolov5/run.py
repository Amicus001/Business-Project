from detect import *
import os, shutil

# weights = "runs/train/face_16k/weights/best.pt"
# weights = "runs/train/face_15k/weights/best.pt"
weights = "runs/train/face_39k/weights/best.pt"

# source = "../datasets/sample/KakaoTalk_20240521_112502845.png"
# source = "../datasets/gstar/"
# source = "../datasets/4k/PSY - 'That That (prod. & feat. SUGA of BTS)' MV.mp4"
source = 0

name = "exp"
# name = "exp1"
# name = "smaple_16k"
# name = "G-star_2023_39k"
# name = "4k_15k"

if os.path.exists("runs/detect/" + name):
    shutil.rmtree("runs/detect/" + name)

run(
    weights=weights,
    source=source,
    name=name,
    conf_thres=0.5,
    hide_conf=True,
    hide_labels=True,
    line_thickness=0,
    mosaic_type=4,
)
