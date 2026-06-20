#!/usr/bin/env python3
import sys
import os
import json
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QTextEdit, QLineEdit, QPushButton, QListWidget, 
                             QLabel, QMessageBox)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QIcon

DB_PATH = os.path.expanduser("~/.config/aria_context_registry.json")

class ContextManager(QWidget):
    def __init__(self):
        super().__init__()
        self.registry = self.load_registry()
        self.init_ui()

    def load_registry(self):
        if os.path.exists(DB_PATH):
            try:
                with open(DB_PATH, 'r') as f:
                    return json.load(f)
            except Exception:
                pass
        # Default initialization state if file doesn't exist
        return {
            "8.0": "✂️ SYSTEM CONTEXT REGISTER: ARIA YADAV (ULTIMATE PRODUCTION EDITION V8.0)\n\n👤 Identity & Profile..."
        }

    def save_registry(self):
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        with open(DB_PATH, 'w') as f:
            json.dump(self.registry, f, indent=4)

    def init_ui(self):
        self.setWindowTitle("Aria - Context Registry Node")
        self.resize(900, 600)

        # Set taskbar/window icon from local file
        script_dir = os.path.dirname(os.path.abspath(__file__))
        for icon_name in ("icon.svg", "icon.png", "icon.jpg", "icon.img"):
            icon_path = os.path.join(script_dir, icon_name)
            if os.path.exists(icon_path):
                icon = QIcon(icon_path)
                self.setWindowIcon(icon)
                QApplication.instance().setWindowIcon(icon)
                break
        
        # Layouts
        main_layout = QHBoxLayout()
        left_panel = QVBoxLayout()
        right_panel = QVBoxLayout()
        
        # Left Panel Components (History & Controls)
        left_panel.addWidget(QLabel("<b>Historical Log Files</b>"))
        self.version_list = QListWidget()
        self.version_list.addItems(sorted(self.registry.keys(), reverse=True))
        self.version_list.itemClicked.connect(self.display_context)
        left_panel.addWidget(self.version_list)
        
        self.version_input = QLineEdit()
        self.version_input.setPlaceholderText("New Version Tag (e.g., 8.1)")
        left_panel.addWidget(self.version_input)
        
        commit_btn = QPushButton("Commit State to Registry")
        commit_btn.clicked.connect(self.commit_state)
        left_panel.addWidget(commit_btn)
        
        # Right Panel Components (Active Context & Operations)
        right_panel.addWidget(QLabel("<b>Active Context Viewport</b>"))
        self.context_display = QTextEdit()
        right_panel.addWidget(self.context_display)
        
        copy_btn = QPushButton("📋 Copy Active Context to Clipboard")
        copy_btn.setStyleSheet("background-color: #2c3e50; color: white; font-weight: bold;")
        copy_btn.clicked.connect(self.copy_to_clipboard)
        right_panel.addWidget(copy_btn)
        
        # Assembly
        main_layout.addLayout(left_panel, 1)
        main_layout.addLayout(right_panel, 3)
        self.setLayout(main_layout)
        
        # Select newest version on boot
        if self.version_list.count() > 0:
            self.version_list.setCurrentRow(0)
            self.display_context(self.version_list.item(0))

    def display_context(self, item):
        version = item.text()
        self.context_display.setPlainText(self.registry[version])

    def commit_state(self):
        version = self.version_input.text().strip()
        content = self.context_display.toPlainText().strip()
        
        if not version or not content:
            self.show_toast("Validation failure: version tag and context content are required.")
            return
            
        self.registry[version] = content
        self.save_registry()
        
        # Refresh List View
        self.version_list.clear()
        self.version_list.addItems(sorted(self.registry.keys(), reverse=True))
        self.version_input.clear()
        self.show_toast(f"State Node {version} committed to registry.")

    def copy_to_clipboard(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.context_display.toPlainText())
        self.show_toast("Context block copied to system clipboard wrapper.")

    def show_toast(self, message):
        toast = QLabel(message, self)
        toast.setStyleSheet("""
            background-color: #2c3e50;
            color: white;
            padding: 12px 24px;
            border-radius: 6px;
            font-weight: bold;
        """)
        toast.adjustSize()
        toast.move(
            self.width() - toast.width() - 20,
            self.height() - toast.height() - 20
        )
        toast.show()
        QTimer.singleShot(2000, toast.deleteLater)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    manager = ContextManager()
    manager.show()
    sys.argv.append('--style=fusion') # Match native KDE aesthetics cleaner
    sys.exit(app.exec())
