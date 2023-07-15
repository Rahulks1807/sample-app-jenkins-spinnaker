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
                   docker build .
                '''
            }
        }
    }
}
