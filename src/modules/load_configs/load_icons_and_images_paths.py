"""
    Window images and icons paths
"""
import os
from dotenv import load_dotenv
load_dotenv( override=True )

class ImgAndIconsPath:
    """ 
        Class that hold all images and icons paths
    """
    # TOP BAR
    minimize_icon : str = os.path.join(
        os.getcwd(),
        os.getenv("MINIMIZE_ICON_PATH")
        )
    maximize_icon : str = os.path.join(
        os.getcwd(),
        os.getenv("MAXIMIZE_ICON_PATH")
        )
    close_icon : str = os.path.join(
        os.getcwd(),
        os.getenv("CLOSE_ICON_PATH")
        )
    question_mark : str = os.path.join(
        os.getcwd(),
        os.getenv("HELP_ICON_PATH")
        )
    logo_image : str = os.path.join(
        os.getcwd(),
        os.getenv("TITLE_ICON_PATH")
        )

    # SIDE BAR
    expand_sidebar : str = os.path.join(
        os.getcwd(),
        os.getenv("EXPAND_SIDEBAR_ICON_PATH")
        )
    home_btn : str = os.path.join(
        os.getcwd(),
        os.getenv("HOME_BUTTON_ICON_PATH")
        )
    geoex_page_btn : str = os.path.join(
        os.getcwd(),
        os.getenv("GEOEX_PAGE_BUTTON_ICON_PATH")
        )
    privacy : str = os.path.join(
        os.getcwd(),
        os.getenv("PRIVACY_POLICIES_ICON_PATH")
        )

    # HOME
    home_image : str = os.path.join(
        os.getcwd(),
        os.getenv("HOME_LOGO_PATH")
        )

    # BOTTON BAR
    resize_button : str = os.path.join(
        os.getcwd(),
        os.getenv("RESIZE_BUTTON_ICON_PATH")
        ).replace("\\", "/")

    # GEOEX PAGE
    woking_gif : str = os.path.join(
        os.getcwd(),
        os.getenv("WORKING_GIF_PATH")
        )

    # TASK BAR
    task_bar_icon : str = os.path.join(
        os.getcwd(),
        os.getenv("TASK_ICON_PATH")
        )
