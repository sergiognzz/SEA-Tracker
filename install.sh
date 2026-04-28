#!/usr/bin/env bash

set -e

APP_NAME="sea-tracker"
INSTALL_DIR="/usr/local/bin"
CONFIG_DIR="$HOME/.config/$APP_NAME"
PROJECT_DIR="$(pwd)"
MAIN_FILE="sea_tracker.py"

REPO_URL="https://github.com/tu-usuario/tu-repo.git"

echo "Installing $APP_NAME..."

# Clone repository
echo "Cloning repository into $CONFIG_DIR..."
rm -rf "$CONFIG_DIR"
git clone "$REPO_URL" "$CONFIG_DIR"

# main file comprobation
if [ ! -f "$CONFIG_DIR/$MAIN_FILE" ]; then
    echo "Error: $MAIN_FILE not found in cloned repository"
    exit 1
fi

# go to coppied directory
cd "$CONFIG_DIR"

# make executable
chmod +x "$MAIN_FILE"

# Add shebang
if ! head -n 1 "$MAIN_FILE" | grep -q "^#!"; then
    echo "Adding shebang..."
    sed -i '1i #!/usr/bin/env python3' "$MAIN_FILE"
fi

# make symlink
echo "Creating symlink in $INSTALL_DIR/$APP_NAME"
sudo ln -sf "$CONFIG_DIR/$MAIN_FILE" "$INSTALL_DIR/$APP_NAME"

echo "Installation completed."
echo "You can now run: $APP_NAME"

echo "Removing original project directory: $PROJECT_DIR"
cd ~
rm -rf "$PROJECT_DIR"

echo "Cleanup completed."
