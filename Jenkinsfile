pipeline {
  agent any
  stages {
    stage('Checkout & Info') {
      steps {
        echo "Workspace: ${env.WORKSPACE}"
        checkout scm
        sh 'pwd; ls -la'
      }
    }

    stage('Smoke placeholder') {
      steps {
        echo "Run smoke tests here (placeholder)."
        // you will replace this with the real build/test steps later
      }
    }
  }
  post {
    always {
      echo "Pipeline finished on ${env.NODE_NAME}"
    }
  }
}
