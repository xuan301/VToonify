from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

path = "./output/MUCLE-0611-MM/"

# 获取所有形如"./output/MUCLE-0611-MM/MUCLE-0611-MM_x_vtoonify_t.mp4"的文件路径
files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.mp4') and f.startswith('MUCLE-0611-MM_') and '_vtoonify_t' in f]

# 按文件名排序，保证按照文件名的先后顺序合并
files = sorted(files)

# 逐个导入视频剪辑并合并
clips = []
for idx, file in enumerate(files):
    clip = VideoFileClip(file)
    
    # 第一个剪辑将确定目标分辨率和帧速率
    if idx == 0:
        target_resolution = clip.size
        target_fps = clip.fps
    else:
        # 将剪辑的分辨率和帧速率设置为目标分辨率和帧速率
        clip = clip.resize(target_resolution)
        clip = clip.set_fps(target_fps)
    
    clips.append(clip)

final_clip = concatenate_videoclips(clips)

# 将输出文件保存在自动生成的文件名中
final_clip.write_videofile("MUCLE-0611-MM-cartoon.mp4")
