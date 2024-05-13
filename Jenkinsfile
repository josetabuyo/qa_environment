pipeline {
    agent none
    stages {
        stage("run qa regression tests") {
            agent any
            steps {
                // sh "docker rm -f qa-regression-pod"
                sh "docker build --platform linux/amd64 -t qa-regression -f Dockerfile.reg ."
                sh "docker run --platform linux/amd64 --add-host localhost:127.0.0.1 --name qa-regression-pod qa-regression"
                sh "cat output/qa_regression_result.html"
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



            
