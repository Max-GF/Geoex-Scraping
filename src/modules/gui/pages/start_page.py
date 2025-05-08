"""
    Start Page Builder
"""
from PySide6.QtCore import (QSize, Qt)
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel,
                               QSizePolicy, QSpacerItem,
                               QVBoxLayout, QWidget)
from src.modules.load_configs.load_icons_and_images_paths import ImgAndIconsPath

def start_page_builder() -> QWidget:
    """
                         HOME PAGE
    ◸——————————————————————————————————————————————————◹
    |                        ↑                          |
    |                    TOP SPACER                     |
    |                        ↓                          |
    |                    ◸———————◹                     |
    |  ← LEFT SPACER →   |  LOGO  |   ← RIGHT SPACER →  |
    |                    ◺———————◿                     |
    |                        ↑                          |
    |                    BOT SPACER                     |
    |                        ↓                          |
    ◺——————————————————————————————————————————————————◿

    Returns:
        QWidget: Home page widget
    """

    home = QWidget()
    home_layout_v = QVBoxLayout(home)

    home_frame = QFrame(home)
    home_frame.setFrameShape(QFrame.StyledPanel)
    home_frame.setFrameShadow(QFrame.Raised)
    home_frame_layout = QVBoxLayout(home_frame)

    top_logo_spacer = QSpacerItem(
        20,
        1000,
        QSizePolicy.Policy.Minimum,
        QSizePolicy.Policy.Maximum
        )

    home_frame_layout.addItem(top_logo_spacer)

    logo_holder = QWidget(home_frame)
    logo_holder_layout = QHBoxLayout(logo_holder)
    lef_logo_spacer = QSpacerItem(
        1000,
        20,
        QSizePolicy.Policy.Expanding,
        QSizePolicy.Policy.Minimum
        )

    logo_holder_layout.addItem(lef_logo_spacer)

    logo = QLabel(logo_holder)
    logo.setEnabled(True)
    size_policy = QSizePolicy(
        QSizePolicy.Policy.Expanding,
        QSizePolicy.Policy.Expanding
        )
    size_policy.setHorizontalStretch(0)
    size_policy.setVerticalStretch(0)
    size_policy.setHeightForWidth(logo.sizePolicy().hasHeightForWidth())
    logo.setSizePolicy(size_policy)
    logo.setMinimumSize(QSize(1, 1))
    logo.setTextFormat(Qt.AutoText)
    logo.setPixmap(QPixmap(ImgAndIconsPath.home_image))
    logo.setScaledContents(True)
    logo.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
    logo_holder_layout.addWidget(
        logo,
        0,
        Qt.AlignRight|Qt.AlignVCenter
        )

    rig_logo_spacer = QSpacerItem(
        1000,
        20,
        QSizePolicy.Policy.Maximum,
        QSizePolicy.Policy.Minimum
        )
    logo_holder_layout.addItem(rig_logo_spacer)

    home_frame_layout.addWidget(
        logo_holder,
        0,
        Qt.AlignHCenter|Qt.AlignVCenter
        )

    bot_logo_spacer = QSpacerItem(
        20,
        1000,
        QSizePolicy.Policy.Minimum,
        QSizePolicy.Policy.Maximum
        )
    home_frame_layout.addItem(bot_logo_spacer)

    home_layout_v.addWidget(home_frame)

    return home
