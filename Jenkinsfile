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
                   docker build -t us-central1-docker.pkg.dev/rohan-orbit/internal/sample-app:${BUILD_NUMBER} .
                '''
            }
        }
        stage('Push') {
            steps {
                echo 'Push Dockerfile'
                sh '''
                   gcloud auth configure-docker us-docker.pkg.dev
                   docker push gcr.io/rohan-orbit/sample-app:${BUILD_NUMBER}
                '''
            }
        }
    }
}
