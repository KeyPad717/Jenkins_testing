pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                echo 'Cloning repository'
                git 'https://github.com/KeyPad717/https://github.com/KeyPad717/Jenkins_testing.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building application'
                sh 'echo Build stage completed'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing application'
                sh 'python3 test.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application'
                sh 'echo Deployment done'
            }
        }

        stage('Monitor') {
            steps {
                echo 'Monitoring application'
                sh 'echo Monitoring done'
            }
        }
    }
}
