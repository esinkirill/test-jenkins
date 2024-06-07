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
                    
                    try {
                        sh 'docker stop competent_nightingale || true'
                    } catch (Exception e) {
                        echo "No existing container found to stop."
                    }
                    try {
                        sh 'docker rm competent_nightingale || true'
                    } catch (Exception e) {
                        echo "No existing container found to remove."
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t esinkirill/test-jenkins-image:latest --build-arg BUILD_DATE=$(date +%Y-%m-%dT%H:%M:%S%z) .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                   
                    def hostPort = findAvailablePort()

                    
                    sh "docker run -d -p ${hostPort}:5003 --name competent_nightingale esinkirill/test-jenkins-image:latest"
                }
            }
        }
    }
}

def findAvailablePort() {
    def port = 5003
    while (!isPortAvailable(port)) {
        port++
    }
    return port
}

def isPortAvailable(port) {
    def result = sh(script: "lsof -i :${port}", returnStatus: true)
    return result != 0
}
