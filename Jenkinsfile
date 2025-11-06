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
          set -e
            # install applesimutils only if it's missing and Homebrew exists on the node
            if ! command -v applesimutils >/dev/null 2>&1; then
              echo "Installing applesimutils..."
              if command -v brew >/dev/null 2>&1; then
                brew tap wix/brew
                brew install applesimutils || true
              else
                echo "Homebrew not found; applesimutils installation skipped."
              fi
            fi
        '''
        sh '''
          set -e

          echo "Ensure applesimutils exists and is usable:"
          if ! command -v applesimutils >/dev/null 2>&1; then
            echo "applesimutils not found in PATH — please install on the node (brew tap wix/brew && brew install applesimutils)"
            exit 2
          fi

          echo "Starting Appium (background)..."
          nohup appium --log-level info > appium.log 2>&1 &
          sleep 6

          # give simulator a moment
          sleep 2

          SIM_ID=$(xcrun simctl list devices booted | grep -v unavailable | head -n1 | awk -F'[()]' '{print $2}')
          if [ -z "$SIM_ID" ]; then
            echo "No booted simulator found — attempting to boot a device named 'iPhone 16'..."
            SIM_ID=$(xcrun simctl list devices | grep "iPhone 16 (" | head -n1 | awk -F'[()]' '{print $2}')

            if [ -z "$SIM_ID" ]; then
              echo "No 'iPhone 16' simulator found. List available simulators with: xcrun simctl list devices"
              exit 3
            fi

            open -a Simulator || true
            xcrun simctl boot "$SIM_ID" || true
            for i in $(seq 1 30); do
              if xcrun simctl list devices booted | grep -q "$SIM_ID"; then
                break
              fi
              sleep 1
            done

            if ! xcrun simctl list devices booted | grep -q "$SIM_ID"; then
              echo "Simulator did not boot within timeout. Try booting manually: xcrun simctl boot $SIM_ID"
              exit 3
            fi
          fi

          echo "Using simulator id: $SIM_ID"

          BUNDLE="com.badigeraravinda.GestureLabIOS"
          echo "Pre-granting permissions for $BUNDLE on $SIM_ID"
          applesimutils --byId "$SIM_ID" --bundle "$BUNDLE" --setPermissions '{"camera":"YES","location":"YES","photos":"YES","notifications":"YES"}' || true

          . ./venv/bin/activate
          pip install -r requirements.txt || true
          pytest -s appium_ios/gesture_2_single_tap.py || exit $?
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

          echo "Preparing reports folder..."
          mkdir -p reports

          echo "Running pytest (writing HTML report)..."
          pytest -v appium_ios/ --html=reports/allreport.html --self-contained-html || true

          echo "Test execution complete. Collecting logs..."
          cp appium.log reports/appium.log || true

          echo "Listing reports folder contents:"
          ls -la reports || true
        '''
      }
    }
  }
  post {
    always {
      echo "Archiving test artifacts..."
      archiveArtifacts artifacts: 'reports/**', fingerprint: true
      echo "Pipeline finished on ${env.NODE_NAME}"
    }
  }
}
