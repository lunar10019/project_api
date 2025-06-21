pipeline {
    agent any

    environment {
        PYTHON = 'python3'
        ALLURE = 'allure'
    }

    stages {
        stage('Получение кода') {
            steps {
                checkout scm
            }
        }

        stage('Установка зависимостей') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Запуск тестов') {
            steps {
                sh 'pytest tests/'
            }
            post {
                always {
                    allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
                    archiveArtifacts artifacts: 'report.html', fingerprint: true
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}