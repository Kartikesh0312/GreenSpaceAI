#!/bin/bash

# Exit on any error
set -e

echo "Starting GreenScape AI setup for Mac M2..."

# Step 1: Install Homebrew
if ! command -v brew &> /dev/null; then
    echo "Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    # Add Homebrew to PATH
    echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zshrc
    eval "$(/opt/homebrew/bin/brew shellenv)"
else
    echo "Homebrew already installed."
fi

# Step 2: Install Miniforge for Python (ARM-compatible)
if ! command -v conda &> /dev/null; then
    echo "Installing Miniforge..."
    curl -L -o Miniforge3.sh https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-arm64.sh
    bash Miniforge3.sh -b -p $HOME/miniforge
    rm Miniforge3.sh
    $HOME/miniforge/bin/conda init zsh
    source ~/.zshrc
else
    echo "Miniforge already installed."
fi

# Step 3: Create and activate a virtual environment
echo "Creating Python virtual environment..."
$HOME/miniforge/bin/conda create -n greenscape python=3.10 -y
source $HOME/miniforge/bin/activate greenscape

# Step 4: Install Streamlit
echo "Installing Streamlit..."
pip install streamlit

# Step 5: Install VSCode (if not already installed)
if ! command -v code &> /dev/null; then
    echo "Installing Visual Studio Code..."
    brew install --cask visual-studio-code
else
    echo "VSCode already installed."
fi

# Step 6: Install SQLite (usually pre-installed on macOS)
if ! command -v sqlite3 &> /dev/null; then
    echo "Installing SQLite..."
    brew install sqlite
else
    echo "SQLite already installed."
fi

# Step 7: Verify installations
echo "Verifying installations..."
echo "Homebrew version: $(brew --version)"
echo "Python version: $(python --version)"
echo "Streamlit version: $(streamlit --version)"
echo "SQLite version: $(sqlite3 --version)"
echo "VSCode version: $(code --version)"

echo "Setup complete! Run 'source $HOME/miniforge/bin/activate greenscape' to activate the environment."
