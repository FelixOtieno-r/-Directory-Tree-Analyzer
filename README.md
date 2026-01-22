# Directory Tree Analyzer

A beginner-friendly **Python tool** that analyzes any folder on your computer and shows you what's inside!

---

## Features
- **Recursive scanning** – Looks through folders and all their subfolders  
- **File & folder counts** – Shows total number of files and folders  
- **Size calculation** – Calculates total size of all files (KB, MB, GB)  
- **File type grouping** – Groups files by extension (.txt, .jpg, .py, etc.)  
- **Largest files** – Identifies the 5 largest files in the folder  
- **Error handling** – Gracefully handles permission errors and empty folders  
- **Simple interface** – Easy-to-use menu system  

---

## Requirements
- Python **3.6 or higher**
- No additional libraries required (uses only Python built-in modules)

---

## Installation

1. Download or copy the program code  
2. Open any text editor (Notepad, VS Code, TextEdit, etc.)  
3. Paste the code  
4. Save the file as:

```text
folder_analyzer.py
```

---

##  How to Run

### Windows
```cmd
cd C:\Users\YourName\Desktop
python folder_analyzer.py
```

### Mac / Linux
```bash
cd ~/Desktop
python3 folder_analyzer.py
```

---

##  How to Use

When the program starts, you’ll see:

```text
==================================================
 DIRECTORY TREE ANALYZER
==================================================

Enter the folder path you want to analyze:
  • Type '.' for current folder
  • Type '..' for parent folder
  • Or type any folder path like '/Users/name/Documents'

Or type 'quit' to exit
==================================================
```

### Examples

| You Type | What It Does |
|--------|--------------|
| `.` | Analyze current folder |
| `..` | Analyze parent folder |
| `~/Desktop` | Analyze Desktop (Mac/Linux) |
| `C:\Users\Name\Downloads` | Analyze Downloads (Windows) |
| `/` | Analyze entire computer ( slow) |

---

## Sample Output

```text
Total files found: 124
Total folders found: 8
Total size: 45.67 MB
```

---

##  What You'll Learn
- `os.walk()` for directory traversal  
- File size and metadata handling  
- Dictionaries for grouping data  
- Error handling with `try/except`  
- Building interactive CLI programs  

---

## Troubleshooting

**Python not recognized**
- Windows: Install Python from python.org
- Mac/Linux: Use `python3`

**Permission errors**
- Analyze folders you own (Documents, Downloads)

**Windows paths**
- Use:
```
C:/Users/Name/Desktop
C:\\Users\\Name\\Desktop
```

---

## Project Ideas
- Find duplicate files  
- Sort files by date  
- Count only images  
- Export results to CSV  

---

## File Structure

```text
folder_analyzer.py
any_folder/
 ├── documents/
 ├── images/
 └── code/
```

---

## License
Educational use – free to use, modify, and share.

---


