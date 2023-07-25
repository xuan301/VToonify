import cv2
import os
import re
import argparse

# 解析命令行参数
parser = argparse.ArgumentParser()
parser.add_argument('--file_name', type=str, required=True, help='视频文件名，不包含路径和后缀')
args = parser.parse_args()

# 构造视频文件路径和输出目录路径
# video_path = f"./data/liuwenxuan/90videos0411/{args.file_name}.mp4"
video_path = f"./data/FBMB/{args.file_name}.mp4"
output_dir = f"./output/{args.file_name}"

# 读取视频帧速率
def getFrameRate(video_path):
    video = cv2.VideoCapture(video_path)
    return int(video.get(cv2.CAP_PROP_FPS))

# 获取帧序列的数字序列
def getFrameNumber(frame_name):
    return int(re.findall(r'\d+', frame_name)[0])

# 合并帧为新视频
def mergeFramesToVideo(frame_folder, output_video_path, frame_rate):
    if not os.path.exists(frame_folder):
        print("目录不存在！")
        return
    frame_names = os.listdir(frame_folder)
    if len(frame_names) == 0:
        print("目录为空！")
        return
    # 按数字序列排序帧文件
    frame_names = sorted(frame_names, key=lambda name: getFrameNumber(name))
    frame_path = os.path.join(frame_folder, frame_names[0])
    frame = cv2.imread(frame_path)
    height, width, _ = frame.shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_video_path, fourcc, frame_rate, (width, height))
    for frame_name in frame_names:
        if not frame_name.endswith('.jpg'):
            continue
        frame_path = os.path.join(frame_folder, frame_name)
        frame = cv2.imread(frame_path)
        video_writer.write(frame)
        print(f"正在写入帧：{frame_name}")
    video_writer.release()

# 测试
if __name__ == '__main__':
    frame_rate = getFrameRate(video_path)
    print(f"帧速率：{frame_rate}")

    os.system(f"ffmpeg -r {frame_rate} -i {output_dir}/result_%4d.jpg -vcodec libx264 -pix_fmt yuv420p {output_dir}-d.mp4")

    # ffprobe -i FUCLE-1135-M-vtoonify.mp4 -show_streams -print_format json
