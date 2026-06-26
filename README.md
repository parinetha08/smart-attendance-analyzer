# 📊 Smart Attendance Analyzer

A web-based **Flask application** that helps students instantly analyze their attendance percentage, identify subjects with low attendance, and visualize attendance statistics through graphs.

## 🚀 Live Demo

> https://smart-attendance-analyzer.onrender.com

## 📌 Features

* 📚 Analyze attendance for multiple subjects
* 📈 Calculate attendance percentage automatically
* ⚠️ Identify subjects at risk due to low attendance
* 📊 Generate attendance bar charts using Matplotlib
* 🖥️ Simple and responsive web interface
* 📝 Instant attendance report for each subject

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS
* **Visualization:** Matplotlib
* **Deployment:** Render
* **Version Control:** Git & GitHub

## 📂 Project Structure

```text
Smart_Attendance_Analyzer/
│── app.py
│── attendance.py
│── main.py
│── Procfile
│── requirements.txt
│── utils.py
│ ├── static/
│ └── graph.png │
├── templates/ │
├── dynamic_form.html
│ ├── form.html
│ └── result.html
│ └── __pycache__/
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/smart-attendance-analyzer.git
```

Go to the project folder:

```bash
cd smart-attendance-analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

## 📷 Screenshots

Add screenshots in a folder named **screenshots**.

Example:

```
screenshots/
├── home.png
├── input-form.png
├── result.png
├── graph.png
```

Then display them like this:

### Home Page

![Home](screenshots/home.png)

### Attendance Input

![Input](screenshots/input-form.png)

### Analysis Result

![Result](screenshots/result.png)

### Attendance Graph

![Graph](screenshots/graph.png)

## 🎯 Future Improvements

* User authentication
* Attendance history
* PDF report generation
* Database integration
* Mobile-friendly UI

## 👩‍💻 Author

**Parinetha Vuppalapu**

GitHub: https://github.com/parinetha08
