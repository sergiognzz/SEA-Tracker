#!/usr/bin/env bash

set -e

APP_NAME="sea-tracker"
INSTALL_DIR="/usr/local/bin"
CONFIG_DIR="$HOME/.config/sea-tracker"
PROJECT_DIR="$(pwd)"
MAIN_FILE="sea_tracker.py"

echo "Installing $APP_NAME..."

# Check if main file exists in current directory
if [ ! -f "$PROJECT_DIR/$MAIN_FILE" ]; then
    echo "Error: $MAIN_FILE not found in current directory"
    exit 1
fi

# Create config directory
echo "Creating config directory at $CONFIG_DIR"
mkdir -p "$CONFIG_DIR"

# Copy entire repository to config directory
echo "Copying project files..."
rsync -av --exclude ".git" "$PROJECT_DIR/" "$CONFIG_DIR/"

# Move into the new directory
cd "$CONFIG_DIR"

# Ensure main file exists after copy
if [ ! -f "$CONFIG_DIR/$MAIN_FILE" ]; then
    echo "Error: $MAIN_FILE not found after copying"
    exit 1
fi

# Make script executable
chmod +x "$CONFIG_DIR/$MAIN_FILE"

# Add shebang if missing
if ! head -n 1 "$CONFIG_DIR/$MAIN_FILE" | grep -q "^#!"; then
    echo "Adding shebang..."
    sed -i '1i #!/usr/bin/env python3' "$CONFIG_DIR/$MAIN_FILE"
fi

# Create symlink in /usr/local/bin
echo "Creating symlink in $INSTALL_DIR/$APP_NAME"
sudo ln -sf "$CONFIG_DIR/$MAIN_FILE" "$INSTALL_DIR/$APP_NAME"

echo "Installation completed."
echo "You can now run: $APP_NAME"