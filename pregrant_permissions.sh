#!/usr/bin/env bash
set -euxo pipefail
SIM_UDID="$1"
BUNDLE="$2"

echo "Uninstalling app if present..."
xcrun simctl uninstall "$SIM_UDID" "$BUNDLE" || true

echo "Setting permissions via applesimutils..."
applesimutils --byId "$SIM_UDID" --bundle "$BUNDLE" --setPermissions '{"camera":"YES","location":"YES","photos":"YES","notifications":"YES"}'