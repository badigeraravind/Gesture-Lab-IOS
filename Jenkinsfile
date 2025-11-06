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
    stage('Build the IOS app') {
      steps {
        echo "Building app on node: ${env.NODE_NAME}"
        sh '''
          set -e
          echo "Cleaning previous DerivedData..."
          rm -rf GestureLabIOS/build || true

          cd GestureLabIOS
          echo "Confirming .xcodeproj presence:"
          ls -la GestureLabIOS.xcodeproj || (echo "project not found" && exit 1)

          echo "Starting clean build..."
          xcodebuild -project GestureLabIOS.xcodeproj -scheme GestureLabIOS \
            -destination "platform=iOS Simulator,name=iPhone 16,OS=18.1" \
            -derivedDataPath ./build clean build

          echo "=== Build output verification ==="
          ls -la build/Build/Products/Debug-iphonesimulator | grep GestureLabIOS || true 
        '''
      }
    }
    stage('Start Appium, grant permissions & run tests') {
      steps {
        sh '''
          if !command - v applesimutils > /dev/null 2 > & 1; then
            echo "Installing applesimutils..."
            # only do this if Homebrew is available on the node
            if command -v brew >/dev/null 2>&1; then
              brew tap wix / brew
              brew install applesimutils || true
            else
              echo "Homebrew not found; applesimutils installation skipped." 
            fi
          fi
        '''
        sh '''
          set -e
          echo "Starting Appium (background)..."
          nohup appium --log-level info > appium.log 2>&1 &

          # give Appium a moment
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
        '''
      }
    }
    stage('Run iOS Appium Tests') {
      steps {
        echo "Running automated iOS Appium tests..."
        sh '''
          set -e
          echo "Activating Python virtual environment..."
          . ./venv/bin/activate

          echo "Installing dependencies..."
          pip install --upgrade pip
          pip install -r requirements.txt || true

          echo "Running pytest..."
          mkdir -p reports
          pytest -s appium_ios --maxfail=1 --disable-warnings --html=reports/test_report.html --self-contained-html || true

          echo "Test execution complete. Collecting logs..."
          cp appium.log reports/appium.log || true

          echo "Listing reports folder contents:"
          ls -la reports || true
        '''
      }
    }

    post {
      always {
        echo "Archiving test results and logs..."
        archiveArtifacts artifacts: 'reports/**/*', fingerprint: true
      }
    }
  }
}
post {
  always {
    echo "Pipeline finished on ${env.NODE_NAME}"
  }
}