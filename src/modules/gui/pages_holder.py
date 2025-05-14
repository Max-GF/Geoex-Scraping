"""
    Module that contains the main file
    for running the application,
    so here are the functions necessary
    to create the Pyside6 instance
    and modify it according to the desired parameters
"""
import sys
import os
from dotenv import load_dotenv
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import (QMainWindow, QFrame, QHBoxLayout,
                               QVBoxLayout, QStackedWidget, QLabel,
                               QSpacerItem, QSizePolicy, QPushButton,
                               QWidget, QSizeGrip)
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt, QPoint, QPropertyAnimation, QEasingCurve
from src.modules.load_configs.load_icons_and_images_paths import ImgAndIconsPath
from src.modules.gui.pop_ups.privacy_policies import PrivacyPolicies
from src.modules.gui.style_sheet import StyleSheets
from src.modules.gui.pop_ups.helper import HelpPopUp
from src.modules.gui.pages_compiler import UiPagesWidget



load_dotenv()
APP_NAME = os.getenv("APP_NAME")

class UiMainWindow(QMainWindow):
    """
        Class that create the main window
        and all the components inside of it

    Args:
        QMainWindow (QMainWindow): Pyside6 original class
    """
    def __init__(self) -> None:
        super().__init__()
        self.central_frame : QFrame
        self.main_layout : QHBoxLayout
        self.draggable : bool = True
        self.drag_pos : QPoint
        self.sidebar : QWidget
        self.sidebar_buttons : list[QPushButton] = []
        self.page_holder : QStackedWidget
        self.pages : UiPagesWidget
        self.status_label : QLabel
        self.setup_ui()

    def setup_ui(self):
        """ 
        Setup main window parameters
        """

        # Setting the window name
        if not self.objectName():
            self.setObjectName("MainWindow")

        # Setting window size parameters
        self.resize(850,650)
        self.setMinimumSize(850,650)
        self.setWindowFlag(Qt.FramelessWindowHint) # Remove base title bar provided by Windowns

        # Setting central frame
        self.central_frame = QFrame()
        self.central_frame.setStyleSheet(StyleSheets.main_window)
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)

        # Creating instances
        self.__create_side_bar()
        self.__create_content_area()
        self.__create_title_bar()

        # Adding things to main layout
        self.setCentralWidget(self.central_frame)

        # Setting buttons functions

    def __create_content_area(self) -> None:
        """
            Function that create content area
        """

        # Setting content and adding it to central frame
        content_frame : QFrame = QFrame()
        content_frame.setStyleSheet(StyleSheets.content)
        content_layout : QVBoxLayout = QVBoxLayout(content_frame)
        content_layout.setContentsMargins(0,0,0,0)
        content_layout.setSpacing(0)

        # Setting content page holder
        self.page_holder = QStackedWidget()
        self.page_holder.setStyleSheet(StyleSheets.page_holder)
        self.pages = UiPagesWidget()
        self.pages.setup_ui(self.page_holder)
        content_layout.addWidget(self.page_holder)

        # Setting content footnote
        footnote = QFrame()
        footnote.setMinimumHeight(15)
        footnote.setMaximumHeight(15)
        footnote.setStyleSheet(StyleSheets.header_footnote)
        footnote_label = QLabel("Feito por Max Gambarini Filho")
        footnote_label2 = QLabel("v1.0.0")
        footnote_layout = QHBoxLayout(footnote)
        footnote_layout.setContentsMargins(10,0,0,0)
        footnote_layout.addWidget(footnote_label)
        footnote_layout.addItem(QSpacerItem(30,30,QSizePolicy.Expanding,QSizePolicy.Minimum))
        footnote_layout.addWidget(footnote_label2)
        size_grip = QSizeGrip(self)
        size_grip.setStyleSheet(StyleSheets.resize_button)
        footnote_layout.addWidget(size_grip)
        content_layout.addWidget(footnote)

        self.main_layout.addWidget(content_frame)

    def __create_side_bar(self) -> None:
        """
            Function that create sidebar
        """

        # Setting side bar layout
        sidebar_layout : QVBoxLayout = QVBoxLayout()
        sidebar_layout.setContentsMargins(7.5, 10, 0, 15)
        sidebar_layout.setSpacing(0)
        sidebar_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        # Expand side bar button
        expand_side_bar_button = QPushButton(cursor=Qt.PointingHandCursor,
                                             icon=QIcon(ImgAndIconsPath.expand_sidebar))
        expand_side_bar_button.setStyleSheet(StyleSheets.side_bar_button)
        expand_side_bar_button.clicked.connect(self.__resize_sidebar)
        self.sidebar_buttons.append(expand_side_bar_button)

        # Home button
        btn_home = QPushButton("\t\t\tHome",
                                cursor=Qt.PointingHandCursor,
                                icon=QIcon(ImgAndIconsPath.home_btn))
        btn_home.setCheckable(True)
        btn_home.setStyleSheet(StyleSheets.side_bar_button)
        btn_home.clicked.connect(lambda : self.__change_page(page=self.pages.home,
                                                             clicked_btn=btn_home))
        self.sidebar_buttons.append(btn_home)

        geoex_page_btn : QPushButton = QPushButton("\t\t\tGeoex Scrapper",
                                               icon=QIcon(ImgAndIconsPath.geoex_page_btn),
                                               cursor=Qt.PointingHandCursor)
        geoex_page_btn.setCheckable(True)
        geoex_page_btn.setStyleSheet(StyleSheets.side_bar_button)
        geoex_page_btn.clicked.connect(lambda : self.__change_page(page=self.pages.geoex_page,
                                                               clicked_btn=geoex_page_btn))
        self.sidebar_buttons.append(geoex_page_btn)

        # Lower side bar button
        bottom_side_bar_button : QPushButton = QPushButton("\t\t\tPolíticas de privacidade",
                                                           cursor=Qt.PointingHandCursor,
                                                           icon=QIcon(ImgAndIconsPath.privacy))
        bottom_side_bar_button.setCheckable(True)
        bottom_side_bar_button.setStyleSheet(StyleSheets.side_bar_button)
        bottom_side_bar_button.clicked.connect(
            lambda : self.__show_privacy_popup(clicked_btn=bottom_side_bar_button))
        self.sidebar_buttons.append(bottom_side_bar_button)


        # Adding button to sidebar layout
        sidebar_layout.addWidget(expand_side_bar_button)
        sidebar_layout.addWidget(btn_home)
        sidebar_layout.addWidget(geoex_page_btn)
        spacer : QWidget = QWidget()
        spacer.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sidebar_layout.addWidget(spacer)
        sidebar_layout.addWidget(bottom_side_bar_button)

        self.sidebar : QFrame = QFrame()
        self.sidebar.setStyleSheet(StyleSheets.side_bar)
        self.sidebar.setMaximumWidth(50)
        self.sidebar.setMinimumWidth(50)
        self.sidebar.setLayout(sidebar_layout)


        self.main_layout.addWidget(self.sidebar)

    def __create_title_bar(self) -> None:
        """
            Create app title bar
        """

        # Create a layout for the title bar
        title_bar_layout : QHBoxLayout = QHBoxLayout()
        title_bar_layout.setAlignment(Qt.AlignRight)
        title_bar_layout.setContentsMargins(15, 0, 0, 0)

        # Add title image
        image_label : QLabel = QLabel()
        pixmap : QPixmap = QPixmap(ImgAndIconsPath.logo_image)
        image_label.setPixmap(pixmap.scaled(25, 25))
        title_bar_layout.addWidget(image_label)

        # Add title label
        title_label : QLabel = QLabel(APP_NAME)
        title_label.setStyleSheet("font-size: 16px; color: white;")  # Estilos para o texto
        title_bar_layout.addWidget(title_label)
        spacer : QWidget = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        title_bar_layout.addWidget(spacer)

        # Build title bar help button
        question_mark : QPushButton = QPushButton(cursor=Qt.PointingHandCursor,
                                                  icon=QIcon(ImgAndIconsPath.question_mark))
        question_mark.setStyleSheet(StyleSheets.title_bar_button)
        question_mark.clicked.connect(lambda name: HelpPopUp().show_message(name))
        title_bar_layout.addWidget(question_mark)

        # Build title bar minimize button
        btn_minimize : QPushButton = QPushButton(cursor=Qt.PointingHandCursor,
                                                 icon=QIcon(ImgAndIconsPath.minimize_icon))
        btn_minimize.setStyleSheet(StyleSheets.title_bar_button)
        btn_minimize.clicked.connect(self.showMinimized)
        title_bar_layout.addWidget(btn_minimize)

        # Build title bar maximize button
        btn_maximize : QPushButton = QPushButton(cursor=Qt.PointingHandCursor,
                                                 icon=QIcon(ImgAndIconsPath.maximize_icon))
        btn_maximize.setStyleSheet(StyleSheets.title_bar_button)
        btn_maximize.clicked.connect(
            lambda : self.showNormal() if self.isMaximized() else self.showMaximized())
        title_bar_layout.addWidget(btn_maximize)

        # Build title bar close button
        btn_close : QPushButton = QPushButton(cursor=Qt.PointingHandCursor,
                                              icon=QIcon(ImgAndIconsPath.close_icon))
        btn_close.setStyleSheet(StyleSheets.title_bar_button)
        btn_close.clicked.connect(self.close)
        title_bar_layout.addWidget(btn_close)

        # Build top bar widget
        title_bar_widget : QWidget = QWidget()
        title_bar_widget.setLayout(title_bar_layout)
        title_bar_widget.setStyleSheet(StyleSheets.title_bar)
        title_bar_widget.setMaximumHeight(30)

        # Allows the window to be moved when clicking the title bar
        title_bar_widget.mousePressEvent = self.__mouse_press_event
        title_bar_widget.mouseMoveEvent = self.__mouse_move_event
        self.setMenuWidget(title_bar_widget)

    def __mouse_press_event(self, event) -> None:
        """ 
            Use mouse press "event" inside of window
            to get his actual position
        """
        # Checks if the click occurred within the title bar
        if event.button() == Qt.LeftButton and event.y() < 30:
            self.draggable = True
            self.drag_pos = event.globalPosition() - self.frameGeometry().topLeft()
            event.accept()
        else:
            self.draggable = False
            event.ignore()

    def __mouse_move_event(self, event) -> None:
        """ 
            Use mouse move "event" inside of window
            to get his actual position and move
            the window to
        """
        if event.buttons() == Qt.LeftButton and self.draggable:
            global_pos = event.globalPosition().toPoint()
            drag_pos = self.drag_pos.toPoint()
            self.move(global_pos - drag_pos)
            event.accept()

    def __resize_sidebar(self) -> None:
        """ 
            Resize side bar 50px <=> 200px
        """
        if self.sidebar.width() == 50:
            aux = 205
        else:
            aux = 50

        animation = QPropertyAnimation(self.sidebar, b"minimumWidth", self)
        animation.setStartValue(self.sidebar.width())
        animation.setEndValue(aux)
        animation.setDuration(800)  # Animation duration in milliseconds
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start()

    def __change_state_sidebar_buttons(self,clicked_btn : QPushButton) -> None:
        """
            As the name says, this functions
            disable all others buttons
            except the one in args
            
        Args:
            clicked_btn (QPushButton): Clicked button
        """
        for button in self.sidebar_buttons:
            if button != clicked_btn and button.isChecked():
                button.setChecked(False)

    def __change_page(self, page: QWidget , clicked_btn : QPushButton) -> None:
        """
            Change Page Holder active page

        Args:
            clicked_btn (QPushButton): Clicked button
            page (QWidget): Wanted page
        """
        self.__change_state_sidebar_buttons(clicked_btn=clicked_btn)
        self.page_holder.setCurrentWidget(page)

    def __show_privacy_popup(self, clicked_btn : QPushButton) -> None:
        """
            Show privacy pop-up again
            
        Args:
            clicked_btn (QPushButton): Clicked button
        """
        self.__change_state_sidebar_buttons(clicked_btn=clicked_btn)
        PrivacyPolicies().show_message()


if __name__ == "__main__":
    # Example usage
    app = QApplication(sys.argv)

    window = UiMainWindow()
    window.show()

    sys.exit(app.exec())
