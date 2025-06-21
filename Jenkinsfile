pipeline {
    agent any

    environment {
        PYTHON = sh(script: 'command -v python3 || command -v python', returnStdout: true).trim()
        VENV_DIR = "${WORKSPACE}/venv"
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
                    if (!env.PYTHON) {
                        error("Python не найден! Установите Python 3 на сервер Jenkins")
                    }
                    sh """
                        echo "Используемый Python: ${PYTHON}"
                        ${PYTHON} --version
                    """
                }
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh """
                    ${PYTHON} -m venv "${VENV_DIR}" || ${PYTHON} -m virtualenv "${VENV_DIR}"
                    . "${VENV_DIR}/bin/activate" && pip install --upgrade pip
                """
            }
        }

        stage('Install Dependencies') {
            steps {
                sh """
                    . "${VENV_DIR}/bin/activate" && pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                sh """
                    . "${VENV_DIR}/bin/activate" && \
                    pytest tests/test_httpbin_api.py -v \
                        --alluredir=allure-results \
                        --html=report.html \
                        --self-contained-html
                """
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

    post {
        always {
            cleanWs()
        }
    }
}