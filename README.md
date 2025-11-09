# 🧩 My Flask Project — CI/CD Deployment on AWS EC2

A simple Flask web application containerized with **Docker** and deployed using **Jenkins CI/CD** on an **AWS EC2** instance.  
This project demonstrates a full end-to-end CI/CD pipeline automating code deployment from **GitHub → Jenkins → Docker → AWS**.

---

## 🚀 Project Goals
- Build a lightweight **Flask web application**.  
- Create a **Docker image** for containerized deployment.  
- Automate **build–push–deploy** workflow using Jenkins.  
- Host the running container on **AWS EC2**.

---

## 🛠️ Tech Stack

| Component | Purpose |
|------------|----------|
| **Flask** | Web framework for the application |
| **Gunicorn (WSGI)** | Production web server |
| **Docker** | Containerization tool |
| **Jenkins** | CI/CD automation |
| **AWS EC2** | Hosting environment |
| **GitHub** | Version control and source repository |

---

## ⚙️ Project Structure
my-flask-project/
├── Jenkinsfile # CI/CD pipeline definition
├── README.md
└── app/
├── Dockerfile # Flask app Docker configuration
├── app.py # Main application file
├── requirements.txt # Python dependencies
├── templates/ # HTML templates
├── config.py # App configuration
└── models.py # Database models / logic

---

## 🧰 How It Works
1. Jenkins pulls the source code from GitHub.
2. Builds a Docker image from the `Dockerfile`.
3. Tags and pushes the image to Docker Hub.
4. Deploys the latest image to EC2 using `docker run`.
5. Flask app becomes accessible at `http://<ec2-public-ip>:8000`.

---

## 💡 Run Locally
```bash
# Clone repository
git clone https://github.com/Siddha200340/my-flask-project.git
cd my-flask-project/app

# Build Docker image
docker build -t flask-app .

# Run container
docker run -d -p 8000:8000 flask-app

# Access in browser
http://localhost:8000
