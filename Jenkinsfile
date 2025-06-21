pipeline {
    agent {
        docker {
            image 'python:3.9'
            args '-v /tmp:/tmp'
        }
    }

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'python -m pip install --upgrade pip'
                sh 'pip install -r requirements.txt pytest'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/ --junitxml=test-results.xml'
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }
    }

    post {
        always {
            echo 'Тестирование завершено.'
        }
    }
}