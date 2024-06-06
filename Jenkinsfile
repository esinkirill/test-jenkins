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
                        echo "No existing container found to stop."
                    }
                    try {
                        docker.remove('competent_nightingale')
                    } catch (Exception e) {
                        // Если контейнер не удалось удалить (возможно, он не существует), продолжаем
                        echo "No existing container found to remove."
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t esinkirill/test-jenkins-image:latest --build-arg BUILD_DATE=2024-06-06T23:21:36Z ."
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Поиск свободного порта на хосте
                    def hostPort = findAvailablePort()

                    // Запуск нового контейнера после пересборки
                    docker.image('esinkirill/test-jenkins-image:latest').run("-p ${hostPort}:5003", "--name competent_nightingale")
                }
            }
        }
    }
}

def findAvailablePort() {
    def port = 5003
    def socket = new java.net.ServerSocket()
    try {
        while (true) {
            try {
                socket.bind(new java.net.InetSocketAddress("localhost", port))
                return port
            } catch (java.net.BindException e) {
                port++
            }
        }
    } finally {
        socket.close()
    }
}

