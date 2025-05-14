"""
    Worker class to perform scraping operations in a separate thread.
"""
from PySide6.QtCore import QObject, Signal, Slot
from src.modules.scrappers.geoex_scrapper import GeoexScraper


class ScraperWorker(QObject):
    """
         Worker class to perform scraping operations in a separate thread.
    """
    finished = Signal(str, bool, str)
    progress = Signal(str, int)

    def __init__(
        self,
        scraper: GeoexScraper,
        operation_type: str,
        credentials: dict,
        project_ids: list,
        gs_id: str,
        gs_range: str
        ):
        super().__init__()
        self.scraper = scraper
        self.operation_type = operation_type # "general", "budget", "rejections"
        self.credentials = credentials
        self.project_ids = project_ids
        self.gs_id = gs_id
        self.gs_range = gs_range
        self._is_cancelled = False

    @Slot()
    def run(self):
        """
        Execute the scraping task.
        """
        success = False
        message = ""
        try:
            if self.operation_type == "general":
                success, message = self.scraper.scrape_projects_infos(
                    self.credentials,
                    self.project_ids,
                    self.gs_id,
                    self.gs_range,
                    lambda val: self.progress.emit(self.operation_type, val)
                )
            elif self.operation_type == "budget":
                success, message = self.scraper.scrape_projects_budgets(
                    self.credentials,
                    self.project_ids,
                    self.gs_id,
                    self.gs_range,
                    lambda val: self.progress.emit(self.operation_type, val)
                )
            elif self.operation_type == "rejections":
                success, message = self.scraper.scrape_projects_rejection_details(
                    self.credentials,
                    self.project_ids,
                    self.gs_id,
                    self.gs_range,
                    lambda val: self.progress.emit(self.operation_type, val)
                )
            else:
                message = "Tipo de operação desconhecido."
                success = False
        except Exception as e: # pylint: disable=W0718
            success = False
            message = f"Erro inesperado no worker: {e}"
        finally:
            self.finished.emit(self.operation_type, success, message)

    def cancel(self):
        """
            Cancel the scraping operation.
        """
        self._is_cancelled = True
        print(f"Worker {self.operation_type} solicitado para cancelar.")
