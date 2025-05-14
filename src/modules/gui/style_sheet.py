"""
    Window Style Sheet
"""
# from icons_images_path import ImgAndIconsPath
from src.modules.load_configs.load_icons_and_images_paths import ImgAndIconsPath

class StyleSheets:
    """
        DataClass that hold all style variables
    """
    main_window : str = """
        background-color: #000000;
        font-family: 'Segoe UI', 'Roboto', sans-serif;
    """
    side_bar : str = """
        background-color: #121212;
        border-right: 1px solid #333333;
        padding: 5px 0px;
    """
    side_bar_button = """
        QPushButton {
            background-color: #121212;
            color: white;
            border: none;
            border-top-left-radius: 15px;
            border-bottom-left-radius: 15px;
            padding: 12px 15px;
            text-align: left;
            font-weight: 500;
            font-size: 13px;
            width: 500px;
            height: 20px;
        }
        QPushButton:hover {
            background-color: #3498DB;
            color: #FFFFFF;
        }
        QPushButton:checked {
            background-color: #2980B9;
            color: #FFFFFF;
            font-weight: bold;
        }
    """
    content : str = """
        background-color: #0F0F0F;
    """
    header_footnote : str = """
        background-color: #0c0c0c;
        font: 600 8pt 'Segoe UI';
        color: #FFFFFF;
        border-bottom: 1px solid #333333;
    """
    page_holder : str = """
        background-color: #121212;
        border-radius: 12px;
    """
    title_bar : str = """
        background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #0F0F0F, stop:1 #1A1A1A);
        border-bottom: 1px solid #333333;
    """
    title_bar_button : str = """
        QPushButton {
            background-color: #2C2C2C;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 8px;
            max-width: 10px;
            max-height: 30px;
            font-weight: bold;
            margin: 2px;
        }
        QPushButton:hover {
            background-color: #3498DB;
        }
        QPushButton:pressed {
            background-color: #2980B9;
        }
    """
    resize_button = f"""
        QSizeGrip {{
            image: url({ImgAndIconsPath.resize_button});
            width: 16px;
            height: 16px;
            margin: 2px;
        }}
    """
    pages : str = """
        QWidget {
            background-color: #121212;
            color: #F5F5F5;
            font-family: 'Segoe UI', 'Roboto', sans-serif;
        }

        QMenuBar {
            background-color: #1A1A1A;
            color: #F5F5F5;
            padding: 2px;
            font-weight: 500;
        }

        QMenuBar::item {
            background-color: transparent;
            padding: 5px 10px;
            border-radius: 6px;
        }

        QMenuBar::item::selected {
            background-color: #3498DB;
        }

        QMenu {
            background-color: #1A1A1A;
            color: #F5F5F5;
            border: 1px solid #333333;
            border-radius: 6px;
            padding: 5px 0px;
        }

        QMenu::item {
            padding: 6px 25px 6px 20px;
            border-radius: 4px;
            margin: 2px 8px;
        }

        QMenu::item::selected {
            background-color: #3498DB;
        }

        QToolBar {
            background-color: #1A1A1A;
            border: 1px solid #333333;
            spacing: 3px;
            padding: 2px;
        }

        QToolButton {
            background-color: #2C2C2C;
            color: #F5F5F5;
            border-radius: 6px;
            padding: 5px;
        }

        QToolButton:hover {
            background-color: #3498DB;
        }

        QPushButton {
            background-color: #2C2C2C;
            color: #FFFFFF;
            border: none;
            padding: 8px 16px;
            border-radius: 10px;
            font-weight: 500;
            font-size: 13px;
            min-height: 30px;
        }

        QPushButton:hover {
            background-color: #3498DB;
        }

        QPushButton:pressed {
            background-color: #2980B9;
        }

        QPushButton:disabled {
            background-color: #1A1A1A;
            color: #666666;
        }

        QLineEdit, QTextEdit, QPlainTextEdit {
            background-color: #1E1E1E;
            color: #F5F5F5;
            border: 1px solid #333333;
            border-radius: 8px;
            padding: 8px;
            selection-background-color: #3498DB;
        }
        
        QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus {
            border: 1px solid #3498DB;
        }
        
        QTableWidget {
            background-color: #1E1E1E;
            alternate-background-color: #3C3C3C;
            font-size: 13px;
            outline: none;
            
        }
        QHeaderView::section {
            background-color: #404040;
            color: white;
            padding: 4px;
            border: 1px solid #ccc;
        }
        QTableWidget::item {
            padding: 5px;
        }
        QTableWidget::item:selected {
            background-color: #007ACC;
            gridline-color: #3498DB;
        }

        QTableWidget QLineEdit {
            background: transparent;
            border: none;
            color: white;
            selection-background-color: #005999;
            padding: 0px;
            outline: none;
            
        }
        QComboBox {
            background-color: #2C2C2C;
            color: #F5F5F5;
            border: 1px solid #333333;
            border-radius: 8px;
            padding: 5px 10px;
            min-height: 28px;
        }
        
        QComboBox::drop-down {
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 25px;
            border-left: 1px solid #333333;
            border-top-right-radius: 8px;
            border-bottom-right-radius: 8px;
        }

        QComboBox QAbstractItemView {
            background-color: #1A1A1A;
            color: #F5F5F5;
            selection-background-color: #3498DB;
            border: 1px solid #333333;
            border-radius: 0px 0px 8px 8px;
            outline: none;
        }

        QHeaderView::section {
            background-color: #1A1A1A;
            color: #F5F5F5;
            border: 1px solid #333333;
            padding: 8px;
            font-weight: bold;
        }

        QTreeView {
            background-color: #1E1E1E;
            color: #F5F5F5;
            border: 1px solid #333333;
            border-radius: 8px;
        }
        
        QTreeView::item {
            padding: 5px;
            border-radius: 4px;
        }
        
        QTreeView::item:selected {
            background-color: #3498DB;
            color: #FFFFFF;
        }

        QListView {
            background-color: #1E1E1E;
            color: #F5F5F5;
            border: 1px solid #333333;
            border-radius: 8px;
            padding: 5px;
        }
        
        QListView::item {
            padding: 5px;
            border-radius: 4px;
        }
        
        QListView::item:selected {
            background-color: #3498DB;
            color: #FFFFFF;
        }

        /* Modern Scrollbars */
        QScrollBar:horizontal {
            border: none;
            background-color: #1A1A1A;
            height: 10px;
            margin: 0px 0px 0px 0px;
            border-radius: 5px;
        }

        QScrollBar::handle:horizontal {
            background-color: #3498DB;
            min-width: 25px;
            border-radius: 5px;
        }

        QScrollBar::handle:horizontal:hover {
            background-color: #2980B9;
        }

        QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
            border: none;
            background: none;
            width: 0px;
        }

        QScrollBar:vertical {
            border: none;
            background: #0F0F0F;
            width: 10px;
            margin: 0px 0px 0px 0px;
            outline: none;
        }

        QScrollBar::handle:vertical {
            background-color: #3498DB;
            min-height: 25px;
        }

        QScrollBar::handle:vertical:hover {
            background-color: #2980B9;
        }

        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            border: none;
            background: none;
            height: 0px;
        }

        QStatusBar {
            background-color: #0F0F0F;
            color: #F5F5F5;
            border-top: 1px solid #333333;
            padding: 2px 5px;
        }

        /* Tab widgets with modern styling */
        QTabWidget::pane {
            border: 1px solid #333333;
            border-radius: 8px;
            top: -1px;
        }

        QTabBar::tab {
            background-color: #1A1A1A;
            color: #F5F5F5;
            border: 1px solid #333333;
            border-bottom-color: #333333;
            border-top-left-radius: 8px;
            border-top-right-radius: 8px;
            padding: 8px 12px;
            min-width: 80px;
            font-weight: 500;
        }

        QTabBar::tab:selected {
            background-color: #3498DB;
            color: #FFFFFF;
        }

        QTabBar::tab:hover:!selected {
            background-color: #2C2C2C;
        }

        QGroupBox {
            border: 1px solid #333333;
            border-radius: 10px;
            margin-top: 20px;
            padding-top: 15px;
            font-weight: bold;
        }

        QGroupBox::title {
            subcontrol-origin: margin;
            subcontrol-position: top center;
            padding: 0px 10px;
            color: #F5F5F5;
            background-color: #121212;
        }

        QToolTip {
            background-color: #1A1A1A;
            color: #F5F5F5;
            border: 1px solid #333333;
            border-radius: 4px;
            padding: 5px;
            font-weight: 500;
        }
        
        QLabel {
            color: #FFFFFF;
            font-weight: 500;
            padding: 2px;
        }
        
        QCheckBox {
            color: #F5F5F5;
            spacing: 5px;
        }
        
        QCheckBox::indicator {
            width: 18px;
            height: 18px;
            border-radius: 4px;
            border: 1px solid #333333;
        }
        
        QCheckBox::indicator:checked {
            background-color: #3498DB;
            border: 1px solid #3498DB;
        }
        
        QRadioButton {
            color: #F5F5F5;
            spacing: 5px;
        }
        
        QRadioButton::indicator {
            width: 18px;
            height: 18px;
            border-radius: 9px;
            border: 1px solid #333333;
        }
        
        QRadioButton::indicator:checked {
            background-color: #3498DB;
            border: 1px solid #3498DB;
        }
        
        QProgressBar {
            border: 1px solid #333333;
            border-radius: 8px;
            background-color: #1A1A1A;
            text-align: center;
            color: #FFFFFF;
            font-weight: bold;
        }
        
        QProgressBar::chunk {
            background-color: #3498DB;
            border-radius: 7px;
        }
        
        QSlider::groove:horizontal {
            border: 1px solid #333333;
            height: 8px;
            background-color: #1A1A1A;
            border-radius: 4px;
        }
        
        QSlider::handle:horizontal {
            background-color: #3498DB;
            border: 1px solid #2980B9;
            width: 18px;
            height: 18px;
            margin: -5px 0;
            border-radius: 9px;
        }
        
        QSlider::handle:horizontal:hover {
            background-color: #2980B9;
        }
    """
    show_error : str = """
        QMessageBox {
            background-color: #121212;
            font-size: 14px;
            border-radius: 10px;
        }
        QMessageBox QLabel {
            color: #FFFFFF;
            margin: 15px 15px 15px 25px;  
            font-weight: 500;
        }
        QMessageBox QPushButton {
            background-color: #2C2C2C;
            color: #FFFFFF;
            border: none;
            padding: 8px 16px;
            border-radius: 8px;
            font-weight: 500;
            min-width: 80px;
            min-height: 30px;
        }

        QMessageBox QPushButton:hover {
            background-color: #3498DB;
        }

        QMessageBox QPushButton:pressed {
            background-color: #2980B9;
        }
    """
    privacy_policies_popup : str = """
        QDialog {
            background-color: #121212;
            font-size: 14px;
            margin: 15px;  
            border-radius: 12px;
        }
        QDialog QLabel {
            color: #FFFFFF;
            margin: 15px;  
            font-weight: 500;
            line-height: 145%;
        }
        QDialog QWidget {
            background-color: #121212;
            border-radius: 8px;
        }
        QDialog QScrollBar:vertical {
            border: none;
            background-color: #1A1A1A;
            width: 10px;
            margin: 0px 0px 0px 0px;
            border-radius: 5px;
        }

        QDialog QScrollBar::handle:vertical {
            background-color: #3498DB;
            min-height: 25px;
            border-radius: 5px;
        }
            
        QDialog QScrollBar::handle:vertical:hover {
            background-color: #2980B9;
        }
        
        QDialog QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            border: none;
            background: none;
            height: 0px;
        }
    """
    ppp_accept_btn : str = """
        QDialog QPushButton {
            background-color: #27AE60;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 8px;
            font-weight: 600;
            font-size: 14px;
        }
        QDialog QPushButton:hover {
            background-color: #219653;
        }
        QDialog QPushButton:pressed {
            background-color: #1E8449;
        }
    """

    ppp_denied_btn : str = """
        QDialog QPushButton {
            background-color: #E74C3C;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 8px;
            font-weight: 600;
            font-size: 14px;
        }
        QDialog QPushButton:hover {
            background-color: #C0392B;
        }
        QDialog QPushButton:pressed {
            background-color: #A93226;
        }
    """
