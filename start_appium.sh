#!/usr/bin/env bash
set -euxo pipefail
LOG=${1:-appium.log}
nohup appium --log-level info > "${LOG}" 2>&1 &
sleep 6
tail -n +1 "${LOG}" | sed -n '1,200p'