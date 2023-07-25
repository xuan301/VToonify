import os
import subprocess

def find_files_with_extension(extension, folder):
    return [f for f in os.listdir(folder) if f.endswith(extension)]

def upload_to_azure(file_path, destination_url):
    # azcopy_command = f'azcopy copy "{file_path}" "{destination_url}" --overwrite=prompt --from-to=LocalBlob --blob-type Detect'
    azcopy_command = f'azcopy copy "{file_path}" "{destination_url}" --recursive=true --overwrite=prompt --from-to=LocalBlob --blob-type Detect'
    subprocess.run(azcopy_command, shell=True)

output_folder = 'output'
extension = '-d-d.mp4'
destination_url_template = 'https://australiav100data.blob.core.windows.net/liuwenxuan/FUMU/{filename}?sv=2021-10-04&se=2023-07-18T17%3A21%3A16Z&sr=c&sp=rwl&sig=EhDzSsSQR9Kua9jbyqDvApZP%2BRTlgjGBFnl3Vpticu4%3D'

files_to_upload = find_files_with_extension(extension, output_folder)

for file in files_to_upload:
    file_path = os.path.join(output_folder, file)
    destination_url = destination_url_template.format(filename=file)
    print(f'Uploading {file_path} to {destination_url}')
    upload_to_azure(file_path, destination_url)
    print(f'Uploaded {file_path} to {destination_url}')
