
import os  
import shutil   
source_dir = input(r"Enter the source directory path : ").replace('\\', '/')   

dest_dir = input(r"Enter the destination directory path : ").replace('\\', '/')  
  

extension_map = {  
    '.jpg': 'Images',  
    '.png': 'Images',  
    '.gif': 'Images',  
    '.jpeg': 'Images',  
    '.pdf': 'PDF Files',  
    '.txt': 'Text Files',  
    '.docx': 'Word Document',  
    '.rtf': 'Word Document',  
    '.xlsx': 'Excel Files',
    '.csv': 'Excel Files',
    '.pptx': 'PowerPoint Presentations',  
    '.ppt': 'PowerPoint Presentations',  
    '.mp3': 'Audio',  
    '.wav': 'Audio',  
    '.mp4': 'Video',  
    '.avi': 'Video',  
    '.exe': 'Executable Files',  
    '.py': 'Python Files',  
    '.cpp': 'C++ Files',  
    '.c': 'C Files',  
    '.java': 'Java Files',  
    '.html': 'HTML Files',  
    '.css': 'CSS Files',  
    '.js': 'Javascript Files',  
    '.zip': 'Zip_Files'  
}  
  
 
for folder_name in set(extension_map.values()):  
    os.makedirs(os.path.join(dest_dir, folder_name), exist_ok=True)  
  
 
for filename in os.listdir(source_dir):  
  

    file_ext = os.path.splitext(filename)[-1].lower()  
  

    if file_ext in extension_map:  
  
        src_path = os.path.join(source_dir, filename)  
  
        dest_path = os.path.join(dest_dir, extension_map[file_ext], filename)  
  
        shutil.move(src_path, dest_path)  
