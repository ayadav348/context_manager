# Aria - Context Registry Node

A lightweight PyQt6 desktop utility for storing, browsing, and copying context text blocks to the clipboard. Context entries are versioned and persisted in a local JSON database.

## Features

- **Versioned Registry** — Store context snapshots under version tags (e.g. `8.0`, `8.1`)
- **Editable Viewport** — View and modify any entry inline before copying or committing
- **Clipboard Export** — Copy any entry to the system clipboard with one click
- **Persistent Storage** — Data lives in `~/.config/aria_context_registry.json`, survives restarts

## Installation

### Dependencies

Requires Python 3 and PyQt6.

```bash
# Arch Linux
sudo pacman -S python-pyqt6

# Debian/Ubuntu
sudo apt install python3-pyqt6

# Fedora
sudo dnf install python3-qt6

# macOS (Homebrew)
brew install pyqt@6
```

### Run

```bash
python3 context_manager.py
```

### KDE Taskbar Pin

1. Make the script executable:
   ```bash
   chmod +x context_manager.py
   ```
2. A `.desktop` file should already be installed at `~/.local/share/applications/aria-context.desktop`. If not, create it with the following content:
   ```ini
   [Desktop Entry]
   Name=Aria Context Registry
   Exec=/path/to/context_manager.py
   Icon=/path/to/icon.svg
   Type=Application
   Categories=Utility;
   ```
3. Run `update-desktop-database ~/.local/share/applications`.
4. Launch the app, right-click its taskbar entry, and select **Pin to Task Manager**.

## Usage

| Area | Component | Action |
|---|---|---|
| Left panel | Version list | Click an entry to load it into the viewport |
| Left panel | Version tag input | Type a new tag (e.g. `8.1`) |
| Left panel | Commit button | Save the current viewport content under the new tag |
| Right panel | Context viewport | View or edit the selected entry |
| Right panel | Copy button | Copy the viewport content to clipboard |

## Data

All entries are stored in `~/.config/aria_context_registry.json`. The file is created automatically on first commit.
