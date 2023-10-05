pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/dhruv2728/time_calculator']])
            }
        }
        stage('Build') {
            steps {
                sh "pip install -r requirements.txt"
            }
        }
    }
}
