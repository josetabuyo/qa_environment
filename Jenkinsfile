pipeline {
    // Assign to docker agent(s) label, could also be 'any'
    agent none
    stages {
        stage("Regression") {
            agent any
            steps {
                sh "docker build --platform linux/amd64 -t qa-regression -f Dockerfile.reg ."
                sh "docker run -v /Users/josetabuyo/Development/experiments/qa_environment/output:/app/output --platform linux/amd64 --add-host localhost:127.0.0.1 qa-regression"
                sh "ls -trola output"
                sh "pwd"
                publishHTML (
                    target : [
                        allowMissing: false,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: '/Users/josetabuyo/Development/experiments/qa_environment/output',
                        reportFiles: 'qa_regression_result.html'
                    ]
                )    
            }
        }
        

        // stage("build and test the project") {
        //     agent {
        //         docker "build-tools-image"
        //     }
        //     stages {
        //        stage("build") {
        //             steps {
        //                 sh '/usr/local/bin/chrome-linux64/chrome --version'
        //                 sh '/usr/local/bin/chromedriver-linux64/chromedriver --version'
        //             }
        //        }
        //        stage("test") {
        //            steps {
        //                sh "./test.sh"
        //            }
        //        }
        //     }
        // }
    }
}



            
