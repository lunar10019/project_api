pipeline {
    agent any

    environment {
        PYTHON = 'python3'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Python') {
            steps {
                script {
                    def pythonExists = sh(script: 'command -v python3', returnStatus: true) == 0
                    if (!pythonExists) {
                        error("Python3 не найден! Установите Python3 на сервер Jenkins или используйте Docker-агент")
                    }

                    sh '${PYTHON} --version'
                }
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                sh '${PYTHON} -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh '. venv/bin/activate && ${PYTHON} -m pytest tests/test_httpbin_api.py -v --alluredir=allure-results --html=report.html --self-contained-html'
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