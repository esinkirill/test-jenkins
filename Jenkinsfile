pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/esinkirill/test-jenkins.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('esinkirill/test-jenkins-image:latest', '', '--no-cache')
                }
            }
        }

        stage('Stop and Remove Existing Container') {
            steps {
                script {
                    docker.stop('competent_nightingale')
                    docker.remove('competent_nightingale')
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    docker.image('esinkirill/test-jenkins-image:latest').run('-p 5003:5003', '--name competent_nightingale')
                }
            }
        }
    }
}
