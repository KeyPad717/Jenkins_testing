pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building application'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 test.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application'
            }
        }

        stage('Monitor') {
            steps {
                echo 'Monitoring application'
            }
        }
    }
}
