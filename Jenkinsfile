pipeline {
    agent any

    stages {
        stage('Initial Stage') {
            steps {
                echo 'Hello This is a sample application'
            }
        }
        stage('Build') {
            steps {
                echo 'Build Dockerfile'
                sh '''
                   docker build -t rahul1807/sample-blue-green-app:${BUILD_NUMBER} .
                '''
            }
        }
        stage('Push') {
            steps {
                echo 'Push Dockerfile'
                sh '''
                   docker push rahul1807/sample-blue-green-app:${BUILD_NUMBER}
                '''
            }
        }
    }
}
