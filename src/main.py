"""
    Main entry point for the application.
"""
import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from src.modules.gui.pages_holder import UiMainWindow # pylint: disable=<C0413>
from src.modules.gui.pop_ups.privacy_policies import PrivacyPolicies # pylint: disable=<C0413>
from src.modules.load_configs.load_icons_and_images_paths import ImgAndIconsPath # pylint: disable=<C0413>

try:
    from ctypes import windll  # Only exists on Windows.
    MYAPPID = 'mycompany.myproduct.subproduct.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(MYAPPID)
except ImportError:
    pass

def main():
    """
        Start the application.
        Initializes the application with privacy policies check.
        If the user accepts the privacy policies, the main window is shown.
        Otherwise, the application exits.
    """
    print(ImgAndIconsPath.task_bar_icon)
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(ImgAndIconsPath.task_bar_icon))
    window = UiMainWindow()
    if PrivacyPolicies().show_message():
        window.show()
        sys.exit(app.exec())


if __name__ == "__main__":
    main()
