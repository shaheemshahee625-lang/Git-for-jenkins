pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat '''
                    python3 --version
                    python3 -m venv venv
                    . venv/bin/activate
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                bat '''
                    . venv/bin/activate
                    pytest
                '''
            }
        }

        stage('Build') {
            steps {
                bat '''
                    . venv/bin/activate
                    echo "Build completed successfully"
                '''
            }
        }
    }
}