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
          echo "Cleaning previous DerivedData..."
          rm -rf GestureLabIOS/build || true

          cd GestureLabIOS
          echo "Confirming .xcodeproj presence:"
          ls -la GestureLabIOS.xcodeproj || exit 1

          echo "Starting clean build..."
          xcodebuild -project GestureLabIOS.xcodeproj -scheme GestureLabIOS \
          -destination "platform=iOS Simulator,name=iPhone 16,OS=18.1" \
          -derivedDataPath ./build clean build

          echo "=== Build output verification ==="
          ls -la build/Build/Products/Debug-iphonesimulator || true
        '''
      }
    }

    stage('Start Appium, grant permissions & run tests') {
      steps {
        sh '''
          set -e
          echo "Starting Appium (background)..."
          # start appium in background and log to appium.log
          nohup appium --log-level info > appium.log 2>&1 &
          sleep 6

          echo "Ensure applesimutils exists and is usable:"
          if ! command -v applesimutils >/dev/null 2>&1; then
            echo "applesimutils not found in PATH — please install on the node (brew tap wix/brew && brew install applesimutils)"
            exit 2
          fi

        # give simulator a moment
        sleep 2

        # pre-grant permissions using applesimutils (use the built app bundle id)
        SIM_ID=$(xcrun simctl list devices booted | grep -v unavailable | head -n1 | awk -F'[()]' '{print $2}')
        echo "Using simulator id: $SIM_ID"
        BUNDLE="com.badigeraravinda.GestureLabIOS"
        echo "Pre-granting permissions for $BUNDLE on $SIM_ID"
        applesimutils --byId "$SIM_ID" --bundle "$BUNDLE" --setPermissions '{"camera":"YES","location":"YES","photos":"YES","notifications":"YES"}' || true

        # activate venv, install reqs and run pytest (adjust venv path if different)
        echo "Activating venv and running tests..."
        . ./venv/bin/activate
        pip install -r requirements.txt || true
        pytest -s appium_ios/gesture_single_tap.py || exit $?
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
