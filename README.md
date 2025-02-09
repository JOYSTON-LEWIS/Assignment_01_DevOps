# 📌 DevOps Assignment On Python

---

## 🔥 **<span style="color:red">NOTE: PLEASE CONSIDER Q1, Q2, Q4 AS THE 3 QUESTIONS SOLVED FOR THIS ASSIGNMENT. Q3 IS ALSO SOLVED AS A BONUS FROM MY SIDE JUST IN CASE.</span>**

---

## 📖 Overview
This repository contains solutions for a DevOps assignment, covering security, system monitoring, automation, and backup tasks using Python. The implemented solutions focus on writing optimized and efficient code while ensuring proper comments and error handling.

## ✅ Solved Questions

### 🚀 Q1: Password Strength Checker
A Python script to validate password strength based on the following criteria:
- Minimum length: 8 characters
- Must include both uppercase and lowercase letters
- Must contain at least one digit
- Must have at least one special character

#### 📌 Execution
Run the script and input a password to check its strength:
```bash
python strength_of_password.py
```

#### 📸 Output Screenshots

![Q1_Img_01](https://github.com/user-attachments/assets/7e8c84a5-fd77-4dc9-a9f0-cf956210c168)
![Q1_Img_02](https://github.com/user-attachments/assets/d2af0fc9-0b0f-4986-962e-502454e733b3)
![Q1_Img_03](https://github.com/user-attachments/assets/27236412-8e61-4544-8dd9-c32d37660144)
![Q1_Img_04](https://github.com/user-attachments/assets/78dffe74-3c30-4c61-8866-df10f47a924c)
![Q1_Img_05](https://github.com/user-attachments/assets/fc5777c0-2fab-44c6-afa6-69740e30e4cc)

---

### 🖥️ Q2: CPU Monitoring Script
A Python script that continuously monitors CPU usage and alerts when it exceeds a predefined threshold (80%).
- Uses the `psutil` library to fetch CPU usage.
- Runs indefinitely until manually stopped.
- Includes error handling for robustness.

#### 📌 Execution
```bash
python health_of_cpu.py
```

#### 📸 Output Screenshots

![Q2_Img_01](https://github.com/user-attachments/assets/a4fe53fd-fe90-41d6-aea5-68e69df008ac)
![Q2_Img_02](https://github.com/user-attachments/assets/f693223c-de08-4fb9-9cd4-b5415e5e5b1e)

---

### 🗄️ Q3 (Bonus): Configuration File Parser & JSON Storage
A Python script to:
- Parse a configuration file and extract key-value pairs.
- Store the extracted data as JSON in a database.
- Provide a GET request endpoint to retrieve configuration data.

#### 📌 Execution
```bash
python process_data_and_store.py
```

#### 📸 Output Screenshots

![Q3_Img_01](https://github.com/user-attachments/assets/a0542ecc-d8e1-4df4-9c6e-f7577a466418)
![Q3_Img_02](https://github.com/user-attachments/assets/78d670bd-910d-4e02-bff9-216aea7f1149)
![Q3_Img_03](https://github.com/user-attachments/assets/d980cb9e-508f-4330-bb60-07e1683576c5)
![Q3_Img_04](https://github.com/user-attachments/assets/b296ff78-b3af-4914-a628-59be0270d378)
![Q3_Img_05](https://github.com/user-attachments/assets/5f62d731-1e1a-4e7a-9c86-546060256ac1)
![Q3_Img_06](https://github.com/user-attachments/assets/fb739fd7-c973-4c84-abe1-f14d06b0f295)
![Q3_Img_07](https://github.com/user-attachments/assets/b13382cd-f033-4726-92e3-7f29d27dcd64)
![Q3_Img_08](https://github.com/user-attachments/assets/cc1c543c-8a2b-4cd0-bea5-73dc3e6689f6)

---

### 📂 Q4: File Backup Script
A Python script to back up files from a source directory to a destination directory:
- Ensures file uniqueness by appending timestamps if a file already exists.
- Gracefully handles errors when directories are missing.

#### 📌 Execution
```bash
python backup.py /path/to/source /path/to/destination
```

#### 📸 Output Screenshots

![Q4_Img_01](https://github.com/user-attachments/assets/fc5b7e63-dc74-4988-8ca9-416d5c8bbcc0)
![Q4_Img_02](https://github.com/user-attachments/assets/23c960db-b50b-44e3-8797-b126279ffb18)
![Q4_Img_03](https://github.com/user-attachments/assets/a64da1ae-cd84-4d9c-8886-de92f331bb04)
![Q4_Img_04](https://github.com/user-attachments/assets/883f449a-5de8-40f7-99fe-7a9dca22d185)
![Q4_Img_05](https://github.com/user-attachments/assets/99c933bf-849e-43cb-bb24-a359af02890e)
![Q4_Img_06](https://github.com/user-attachments/assets/773eee35-a827-48e9-9370-b5392defe996)
![Q4_Img_07](https://github.com/user-attachments/assets/416e9537-b6c0-4fd8-abc1-aabef755649e)
![Q4_Img_08](https://github.com/user-attachments/assets/e98fc407-6f84-4bba-8ebc-fab16307fd90)
![Q4_Img_09](https://github.com/user-attachments/assets/20bf075e-78d9-4c01-8d7c-1cbf0bfa7235)

---

## 🛠️ Requirements
Ensure you have the required dependencies installed:
```bash
pip install psutil flask pymongo configparser
```

## 📜 License
This project is licensed under the MIT License.

## 🤝 Contributing
Feel free to fork and improve the scripts! ⭐ If you find this project useful, please consider starring the repo—it really helps and supports my work! 😊

## 📧 Contact
For any queries, reach out via GitHub Issues.

---

🎯 **Thank you for reviewing this project! 🚀**


