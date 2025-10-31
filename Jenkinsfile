 pipeline {
  agent any

  environment {
    DOCKERHUB_CRED = credentials('dockerhub-creds') // username/password pair
    SSH_CRED_ID = 'ec2-ssh-key'    // Jenkins credential of type SSH private key
    EC2_USER = 'ubuntu'
    EC2_HOST = '13.232.26.165'     // change to your EC2 public IP or DNS
    IMAGE_NAME = "yourdockerhubusername/flask-ci-cd-app"
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build Docker Image') {
      steps {
        script {
          def tag = "${IMAGE_NAME}:${env.BUILD_NUMBER}"
          sh "docker build -t ${tag} ./app"
          // also tag as latest
          sh "docker tag ${tag} ${IMAGE_NAME}:latest"
          env.IMAGE_TAG = tag
        }
      }
    }

    stage('Login & Push to Docker Hub') {
      steps {
        sh """
          echo ${DOCKERHUB_CRED_PSW} | docker login -u ${DOCKERHUB_CRED_USR} --password-stdin
          docker push ${IMAGE_TAG}
          docker push ${IMAGE_NAME}:latest
        """
      }
    }

    stage('Deploy to EC2') {
      steps {
        // Use ssh-agent plugin or the ssh-credentials plugin. This example uses an sh with ssh (private key from credentials)
        sshagent (credentials: [env.SSH_CRED_ID]) {
          sh """
            ssh -o StrictHostKeyChecking=no ${EC2_USER}@${EC2_HOST} \\
              'docker pull ${IMAGE_TAG} && docker stop app || true && docker rm app || true && docker run -d --name app -p 8000:8000 ${IMAGE_TAG}'
          """
          // reload nginx if necessary (if using different ports / upstream)
          sh "ssh ${EC2_USER}@${EC2_HOST} 'sudo systemctl restart nginx || true'"
        }
      }
    }
  }

  post {
    success {
      echo "Build and deploy successful: ${IMAGE_TAG}"
    }
    failure {
      echo "Build or deploy failed."
    }
  }
}
