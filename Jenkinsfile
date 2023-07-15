pipeline {
    agent any
    parameters {
        credentials(name: 'auth_key', description: 'authentication key', defaultValue: 'auth_key.json', credentialType: "Secret File", required: false )
    }
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
                   
                   gcloud auth configure-docker
                   docker push gcr.io/rohan-orbit/sample-app:${BUILD_NUMBER}
                '''
            }
        }
    }
}
