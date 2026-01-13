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
                dir("${COMPOSE_DIR}") {
                    sh '''
                        docker compose build
                    '''
                }
            }
        }

        stage('Run Container') {
            steps {
                dir("${COMPOSE_DIR}") {
                    sh '''
                        docker compose up -d
                    '''
                }
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
