pipeline {
    // Assign to docker agent(s) label, could also be 'any'
    agent none
    stages {
        stage("dumy stage") {
            agent any
            steps {
                sh "echo HolaGuacho"
                sh "docker build --platform linux/amd64 -t qa-regression -f Dockerfile.reg ."
                sh "docker run --platform linux/amd64 --add-host localhost:127.0.0.1 qa-regression"
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



            
