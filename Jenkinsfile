pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/esinkirill/test-jenkins.git'
            }
        }
        
        stage('Stop and Remove Existing Container') {
            steps {
                script {
                    // Остановка и удаление существующего контейнера, если он существует
                    try {
                        docker.stop('competent_nightingale')
                    } catch (Exception e) {
                        // Если контейнер не удалось остановить (возможно, он не существует), продолжаем
                    }
                    try {
                        docker.remove('competent_nightingale')
                    } catch (Exception e) {
                        // Если контейнер не удалось удалить (возможно, он не существует), продолжаем
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Пересборка образа
                    docker.build('esinkirill/test-jenkins-image:latest', "--build-arg BUILD_DATE='2024-06-06T23:21:36Z'")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Запуск нового контейнера после пересборки
                    docker.image('esinkirill/test-jenkins-image:latest').run('-p 5003:5003', '--name competent_nightingale')
                }
            }
        }
    }
}
