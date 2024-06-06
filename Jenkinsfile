pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Клонирование репозитория с помощью Git
                git 'https://github.com/esinkirill/test-jenkins.git'
            }
        }
        stage('Build on Remote Host') {
            environment {
                REMOTE_HOST = '188.120.225.17' // IP адрес удаленного хоста
                REMOTE_USER = 'esinkirill' // Имя пользователя для доступа к удаленному хосту
                REMOTE_DIR = '/home/esinkirill/test-jenkins/test-jenkins/' // Путь до проекта на удаленном хосте
            }
            steps {
                // Копирование проекта на удаленный хост
                sh "scp -r . ${env.REMOTE_USER}@${env.REMOTE_HOST}:${env.REMOTE_DIR}"
                
                // Выполнение сборки Docker образа на удаленном хосте
                sh "ssh ${env.REMOTE_USER}@${env.REMOTE_HOST} 'cd ${env.REMOTE_DIR} && docker build -t your_image_name .'"
            }
        }
    }
}

