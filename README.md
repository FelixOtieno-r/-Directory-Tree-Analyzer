# -Directory-Tree-Analyze
A beginner-friendly Python tool that analyzes any folder on your computer and shows you what's inside!

Features
Recursive scanning - Looks through folders and all their subfolders

File & folder counts - Shows total number of files and folders

Size calculation - Calculates total size of all files (in KB, MB, GB)

File type grouping - Groups files by extension (.txt, .jpg, .py, etc.)

Largest files - Identifies the 5 largest files in the folder

Error handling - Gracefully handles permission errors and empty folders

Simple interface - Easy-to-use menu system

Requirements
Python 3.6 or higher (usually comes pre-installed on Mac/Linux)

No additional libraries needed - uses only Python's built-in modules

Installation
Download the program:

bash
# Copy the code from folder_analyzer.py
# Save it to your computer
Save as a Python file:

Open any text editor (Notepad, VS Code, TextEdit, etc.)

Copy and paste the code

Save as folder_analyzer.py

How to Run
Windows:
Open Command Prompt

Navigate to the folder where you saved the file:

cmd
cd C:\Users\YourName\Desktop
Run the program:

cmd
python folder_analyzer.py
Mac/Linux:
Open Terminal

Navigate to the folder where you saved the file:

bash
cd ~/Desktop
Run the program:

bash
python3 folder_analyzer.py
How to Use
When you run the program, you'll see a simple menu:


==================================================
  DIRECTORY TREE ANALYZER
==================================================

Enter the folder path you want to analyze:
  • Type '.' for current folder
  • Type '..' for parent folder
  • Or type any folder path like '/Users/name/Documents'

Or type 'quit' to exit
==================================================

Your choice: 
Try these examples:
You Type	What It Does
.	Analyzes the current folder
..	Analyzes the parent folder
~/Desktop	Analyzes your Desktop (Mac/Linux)
C:\Users\Name\Downloads	Analyzes Downloads (Windows)
/	Analyzes the entire computer (be careful - this might take a while!)
 Sample Output

==================================================
  DIRECTORY ANALYSIS RESULTS
==================================================

Folder analyzed: /Users/you/Desktop
Total files found: 124
Total folders found: 8
Total size: 45.67 MB

Files by type:
------------------------------
  .jpg                  →   45 files
  .txt                  →   32 files
  .pdf                  →   18 files
  .py                   →   12 files
  .docx                 →    8 files

   Top 5 Largest Files:
--------------------------------------------------
 1. 15.23 MB     → vacation_photo.jpg
 2. 8.45 MB      → report.pdf
 3. 5.12 MB      → data_backup.zip
 4. 3.78 MB      → presentation.pptx
 5. 2.91 MB      → movie_trailer.mp4

==================================================
   Analysis complete!
==================================================
 What You'll Learn
This project is perfect for learning:

os.walk() - How to navigate folder structures

File operations - Getting file sizes and information

Dictionaries - Counting and grouping data

Error handling - Dealing with permission errors gracefully

User input - Creating interactive command-line programs

Data formatting - Making output readable and user-friendly

 Troubleshooting
"Python is not recognized" error:
Windows: Install Python from python.org

Mac/Linux: Try python3 instead of python

Permission errors:
Try analyzing a folder you own (like Documents or Downloads)

The program will skip files it can't access and continue running

Empty folder results:
Make sure the folder exists and has files

Try using the full path instead of shortcuts

Windows path issues:
Use one of these formats:

C:\\Users\\Name\\Desktop (double backslashes)

C:/Users/Name/Desktop (forward slashes)

  Project Ideas for Learning
Try modifying the program to add new features:

Find duplicate files - Files with same name and size

Oldest/Newest files - Sort files by creation date

Image counter - Count only image files (.jpg, .png, .gif)

Size thresholds - Find files larger than a certain size

Export to CSV - Save results to a spreadsheet file

 File Structure

folder_analyzer.py        # Main program file
any_folder/              # Any folder you want to analyze
    ├── documents/
    │   ├── report.pdf
    │   └── notes.txt
    ├── images/
    │   ├── photo1.jpg
    │   └── photo2.png
    └── code/
        └── script.py
  Contributing
Found a bug or have an idea? Feel free to:

Modify the code for your needs

Share with classmates to compare folder structures

Add your own features and improvements
 Learning Resources
Python Official Documentation

Python os module tutorial

Command Line Basics

 Tips for Success
Start small - Analyze your Documents folder before trying your whole computer

Read the output - Understanding what each number means is part of learning

Experiment - Try different folders and see how the results change

Modify the code - Change the display format or add new features

Ask questions - If something doesn't make sense, look it up or ask for help!

License
This project is created for educational purposes. Feel free to use, modify, and share!
