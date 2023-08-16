
# Simple Automatic File Organizer

A Python script that automatically organizes your files into categorized directories based on their extensions. For example, `.mp3` files will be moved into the `Music` directory.

## Features:

- Categorizes files into:
  - Pictures
  - Music
  - Documents
  - Videos
  - Others
- Handles file name collisions by enumerating files.
- Option to include or exclude subdirectories.

## Installation

1. Clone this repository:
```
git clone https://github.com/BluEyeNick/Simple-Automatic-File-Organizer
```
2. Navigate to the repository's directory:
```
cd Simple-Automatic-File-Organizer
```

## Usage:

1. Update the `directories` list in the `main()` function of `main.py` with the paths you'd like to organize.

2. Set the `include_subdirs` flag to `True` if you want to organize all files including those in subdirectories. Set it to `False` if you want to organize only the top-level directory files.

3. Run the script:
```
python main.py
```

## Dependencies:

- Python (Tested with Python 3.8 and above)
- os, shutil, logging (All part of Python's standard library)

## License:

This project is licensed under the MIT License. For more details, see the `LICENSE` file in the repository.

---


