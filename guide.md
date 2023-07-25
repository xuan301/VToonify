# VToonify 视频动画化手册
本代码须在linux环境下执行，windows环境下可能会出现一些问题，而且难以解决，处理视频最好不要超过5分钟

## 1. 安装环境
首先在命令行中进入VToonify项目目录：
> cd VToonify

然后安装项目所需的环境：
> conda env create -f ./environment/vtoonify_env.yaml

安装好以后进入环境：
> conda activate vtoonify_env

但是要注意，由于版本不兼容，原环境中安装的torch版本为1.7.0，而我们的3080显卡只支持更高版本，所以需要重新安装torch：
> pip install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html

此后需要重新安装的库可以参考文档最后的tips，由于每个人的系统环境各不相同，先尝试进入步骤2运行代码，按照程序提示哪些库的版本不对，再参照最后的tips重新安装。

## 2. 运行代码
### 2.1 添加CUDA_HOME
首先在命令行中执行以下代码：
> export CUDA_HOME=/usr/local/cuda

不执行这个代码大概率报错：
> RuntimeError: Error building extension 'fused': [1/2] :/usr/local/cuda-11.2/bin/nvcc  ...
/bin/sh: :/usr/local/cuda-11.2/bin/nvcc: 没有那个文件或目录
ninja: build stopped: subcommand failed.

### 2.2 运行代码
接下来就可以动画化视频了，在命令行执行：
> python style_transfer.py --content ./data/FBCLE-1027.mp4     --scale_image --backbone toonify        --ckpt ./checkpoint/vtoonify_t_cartoon/vtoonify.pt        --padding 300 300 600 600 --video

更改动画化的视频只需要更改```--content ./data/FBCLE-1027.mp4```中的视频路径即可

但是此时官方生成的视频（在output文件夹下，以```_vtoonify_t.mp4```结尾）有概率会无法用视频播放器打开，所以需要用ffmpeg重新编码一下


python style_transfer.py --content ./data/total_movies/FBCLS-0328.mp4     --scale_image --backbone toonify        --ckpt ./checkpoint/vtoonify_t_cartoon/vtoonify.pt        --padding 300 300 600 600 --video



### 2.3 重新编码得到最终视频
在combine_frame.py的第41行：
> video_path = './data/FBCLE-1027.mp4'

和第45行：
> os.system(f"ffmpeg -r {frame_rate} -i ./output/FBCLE-1027/result_%4d.jpg -vcodec libx264 -pix_fmt yuv420p ./output/FBCLE-1027-t.mp4")

将```FBCLE-1027```改为你的视频名字，然后在命令行执行：
> python combine_frame.py

这样就可以得到最终的视频了, 在output文件夹下，以```-t.mp4```结尾




## 3.Tips（如果需要的话）
### 安装dlib
安装 Anaconda 后，首先在命令行输入：
> anaconda search -t conda dlib

用来搜索可以使用的 dlib 版本；然后再输入：
> conda install -c https://conda.anaconda.org/conda-forge dlib

### 安装ninja
> pip install ninja

### 安装cmake
> sudo apt-get install cmake

