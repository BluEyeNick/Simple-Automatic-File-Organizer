import os
import shutil
import logging

# Define file type categories
pictures = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.ico', '.jfif', '.webp', '.heif']
music = ['.mp3', '.wav', '.wma', '.flac', '.aac', '.ogg', '.aiff']
documents = ['.doc', '.docx', '.pdf', '.txt', '.xlsx', '.xls', '.ppt', '.pptx', '.odt', '.ods', '.odp', '.rtf', '.csv']
videos = ['.mp4', '.mov', '.wmv', '.flv', '.avi', '.mkv', '.webm', '.vob', '.ogv', '.drc', '.gifv', '.mng', '.qt', '.yuv', '.rm', '.rmvb', '.asf', '.amv', '.m4p', '.m4v', '.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.m2v', '.m4v', '.svi', '.3gp', '.3g2', '.mxf', '.roq', '.nsv']

def organize_files(directory, include_subdirs):
    try:
        # Loop over all files in the directory
        for foldername, subfolders, filenames in os.walk(directory):
            for filename in filenames:
                # Get file extension
                extension = os.path.splitext(filename)[-1].lower()

                # Determine the category of the file
                if extension in pictures:
                    category = 'Pictures'
                elif extension in music:
                    category = 'Music'
                elif extension in documents:
                    category = 'Documents'
                elif extension in videos:
                    category = 'Videos'
                else:
                    category = 'Others'

                # Determine source and destination paths
                source = os.path.join(foldername, filename)
                base_filename = os.path.splitext(filename)[0]
                destination = os.path.join(directory, category, filename)

                # If a file with the same name exists in the destination, enumerate the filename
                counter = 1
                while os.path.exists(destination):
                    destination = os.path.join(directory, category, f'{base_filename}({counter}){extension}')
                    counter += 1

                # Move the file
                shutil.move(source, destination)
                
                print(f'Moved file {source} to {destination}')
            
            # If not including subdirectories, break after the first loop
            if not include_subdirs:
                break
    except Exception as e:
        logging.error(f"Error while organizing files in directory {directory}: {str(e)}")

def main():
    # Setup logging
    logging.basicConfig(filename='file_organizer.log', level=logging.ERROR)

    # Define the directories and include_subdirs flag
    directories = ['/path/to/directory1', '/path/to/directory2']  # Update these paths
    include_subdirs = False  # Set this flag to True if you want to include all subdirectories
    
    # Organize files in each directory
    for directory in directories:
        directory = directory.strip()
        if os.path.isdir(directory):
            organize_files(directory, include_subdirs)
        else:
            print(f'Invalid directory: {directory}')
            logging.error(f'Invalid directory: {directory}')

if __name__ == "__main__":
    main()

