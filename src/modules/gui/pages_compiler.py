"""
    Internal pages pyside6 module
"""
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PySide6.QtWidgets import QStackedWidget
from src.modules.gui.pages.start_page import StartPage
from src.modules.gui.pages.geoex_page import GeoexPage
from src.modules.scrappers.geoex_scrapper import GeoexScraper



class UiPagesWidget:
    """
    Helper class to set up pages in a QStackedWidget.
    It does not inherit from QWidget itself.
    """
    def __init__(self) -> None:
        """Initializes page references."""
        self.home: StartPage | None = None
        self.geoex_page: GeoexPage | None = None

    def setup_ui(self, pages_widget: QStackedWidget):
        """
            Sets up content pages within the provided QStackedWidget.

        Args:
            pages_widget (QStackedWidget): The widget to add pages to.
        """
        if not pages_widget.objectName():
            pages_widget.setObjectName("PagesWidget")

        self.home = StartPage()
        self.geoex_page = GeoexPage(GeoexScraper())

        pages_widget.addWidget(self.home)
        pages_widget.addWidget(self.geoex_page)

        pages_widget.setCurrentIndex(0)

if __name__ == "__main__":
    # Example usage
    # Change pages_widget.setCurrentIndex(index) to the desired page index

    app = QApplication([])

    main_window = QWidget()
    layout = QVBoxLayout(main_window)
    page_widget = QStackedWidget()
    layout.addWidget(page_widget)

    ui_pages = UiPagesWidget()
    ui_pages.setup_ui(page_widget)

    main_window.show()
    app.exec()
