# VS Code Automation Script

🚀 **Automate the opening of VS Code, launching the terminal, and running commands automatically.**

## 📌 Features
- ✅ Opens VS Code with a specified folder.
- ✅ Launches the integrated terminal automatically (`Ctrl + \``).
- ✅ Runs a predefined command in the terminal.
- ✅ Can be scheduled to execute at a specific time.

## 🛠️ Requirements
- **Windows OS** (Tested on Windows 10/11)
- **Python 3.x** ([Download Python](https://www.python.org/downloads/))
- **VS Code Installed** ([Download VS Code](https://code.visualstudio.com/))
- **Git Installed** ([Download Git](https://git-scm.com/downloads))
- **Required Python Package:** `pyautogui`

## 📥 Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/VSCode-Automation.git
cd VSCode-Automation
```

### 2️⃣ Install Dependencies
```sh
pip install pyautogui
```

## ⚙️ Usage
### **1️⃣ Configure the Script**
Edit `script.py` and update these variables:
```python
VSCODE_PATH = r"C:\Path\To\VSCode.exe"  # Update with your VS Code path
FOLDER_PATH = r"C:\Path\To\Your\Project"  # Update with your project folder path
TARGET_TIME = "12:01"  # Set the desired execution time in HH:MM format (24-hour)
```

### **2️⃣ Run the Script**
```sh
python script.py
```

## ⏳ How It Works
1. Waits until the scheduled time.
2. Opens VS Code with the specified folder.
3. Focuses on the VS Code window.
4. Opens the integrated terminal (`Ctrl + \``).
5. Runs a predefined command in the terminal.

## 📝 Notes
- Ensure **VS Code is installed at the specified path**.
- The script can be customized to execute different commands.
- If the terminal does not open, try running the script as an administrator.

## 🤝 Contributing
1. **Fork** the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Added new feature"`).
4. Push to your branch (`git push origin feature-branch`).
5. Open a **Pull Request**.

## 📜 License
This project is licensed under the **MIT License**.

---
💡 *For any issues or improvements, feel free to contribute!* 🚀

