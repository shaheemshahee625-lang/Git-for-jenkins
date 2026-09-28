pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\theed\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat '"C:\\Users\\theed\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pytest'
            }
        }

        stage('Build') {
            steps {
                bat '"C:\\Users\\theed\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pip freeze'
            }
        }
    }
}