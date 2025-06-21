pipeline {
    agent any

    environment {
        PYTHON = 'python3'
        ALLURE = 'allure'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup') {
            steps {
                sh '''
                    ${PYTHON} -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pip install pytest allure-pytest pytest-html
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    ${PYTHON} -m pytest tests/test_httpbin_api.py -v --alluredir=allure-results --html=report.html --self-contained-html
                '''
            }
        }

        stage('Generate Reports') {
            steps {
                script {
                    if (fileExists('allure-results')) {
                        allure includeProperties: false,
                              jdk: '',
                              results: [[path: 'allure-results']]
                    } else {
                        echo 'No Allure results found'
                    }

                    if (fileExists('report.html')) {
                        archiveArtifacts artifacts: 'report.html', fingerprint: true
                    } else {
                        echo 'No HTML report found'
                    }
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