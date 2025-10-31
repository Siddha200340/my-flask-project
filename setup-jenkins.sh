#!/bin/bash
# -----------------------------------------
# setup-jenkins.sh
# Automates Jenkins + Docker setup on Ubuntu EC2
# -----------------------------------------

echo "🚀 Updating system..."
sudo apt update -y
sudo apt upgrade -y

echo "🔧 Installing Java (required for Jenkins)..."
sudo apt install fontconfig openjdk-17-jre -y

echo "�� Adding Jenkins repository..."
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null

echo "📥 Installing Jenkins..."
sudo apt update -y
sudo apt install jenkins -y

echo "🐳 Installing Docker..."
sudo apt install docker.io -y
sudo systemctl enable docker
sudo systemctl start docker

echo "🧰 Adding Jenkins user to Docker group..."
sudo usermod -aG docker jenkins
sudo usermod -aG docker ubuntu

echo "🧱 Installing Git..."
sudo apt install git -y

echo "✅ Enabling and starting Jenkins..."
sudo systemctl enable jenkins
sudo systemctl start jenkins

echo "🔑 Fetching initial Jenkins admin password..."
sudo cat /var/lib/jenkins/secrets/initialAdminPassword

echo ""
echo "🎉 Jenkins setup complete!"
echo "👉 Access it at: http://<your-ec2-public-ip>:8080"
echo "Use the above password to unlock Jenkins."

