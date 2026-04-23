# 🌊 SEA TRACKER  
> _“Track smarter. Discover faster. Stay invisible.”_

<p align="center">
  <img src="https://img.shields.io/badge/OSINT-Tool-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge">
</p>

---

## 🧠 What is Sea Tracker?

**Sea Tracker** is a lightweight OSINT tool built for fast reconnaissance and intelligence gathering directly from your terminal.

It allows you to extract valuable information about:

- 🌐 IP addresses  
- 📱 Phone numbers  
- 👤 Usernames across multiple platforms  
- 💻 Local system information  

All from a simple and interactive CLI interface.

---

## ⚡ Features

✔ IP Geolocation Tracking  
✔ Phone Number Intelligence  
✔ Username Enumeration (40+ platforms)  
✔ Local System Recon  
✔ Interactive Menu  
✔ Clean Colored Output  

---

## 🖥️ Interface Preview
<img width="1085" height="1368" alt="image" src="https://github.com/user-attachments/assets/3962670b-ec00-4983-be6c-6dd582bf33bb" />
<img width="1104" height="356" alt="image" src="https://github.com/user-attachments/assets/5dcc7ed2-a204-49e0-bd92-d60685b17cd2" />




---

## ⚙️ Requirements

Before running the tool, make sure you have:

- Python **3.8+**
- Linux environment (recommended)
- Internet connection

---

## 🐍 Virtual Environment Setup (IMPORTANT)

Using a virtual environment is **strongly recommended**.

### 1. Create environment

```bash
python3 -m venv venv
```

### 2. Activate it

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Dependencies

Required Python libraries:

- requests  
- phonenumbers  
- termcolor  

Manual installation (if needed):

```bash
pip install requests phonenumbers termcolor
```

---

## 🚀 Installation

### Option 1 – Manual

```bash
git clone https://github.com/sergiognzz/sea-tracker.git
cd sea-tracker
chmod +x sea_tracker.py
```

---

### Option 2 – System-wide installation

```bash
chmod +x install.sh
./install.sh
```

Run globally:

```bash
sea-tracker
```

---

## ▶️ Usage

### Basic command

```bash
python3 sea_tracker.py <target>
```

---

### Examples

```bash
python3 sea_tracker.py 8.8.8.8
python3 sea_tracker.py +34123456789
python3 sea_tracker.py <username>

sea-tracker 8.8.8.8
sea-tracker +34123456789
sea-tracker <username>

```

---

## 🖼️ Example Execution

<img width="797" height="406" alt="image" src="https://github.com/user-attachments/assets/8adccf46-30dd-4b88-82ec-4f9cd841f304" />


---

## 📋 Interactive Menu

```
1. Ip tracker
2. Phone tracker
3. User tracker
4. Show pc info
5. Insert target manually
6. Exit
```

<img width="1104" height="356" alt="image" src="https://github.com/user-attachments/assets/22d488f2-58d2-4329-bdba-88740b13c22d" />


---

## 🔎 Modules Breakdown

---

### 🌐 1. IP Tracker

Uses an external API to gather geolocation and network data.

**Output includes:**

- Country / City / Region  
- Coordinates (Latitude & Longitude)  
- ISP / Organization / ASN  
- Timezone info  
- Google Maps link  

<img width="1131" height="950" alt="image" src="https://github.com/user-attachments/assets/f12c8b2a-6139-40dc-b5e6-8669b5c50ba0" />


---

### 📱 2. Phone Tracker

Analyzes phone numbers using `phonenumbers`.

**Output includes:**

- Location / Region  
- Carrier (Operator)  
- Timezone  
- Valid / Possible status  
- Formats (International, E164, Local)  
- Number type (Mobile / Fixed)  

<img width="1176" height="773" alt="image" src="https://github.com/user-attachments/assets/b3c1ec39-f1f4-4ed7-a191-735346574a39" />


---

### 👤 3. User Tracker

Searches a username across multiple platforms.

**Platforms supported:**

- Facebook  
- Twitter  
- Instagram  
- GitHub  
- Reddit  
- TikTok  
- LinkedIn  
- YouTube  
- Twitch  
- Pinterest  
- And many more...

**Output:**

- ✅ Found → Profile URL  
- ❌ Not Found → "Not Found"  
- ⚠️ Error → Request issue  

<img width="863" height="1048" alt="image" src="https://github.com/user-attachments/assets/4e413278-8e6e-49cb-8439-3884d37af14c" />


---

### 💻 4. System Info

Displays local machine information via shell script.

**Includes:**

- Username  
- Hostname  
- OS & Kernel  
- Uptime  
- Local IP  
- Public IP  

<img width="1124" height="629" alt="image" src="https://github.com/user-attachments/assets/63a9fbf7-0196-412b-a917-c25c11d2f404" />


---

### 🎯 5. Insert Target Manually

Allows dynamic target input during execution.

Useful for:

- Switching targets quickly  
- Running multiple checks without restarting  

<img width="497" height="281" alt="image" src="https://github.com/user-attachments/assets/40eb7a18-bd85-4711-a218-f828108780e9" />


---

### ❌ 6. Exit

Closes the tool safely.

---

## 🧠 How It Works

1. You provide a target (IP, phone, or username)  
2. The tool identifies the type  
3. It runs the corresponding module  
4. Results are displayed in a structured format  

---

## 📁 Project Structure

```
sea-tracker/
│── sea_tracker.py
│── methods.py
│── requirements.txt
│── install.sh
│── animationStart.sh
│── seaTrackerInfo.sh
```

---

## ⚠️ Common Errors

### No target provided

```bash
python3 sea_tracker.py <target>
```

---

### Missing dependencies

```bash
pip install -r requirements.txt
```

---

### Permission issues

```bash
chmod +x sea_tracker.py
```

---

## ⚠️ Disclaimer

This tool is intended for:

✔ Educational purposes  
✔ Ethical OSINT investigations  

Do NOT use for:

❌ Harassment  
❌ Stalking  
❌ Illegal tracking  

You are fully responsible for your actions.

---

## 👨‍💻 Author

**Sergio González Sabucedo**

---

## ⭐ Contributing

Pull requests, improvements, and ideas are welcome.

---

## 📜 License

MIT License
