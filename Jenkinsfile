pipeline {
    agent {
        docker {
            image 'python:3.9-slim'
            args '-v /tmp:/tmp'
        }
    }

    environment {
        PYTHON = 'python'
        PIP = 'pip'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Dependencies') {
            steps {
                sh '${PYTHON} --version'
                sh '${PIP} --version'
                sh '${PIP} install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh '${PYTHON} -m pytest tests/test_httpbin_api.py -v --alluredir=allure-results --html=report.html --self-contained-html'
            }
        }

        stage('Generate Reports') {
            steps {
                allure includeProperties: false,
                      jdk: '',
                      results: [[path: 'allure-results']]

                archiveArtifacts artifacts: 'report.html', fingerprint: true
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}