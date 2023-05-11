pipeline {
    environment{
        dockerimg = ''
        DB_NAME = "mydatabase"
        DB_HOST = "127.0.0.1"
        DB_PORT = "3306"
        DB_USER = "root"
        DB_PASSWORD = "Vipul*20"
    }
    
    agent any
    
    stages {
        stage('Git Pull') {
            steps {
                echo 'Git Pull'
                git branch: 'main', url: 'https://github.com/vipul2097/SPECRM.git',
                credentialsId: 'githubid'
            }
        }
        stage('Install Dependencies in the Jenkins Workspace..') {
            steps {
                echo 'Installing Dependencies'
                sh 'pip3 install django mysqlclient '
            }
        }
        stage('Test and Build') {
            steps {
                echo 'We dont need to Build our code. Just do the Model testing.'
                sh 'python3 manage.py test client.tests'
                sh 'python3 manage.py test lead.tests'
                sh 'python3 manage.py test team.tests'
                sh 'python3 manage.py test userprofile.tests'
            }
        }
        stage('Docker Build Image..') {
            steps {
                 script {
                     echo 'Docker Build Image.'
                     dockerimg = docker.build("vipul2097/spemajorproject")
                }
            }
        }
        stage('Push Django Docker Image') {
            steps {
                script{
                    docker.withRegistry('','dockerhub'){
                    dockerimg.push()
                    }
                }
            }
        }
        stage('Delete Docker Containers') {
            steps {
                script{
                    // here we are checking if there are any containers running in our system if so then delete them.
                    def running_containers = sh (returnStdout: true, script: 'docker ps -q').trim()
                    if (running_containers) {
                        sh 'docker rm -f $(docker ps -aq)'
                    }
                    
                    sh 'docker image rm -f vipul2097/spemajorproject'
                }
            }
        }
        stage('Clean Docker Images') {
            steps{
            sh '''
               # Remove all images with the tag <none>
               docker rmi --force $(docker images | grep "<none>" | awk '{print $3}')
            '''
            }
         }
         stage('Ansible Deploy'){
            steps{
              ansiblePlaybook colorized:true, disableHostKeyChecking:true, installation:'Ansible', inventory:'Inventory', playbook:'playbook.yml'
            }
         }
        
    }
}
