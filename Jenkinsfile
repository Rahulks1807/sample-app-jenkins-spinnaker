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
                   docker build -t gcr.io/rohan-orbit/sample-app:${BUILD_NUMBER} .
                '''
            }
        }
        stage('Push') {
            steps {
                echo 'Push Dockerfile'
                sh '''
                   gcloud auth activate-service-account rohan-orbit  --key-file=${auth_key}
                   gcloud auth configure-docker
                   docker push gcr.io/rohan-orbit/sample-app:${BUILD_NUMBER}
                '''
            }
        }
    }
}
