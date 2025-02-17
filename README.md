# 🎨 File Organizer Script

## 🌟 Overview
This Python script **automatically organizes files** in a specified directory by sorting them into folders based on their file extensions. It helps in decluttering your workspace and enhances productivity with a **well-structured** file system.

---

## 🔧 Requirements
### 🖥️ What You Need
✔️ **Python 3.x** installed on your system.  
✔️ Basic understanding of how to run Python scripts.  
✔️ A directory with files that need organizing.  

To check if Python is installed, run:
```bash
python --version
```

---

## 🚀 How It Works
1️⃣ The script prompts the user to **enter a directory path**.  
2️⃣ It scans the directory and lists all files.  
3️⃣ Each file is **categorized based on its extension**.  
4️⃣ A separate folder is **created for each file type** (if not already present).  
5️⃣ Files are **moved** into their respective folders.  
6️⃣ A **success message** is displayed upon completion.  

---

## 📥 Installation & Usage

### ▶️ **Run the Script**
```bash
python file_organizer.py
```

### 🏷️ **Enter the Directory Path**
Example:
```
Enter your path: C:\Users\YourName\Downloads
```

---

## 📂 Example

### **Before Running the Script:**
```
Downloads/
├── document.pdf
├── image.jpg
├── song.mp3
├── notes.txt
├── slides.pptx
```

### **After Running the Script:**
```
Downloads/
├── 📁 pdf/
│   └── document.pdf
├── 📁 jpg/
│   └── image.jpg
├── 📁 mp3/
│   └── song.mp3
├── 📁 txt/
│   └── notes.txt
├── 📁 pptx/
│   └── slides.pptx
```

---

