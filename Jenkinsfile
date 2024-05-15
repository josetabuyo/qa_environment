pipeline {
    // Assign to docker agent(s) label, could also be 'any'
    agent none
    stages {
        stage("run qa regression tests ssssssss") {
            //  // Equivalent to "docker build -f Dockerfile.reg --build-arg version=1.0.2 ./build/
            // agent {
            //     dockerfile {
            //         filename 'Dockerfile.reg'
            //         dir 'build'
            //         label 'my-defined-label'
            //         additionalBuildArgs  '--build-arg version=1.0.2'
            //         args '-v /tmp:/tmp'
            //     }
            // }
            environment {
                HOME="."
            }
            // docker build --platform linux/amd64 -t qa-regression -f Dockerfile.reg .
            agent {
                dockerfile {
                    filename 'Dockerfile.reg'
                    additionalBuildArgs  '--platform linux/amd64 -t qa-regression'
                    args '-it --platform linux/amd64 --add-host localhost:127.0.0.1 qa-regression /bin/sh'
                }
            }
            steps {
                sh "echo HolaGuacho"
                
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



            
