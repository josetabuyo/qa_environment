pipeline {
    agent { dockerfile true }
    stages {
        stage('CheckExample') {
            steps {
                sh '/usr/local/bin/chrome-linux64/chrome --version'
                sh '/usr/local/bin/chromedriver-linux64/chromedriver'
            }
        }
    }
}