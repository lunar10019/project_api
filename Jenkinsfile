pipeline {
    agent {
        docker {
            image 'python:3.9'
            args '-u root'
        }
    }

    environment {
        PYTHON = 'python3'
        PIP = 'pip3'
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
                sh '${PIP} install --upgrade pip'
                sh '${PIP} install -r requirements.txt'
                sh '${PIP} install pytest allure-pytest'
            }
        }

        stage('Запуск тестов') {
            steps {
                sh '${PYTHON} -m pytest tests/ --alluredir=allure-results'
            }
            post {
                always {
                    allure([
                        includeProperties: false,
                        jdk: '',
                        results: [[path: 'allure-results']],
                        reportBuildPolicy: 'ALWAYS'
                    ])
                    archiveArtifacts(artifacts: 'allure-results/**', fingerprint: true)
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