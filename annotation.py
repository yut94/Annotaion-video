import numpy as np
import cv2
import os

VIDEO_DIR = './data'
SAVE_PATH = './results/1.mp4'

bounding_boxes = [(246, 121, 368, 304)]
st = "Is this effect OK?"
(text_w, text_h), baseline = cv2.getTextSize(st, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)

for _, name in enumerate(os.listdir(VIDEO_DIR)):
    video_path = VIDEO_DIR+os.sep+name

    cap = cv2.VideoCapture(video_path)
    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    w, h = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    vid_writer = cv2.VideoWriter(SAVE_PATH, cv2.VideoWriter_fourcc(*'mp4v'), 30.0, (w, h))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            #draw
            for (start_x, start_y, end_x, end_y) in (bounding_boxes):
                cv2.rectangle(frame, (start_x-10, start_y - (2 * baseline + 5)), (start_x + 145, start_y), (0, 255, 255), -1)
                cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), (0, 255, 255), 2)
                cv2.putText(frame, st, (start_x-10, start_y), 1, 1, (0, 0, 0), 1)
            vid_writer.write(frame)
        else:
            break

    cap.release()
    vid_writer.release()
    cv2.destroyAllWindows()

    print(f'{name} done!')
print(f"Saved in {SAVE_PATH}")
