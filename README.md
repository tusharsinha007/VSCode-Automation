# VS Code Automation Script

🚀 **Automate the opening of VS Code, launching the terminal, and running commands automatically.**

## 📌 Features
- ✅ Opens VS Code with a specified folder.
- ✅ Launches the integrated terminal automatically (`Ctrl + \``).
- ✅ Runs a predefined command in the terminal.
- ✅ Can be scheduled to execute at a specific time using Task Scheduler.

## 🫠 Requirements
- **Windows OS** (Tested on Windows 10/11)
- **Python 3.x** ([Download Python](https://www.python.org/downloads/))
- **VS Code Installed** ([Download VS Code](https://code.visualstudio.com/))
- **Git Installed** ([Download Git](https://git-scm.com/downloads))
- **Required Python Package:** `pyautogui`

## 💞 Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/tusharsinha007/VSCode-Automation
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

---

## 📅 Scheduling the Script Using Task Scheduler
You can automate this script to run at a specific time daily using **Task Scheduler**:

### **1️⃣ Open Task Scheduler**
- Press `Win + R`, type `taskschd.msc`, and press **Enter**.

### **2️⃣ Create a New Task**
1. Click **Create Basic Task**.
2. Enter a **Name** and **Description**.
3. Click **Next** and select **Daily** (or your preferred frequency).
4. Set the **Start Time** and click **Next**.
5. Choose **Start a Program** and click **Next**.
6. In **Program/Script**, enter:
   ```sh
   python
   ```
7. In **Add arguments**, enter the path to `script.py`:
   ```sh
   "C:\Path\To\Your\Project\script.py"
   ```
8. Click **Finish**.

### **3️⃣ Verify the Task**
- Find your task in the list and **Run** it manually to test.
- If it works, it will now execute automatically at the scheduled time.

---

## 📝 Notes
- Ensure **VS Code is installed at the specified path**.
- The script can be customized to execute different commands.
- If the terminal does not open, try running the script as an administrator.

---

## 🤝 Contributing
1. **Fork** the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Added new feature"`).
4. Push to your branch (`git push origin feature-branch`).
5. Open a **Pull Request**.

---

## 🐟 License
This project is licensed under the **MIT License**.

---

💡 *For any issues or improvements, feel free to contribute!* 🚀

