pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
                sh '''
                   docker info
                   docker build .
                '''
            }
        }
        stage('Build') {
            steps {
                echo 'Build Dockerfile'
                sh '''
                   docker build -t rahul1807/sample-blue-green-app:${build-number} .
                '''
            }
        }
    }
}
