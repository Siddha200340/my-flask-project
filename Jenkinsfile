 pipeline {
  agent any

  environment {
    // DockerHub credentials (create in Jenkins → Credentials → Username & Password)
    DOCKERHUB_CRED = credentials('dockerhub-creds')

    // EC2 SSH key credential ID (create in Jenkins → SSH Username with private key)
    SSH_CRED_ID = 'ec2-ssh-key'

    // EC2 instance details
    EC2_USER = 'ubuntu'
    EC2_HOST = '13.235.80.235'

    // Docker image name (DockerHub repo)
    IMAGE_NAME = "siddha200340/my-flask-project-image"
  }

  stages {
    stage('Checkout') {
      steps {
        echo "Checking out source code..."
        checkout scm
      }
    }

    stage('Build Docker Image') {
      steps {
        script {
          def tag = "${IMAGE_NAME}:${env.BUILD_NUMBER}"
          echo "Building Docker image with tag: ${tag}"
          // since Dockerfile is inside 'app' folder
          sh "docker build -t ${tag} ./app"
          // also tag as latest
          sh "docker tag ${tag} ${IMAGE_NAME}:latest"
          env.IMAGE_TAG = tag
        }
      }
    }

    stage('Login & Push to Docker Hub') {
      steps {
        echo "Logging into DockerHub and pushing images..."
        sh """
          echo ${DOCKERHUB_CRED_PSW} | docker login -u ${DOCKERHUB_CRED_USR} --password-stdin
          docker push ${IMAGE_TAG}
          docker push ${IMAGE_NAME}:latest
        """
      }
    }

    stage('Deploy to EC2') {
      steps {
        echo "Deploying to EC2 instance..."
        sshagent (credentials: [env.SSH_CRED_ID]) {
          sh """
            ssh -o StrictHostKeyChecking=no ${EC2_USER}@${EC2_HOST} '
              sudo docker pull ${IMAGE_TAG} &&
              sudo docker stop flask-container || true &&
              sudo docker rm flask-container || true &&
              sudo docker run -d --name flask-container -p 8000:8000 ${IMAGE_TAG}
            '
          """
          echo "Deployment complete!"
        }
      }
    }
  }

  post {
    success {
      echo "✅ Build and deploy successful: ${IMAGE_TAG}"
    }
    failure {
      echo "❌ Build or deploy failed."
    }
  }
}
