pipeline {
    agent {
        docker {
            image 'python:3.9-slim'
            args '-u root'
            reuseNode true
        }
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Environment') {
            steps {
                sh 'python --version'
                sh 'pip --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/test_httpbin_api.py -v --alluredir=allure-results --html=report.html --self-contained-html'
            }
        }

        stage('Publish Reports') {
            steps {
                allure includeProperties: false,
                      jdk: '',
                      results: [[path: 'allure-results']]
                archiveArtifacts artifacts: 'report.html', fingerprint: true
            }
        }
    }

