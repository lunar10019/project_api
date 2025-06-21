pipeline {
    agent any

    environment {
        PYTHON = 'python3'
        ALLURE = 'allure'
    }

    stages {
        stage('Setup') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/test_httpbin_api.py -v --alluredir=allure-results --html=report.html --self-contained-html'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}