pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Python') {
            steps {
                sh '''
                apt-get update -qq && \
                apt-get install -y --no-install-recommends python3 python3-pip && \
                python3 --version
                '''
            }
        }

        stage('Setup Dependencies') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m pytest tests/test_httpbin_api.py -v --alluredir=allure-results --html=report.html --self-contained-html'
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