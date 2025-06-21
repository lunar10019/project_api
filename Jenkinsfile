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
                    echo "Используемый Python: ${env.PYTHON}"
                    sh "${env.PYTHON} --version"
                }
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                script {
                    try {
                        sh """
                            ${env.PYTHON} -m venv "${env.VENV_DIR}" || \
                            ${env.PYTHON} -m virtualenv "${env.VENV_DIR}" || \
                            { echo "Не удалось создать виртуальное окружение"; exit 1; }
                        """
                    } catch (Exception e) {
                        error("Ошибка создания виртуального окружения: ${e.getMessage()}")
                    }
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                sh """
                    . "${env.VENV_DIR}/bin/activate" && \
                    pip install --upgrade pip && \
                    pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                sh """
                    . "${env.VENV_DIR}/bin/activate" && \
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