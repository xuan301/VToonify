import os
import subprocess
import logging

# 设置日志文件的路径和格式
logging.basicConfig(filename='run.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 指定待处理的文件夹路径
folder_path = './data/FUMU/'

# 指定输出文件夹路径
output_folder = './output/'

# 遍历文件夹中的所有视频文件
for file_name in os.listdir(folder_path):
    if file_name.startswith(('FU', 'MU')) and file_name.endswith('.mp4'):
        logging.info(f'Start processing {file_name}')
        print(f'Start processing {file_name}')
        output_file = file_name[:-4] + '-d.mp4'
        output_file_path = os.path.join(output_folder, output_file)
        if os.path.exists(output_file_path):
            logging.info(f'{file_name} has been processed before')
            print(f'{file_name} has been processed before')
        else:
            content_file_path = os.path.join(folder_path, file_name)
            try:
                # 运行style_transfer.py
                subprocess.check_call([
                    'python',
                    'style_transfer.py',
                    '--content',
                    content_file_path,
                    '--scale_image',
                    '--style_id',
                    '26',
                    '--style_degree',
                    '0.5',
                    '--ckpt',
                    './checkpoint/vtoonify_d_cartoon/vtoonify_s026_d0.5.pt',
                    '--padding',
                    '300',
                    '300',
                    '600',
                    '600',
                    '--video'
                ])
                # 运行combine_frame.py
                subprocess.check_call([
                    'python',
                    'combine_frame.py',
                    '--file_name',
                    file_name[:-4]
                ])
                print(f'{file_name} processed successfully')
                logging.info(f'{file_name} processed successfully')
            except subprocess.CalledProcessError as e:
                print(f'Error processing {file_name}: {str(e)}')
                logging.error(f'Error processing {file_name}: {str(e)}')
