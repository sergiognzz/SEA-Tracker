#!/usr/bin/env bash

set -e

APP_NAME="sea-tracker"
INSTALL_DIR="/usr/local/bin"
CONFIG_DIR="$HOME/.config/$APP_NAME"
SYMLINK_PATH="$INSTALL_DIR/$APP_NAME"

echo "Uninstalling $APP_NAME..."


if [ -L "$SYMLINK_PATH" ] || [ -f "$SYMLINK_PATH" ]; then
    echo "Removing symlink $SYMLINK_PATH"
    sudo rm -f "$SYMLINK_PATH"
else
    echo "Symlink not found at $SYMLINK_PATH"
fi


if [ -d "$CONFIG_DIR" ]; then
    echo "Removing config directory $CONFIG_DIR"
    rm -rf "$CONFIG_DIR"
else
    echo "Config directory not found at $CONFIG_DIR"
fi

echo "Uninstallation completed."
