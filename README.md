# 🧩 My Flask Project

A simple Flask web application containerized with **Docker** and deployed using **Jenkins CI/CD** on an **EC2 instance**.  
This project demonstrates how to automate application deployment from GitHub to a running container on a cloud server.

---

## 🚀 Project Overview

The goal of this project is to:
- Build a lightweight Flask web app.
- Create a Docker image for the app.
- Automate the entire build–push–deploy process using Jenkins.
- Host the running container on an AWS EC2 instance.

---

## 🛠️ Tech Stack

| Component | Purpose |
|------------|----------|
| **Flask** | Web framework for building the application |
| **Gunicorn (WSGI)** | Runs the Flask app in production |
| **Docker** | Containerizes the application |
| **Jenkins** | Automates CI/CD pipeline |
| **AWS EC2** | Host environment for Jenkins and the app |
| **GitHub** | Source code repository |

---

## ⚙️ Project Structure

my-flask-project/
├── Jenkinsfile              # CI/CD pipeline definition
├── README.md
└── app/
    ├── Dockerfile           # Flask app Docker configuration
    ├── app.py               # Main application file
    ├── requirements.txt     # Python dependencies
    ├── templates/           # HTML templates
    ├── config.py            # Application configuration
    └── models.py            # Database models or app logic


---

## 🧰 How It Works

1. **Jenkins** pulls the source code from GitHub.
2. Builds a **Docker image** from the `Dockerfile`.
3. Tags and pushes the image to **Docker Hub**.
4. Deploys the latest image on the **EC2 instance** using `docker run`.
5. Application becomes accessible on port **8000**.

---

## 💡 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/Siddha200340/my-flask-project.git
cd my-flask-project/app

# Build Docker image
docker build -t flask-app .

# Run container
docker run -d -p 8000:8000 flask-app

# Access in browser
http://localhost:8000
