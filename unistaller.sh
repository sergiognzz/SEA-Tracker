#!/usr/bin/env bash

set -e

APP_NAME="sea-tracker"

echo "Uninstalling $APP_NAME..."
sudo rm -rf ~/.config/sea-tracker 2>/dev/null
sudo rm -rf /usr/local/bin/sea-tracker 2>/dev/null

echo "Uninstallation completed."
