pipeline {
    agent {
        label 'local_2250'
    }

    environment {
        IMAGE_NAME = "demo_env"
        COMPOSE_DIR = "docker/demo_env"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Image') {
            steps {
                sh '''
                    pwd
                '''
            }
        }

        stage('Run Container') {
            steps {
                echo "IMAGE_NAME: ${IMAGE_NAME}"
            }
        }
    }

    post {
        success {
            echo '✅ Build & Run success'
        }
        failure {
            echo '❌ Pipeline failed'
        }
    }
}
