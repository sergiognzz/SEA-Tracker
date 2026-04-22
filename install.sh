#!/usr/bin/env bash

set -e

APP_NAME="sea-tracker"
INSTALL_DIR="/usr/local/bin"
PROJECT_DIR="$(pwd)"
MAIN_FILE="sea_tracker.py"

echo "Installing $APP_NAME..."

# Check if main file exists
if [ ! -f "$PROJECT_DIR/$MAIN_FILE" ]; then
    echo "Error: $MAIN_FILE not found in the current directory"
    exit 1
fi

# Make main script executable
chmod +x "$PROJECT_DIR/$MAIN_FILE"

# Add shebang if missing
if ! head -n 1 "$PROJECT_DIR/$MAIN_FILE" | grep -q "^#!"; then
    echo "Adding shebang..."
    sed -i '1i #!/usr/bin/env python3' "$PROJECT_DIR/$MAIN_FILE"
fi

# Create symlink in /usr/local/bin
echo "Creating symlink in $INSTALL_DIR/$APP_NAME"
sudo ln -sf "$PROJECT_DIR/$MAIN_FILE" "$INSTALL_DIR/$APP_NAME"

# Install dependencies if requirements.txt exists
if [ -f "$PROJECT_DIR/requirements.txt" ]; then
    echo "Installing dependencies..."
    pip3 install -r "$PROJECT_DIR/requirements.txt"
fi

echo "Installation completed."
echo "You can now run: $APP_NAME"