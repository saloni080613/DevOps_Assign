pipeline {
    agent any

    environment {
        IMAGE_NAME = "apsit-sample-app"
        CONTAINER_NAME = "apsit-sample-app-container"
        PORT = "5000"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code from GitHub...'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker Image...'
                bat "docker build -t %IMAGE_NAME%:%BUILD_NUMBER% -t %IMAGE_NAME%:latest ."
            }
        }

        stage('Clean Previous Container') {
            steps {
                echo 'Stopping and removing existing container if present...'
                bat """
                docker stop %CONTAINER_NAME% 2>nul || exit 0
                docker rm -f %CONTAINER_NAME% 2>nul || exit 0
                """
            }
        }

        stage('Deploy Container') {
            steps {
                echo 'Running Docker container on host port %PORT%...'
                bat "docker run -d -p %PORT%:5000 --name %CONTAINER_NAME% %IMAGE_NAME%:latest"
            }
        }

        stage('Verify Deployment') {
            steps {
                echo 'Waiting for application to warm up...'
                sleep time: 4, unit: 'SECONDS'
                echo 'Verifying application response...'
                bat "curl -f -s http://localhost:%PORT%/health"
            }
        }
    }

    post {
        success {
            echo "CI/CD Pipeline executed and application deployed successfully!"
        }
        failure {
            echo "Pipeline failed. Check stage console outputs."
        }
        always {
            cleanWs()
        }
    }
}
