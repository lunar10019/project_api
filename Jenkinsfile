pipeline {
    agent any

    stages {
        stage('Установка зависимостей') {
            steps {
                sh 'git config --global --add safe.directory /var/jenkins_home/workspace/project_api_tests'
                sh 'python3 -m pip install -r requirements.txt --break-system-packages'
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
}



