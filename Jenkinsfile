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

            // docker build --platform linux/amd64 -t qa-regression -f Dockerfile.reg .
            agent {
                dockerfile {
                    filename 'Dockerfile.reg'
                    dir '.'
                    additionalBuildArgs  '--platform linux/amd64 -t qa-regression'
                    args '--platform linux/amd64 --add-host localhost:127.0.0.1 --name qa-regression-pod qa-regression -v /$PWD:/$PWD'
                }
            }
            steps {
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



            
