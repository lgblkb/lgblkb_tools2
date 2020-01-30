pipeline {
    agent { docker { image 'python:3.6.10' } }
    stages {
        stage('build') {
            steps {
                sh 'echo "Hello World"'
                sh '''
                    echo "Multiline shell steps works too"
                    ls -lah
                '''
                sh 'python --version'
            }
        }
    }
}