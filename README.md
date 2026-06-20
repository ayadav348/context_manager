# Context Registry Node

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

### KDE Desktop Integration (Taskbar Pin)

The `.desktop` file and icon must be set up correctly for KDE to show the right icon when the app is pinned to the taskbar.

**1. Generate a PNG icon from the SVG:**

KDE's taskbar/pin system requires a raster icon installed in the hicolor theme. The SVG alone is not reliable for pinned entries.

```bash
rsvg-convert -w 256 -h 256 icon.svg -o icon.png
mkdir -p ~/.local/share/icons/hicolor/256x256/apps
cp icon.png ~/.local/share/icons/hicolor/256x256/apps/aria-context.png
```

**2. Create the `.desktop` file:**

Save the following to `~/.local/share/applications/aria-context.desktop`:

```ini
[Desktop Entry]
Name=Aria Context Registry
Exec=python3 /path/to/context_manager.py
Icon=aria-context
Type=Application
Categories=Utility;
StartupWMClass=context_manager
StartupNotify=false
```

> Use `Icon=aria-context` (the theme name), not an absolute path to the SVG or PNG. This is what KDE uses to resolve the icon for pinned entries.
> Use `Exec=python3 /path/to/...` rather than executing the `.py` file directly.

**3. Register the desktop entry:**

```bash
update-desktop-database ~/.local/share/applications
```

**4. Pin to taskbar:**

Launch the app, right-click its taskbar entry, and select **Pin to Task Manager**.

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
