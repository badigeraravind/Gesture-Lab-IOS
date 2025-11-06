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

    stage('Build the IOS app'){
      steps{
        echo "Building app on node: ${env.NODE_NAME}"
        sh '''
          set -e
          cd GestureLabIOS
          xcodebuild -scheme GestureLabIOS \
          -destination "platform=iOS Simulator,name=iPhone 16,OS=18.1" \
          -derivedDataPath ./build clean build
          ls -la build/Build/Products/Debug-iphonesimulator | grep GestureLabIOS || true
        '''
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
