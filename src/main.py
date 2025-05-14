"""
    Main entry point for the application.
"""
import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from src.modules.gui.pages_holder import UiMainWindow # pylint: disable=<C0413>
from src.modules.gui.pop_ups.privacy_policies import PrivacyPolicies # pylint: disable=<C0413>


def main():
    """
        Start the application.
        Initializes the application with privacy policies check.
        If the user accepts the privacy policies, the main window is shown.
        Otherwise, the application exits.
    """
    app = QApplication(sys.argv)

    window = UiMainWindow()
    if PrivacyPolicies().show_message():
        window.show()
        sys.exit(app.exec())


if __name__ == "__main__":
    main()
