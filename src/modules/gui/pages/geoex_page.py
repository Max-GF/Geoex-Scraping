"""
    Needed functions and classes to create the geoex page
    and its widgets, buttons and layout.
"""
import os
import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout,
    QHBoxLayout, QGroupBox, QPushButton,
    QTableWidget, QTableWidgetItem, QScrollArea,
    QGridLayout,QLineEdit,QProgressBar,QMessageBox
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QMovie,QKeySequence
from src.modules.scrappers.geoex_scrapper import GeoexScraper
from src.modules.gui.style_sheet import StyleSheets
from src.modules.load_configs.load_icons_and_images_paths import ImgAndIconsPath

class GeoexPage(QWidget):
    """
        Geoex page that holds all the widgets and buttons
        needed to collect data from the geoex website
        and send it to the google sheets.

    Args:
        QWidget (_type_): PySide6 QWidget class
    """
    def __init__(self, scraper: GeoexScraper):
        """
            Constructor of the GeoexPage class.

        Args:
            scraper (GeoexScraper): GeoexScraper to be used
        """
        super().__init__()
        self.setWindowTitle("Coletor de Dados Geoex")
        self.setMinimumSize(800, 600)
        self.scraper = scraper

        # Page Buttons
        self.collect_general_button = None
        self.collect_budget_button = None
        self.collect_rejections_button = None

        # Page inputs
        self.cookies_input = None
        self.session_id_input = None
        self.bot_id_input = None
        self.gs_id_input = None
        self.gs_range_input = None

        # Page tables
        self.project_table = None

        # Page general widgets
        self.execution_box = None
        self.loading_bar = None
        self.robo_label = None
        self.robo_movie = None
        self.static_robo_pixmap = None

        self.build_page()
        self.connect_signals()
        self.setStyleSheet(StyleSheets.pages)

        if self.execution_box:
            self.execution_box.setVisible(False)

    def build_page(self):
        """
            Main function to build the page and its widgets
        """
        main_layout = QGridLayout(self)
        main_layout.setColumnStretch(0, 1)
        main_layout.setColumnStretch(1, 1)
        main_layout.setColumnStretch(2, 1)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(15, 15, 15, 15)

        buttons_box = self.build_buttons_group()
        main_layout.addWidget(buttons_box, 0, 0, 1, 3)

        projects_table_box = self.build_projects_table()
        main_layout.addWidget(projects_table_box, 1, 0, 2, 1)

        geoex_box = self.build_geoex_group()
        main_layout.addWidget(geoex_box, 1, 1)

        gs_box = self.build_google_sheets_group()
        main_layout.addWidget(gs_box, 2, 1)

        self.execution_box = self.build_execution_group()
        main_layout.addWidget(self.execution_box, 1, 2, 2, 1)

    def build_buttons_group(self) -> QGroupBox:
        """
            Build the buttons group.
            Remember to add the buttons in the init function
            and connect the signals to the buttons.
            

        Returns:
            QGroupBox: GroupBox with the buttons
        """
        buttons_box = QGroupBox("Tipos de coleta no Geoex por projeto")
        buttons_layout = QHBoxLayout()
        self.collect_general_button = QPushButton("Dados Gerais")
        self.collect_budget_button = QPushButton("Detalhes dos Orçamentos")
        self.collect_rejections_button = QPushButton("Detalhes das Rejeições")
        buttons_layout.addWidget(self.collect_general_button)
        buttons_layout.addWidget(self.collect_budget_button)
        buttons_layout.addWidget(self.collect_rejections_button)
        buttons_layout.addStretch(1)
        buttons_box.setMinimumWidth(400)
        buttons_box.setMaximumHeight(100)
        buttons_box.setLayout(buttons_layout)
        return buttons_box

    def build_projects_table(self) -> QGroupBox:
        """
            Build the projects table group.

        Returns:
            QGroupBox: GroupBox with the projects table
        """
        table_box = QGroupBox("Projetos para Coleta")
        table_layout = QVBoxLayout()
        self.project_table = PasteAwareTableWidget()
        self.project_table.setColumnCount(1)
        self.project_table.setHorizontalHeaderLabels(["Lista de projetos"])
        self.project_table.horizontalHeader().setStretchLastSection(True)
        self.project_table.verticalHeader().setVisible(False)
        self.project_table.setAlternatingRowColors(True)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.project_table)
        table_layout.addWidget(scroll_area)
        table_box.setLayout(table_layout)
        return table_box

    def build_geoex_group(self) -> QGroupBox:
        """
            Build the geoex group with the credentials needed.

        Returns:
            QGroupBox: GroupBox with the geoex credentials
        """
        geoex_box = QGroupBox("Credenciais Geoex")
        geoex_layout = QVBoxLayout()
        geoex_layout.addWidget(QLabel("Cookies:"))
        self.cookies_input = QLineEdit(placeholderText="Insira os cookies do Geoex")
        geoex_layout.addWidget(self.cookies_input)
        geoex_layout.addWidget(QLabel("Session ID:"))
        self.session_id_input = QLineEdit(placeholderText="Insira o GxSessao ID do Geoex")
        geoex_layout.addWidget(self.session_id_input)
        geoex_layout.addWidget(QLabel("Bot ID:"))
        self.bot_id_input = QLineEdit(placeholderText="Insira o GxBot ID do Geoex")
        geoex_layout.addWidget(self.bot_id_input)
        geoex_box.setLayout(geoex_layout)
        return geoex_box

    def build_google_sheets_group(self) -> QGroupBox:
        """
            Build the google sheets group with the credentials needed.

        Returns:
            QGroupBox: GroupBox with the google sheets credentials
        """
        gs_box = QGroupBox("Configuração Google Sheets")
        gs_layout = QVBoxLayout()
        gs_layout.addWidget(QLabel("ID da Planilha:"))
        self.gs_id_input = QLineEdit(placeholderText="Insira o ID da planilha do Google Sheets")
        gs_layout.addWidget(self.gs_id_input)
        gs_layout.addWidget(QLabel("Intervalo de Dados:"))
        self.gs_range_input = QLineEdit(placeholderText="Ex: 'Página1'!A1:Z100")
        gs_layout.addWidget(self.gs_range_input)
        gs_box.setLayout(gs_layout)
        return gs_box

    def build_execution_group(self) -> QGroupBox:
        """
            Build the execution group with the
            progress bar and the gif.
            The gif is loaded from the 
            ImgAndIconsPath.woking_gif path.
            If the gif is not found, a static
            pixmap is used instead.

        Returns:
            QGroupBox: GroupBox with the execution group
        """
        execution_box = QGroupBox("Status da Execução")
        execution_layout = QVBoxLayout()
        execution_layout.setSpacing(15)
        self.loading_bar = QProgressBar()
        self.loading_bar.setRange(0, 100)
        self.loading_bar.setValue(0)
        self.loading_bar.setTextVisible(True)
        self.loading_bar.setAlignment(Qt.AlignCenter)
        self.loading_bar.setFixedHeight(25)
        execution_layout.addWidget(self.loading_bar)
        self.robo_label = QLabel()
        self.robo_label.setFixedSize(QSize(300, 400))
        self.robo_label.setAlignment(Qt.AlignCenter)
        self.robo_label.setStyleSheet("background-color: #E8E8E8; border: 1px solid #D0D0D0; border-radius: 5px;")
        gif_path = ImgAndIconsPath.woking_gif
        if not os.path.exists(gif_path):
            print(f"Aviso: Caminho do GIF '{gif_path}' não existe. Animação não será carregada.")
            self.robo_label.setText("Animação Indisponível")
            self.robo_movie = None
            self.static_robo_pixmap = None
        else:
            self.robo_movie = QMovie(gif_path)
            if not self.robo_movie.isValid() or self.robo_movie.frameCount() == 0:
                print(f"Erro: Não foi possível carregar o GIF de '{gif_path}' ou o GIF está vazio.")
                self.robo_label.setText("Erro ao carregar GIF")
                self.robo_movie = None
                self.static_robo_pixmap = None
            else:
                self.robo_movie.jumpToFrame(0)
                self.static_robo_pixmap = self.robo_movie.currentPixmap().copy()
                self.robo_label.setPixmap(self.static_robo_pixmap)
        execution_layout.addWidget(self.robo_label, alignment=Qt.AlignCenter)
        execution_box.setLayout(execution_layout)
        return execution_box

    def connect_signals(self):
        """
            Connect the signals to the buttons and inputs.
            The buttons are connected to the functions
        """
        if self.collect_general_button:
            self.collect_general_button.clicked.connect(self.collect_general_data)
        if self.collect_budget_button:
            self.collect_budget_button.clicked.connect(self.collect_budget_data)
        if self.collect_rejections_button:
            self.collect_rejections_button.clicked.connect(self.collect_rejections_data)

    def _update_progress_from_scraper(
        self,
        current_value: int,
        ):
        """
            Update the progress bar with scrapper callback.

        Args:
            current_value (int): current value of the progress bar
        """
        if self.loading_bar:
            self.loading_bar.setValue(current_value)
        QApplication.processEvents()

    def _get_project_ids_from_table(self) -> list:
        """Extrai os IDs dos projetos da tabela."""
        ids = []
        if self.project_table:
            for row in range(self.project_table.rowCount()):
                item = self.project_table.item(row, 0)
                if item and item.text():
                    ids.append(item.text())
        return ids

    def _start_processing_ui(self, action_name: str):
        """Configura a UI para o início do processamento."""
        print(f"UI: Iniciando {action_name}")
        if self.execution_box:
            self.execution_box.setVisible(True)

        num_projects = self.project_table.rowCount() # ou len(self._get_project_ids_from_table())
        if num_projects == 0:
            self.loading_bar.setRange(0, 1)
            self.loading_bar.setValue(0)
            self.loading_bar.setFormat("Nenhum projeto selecionado")
            if self.static_robo_pixmap:
                self.robo_label.setPixmap(self.static_robo_pixmap)
            else: self.robo_label.setText("Pronto")
            QMessageBox.information(self, "Sem Projetos", "Nenhum projeto na tabela para processar.")
            return False # Indica que não há projetos

        self.loading_bar.setRange(0, num_projects)
        self.loading_bar.setValue(0)
        self.loading_bar.setFormat(f"{action_name}: %v / %m")

        if self.robo_movie and self.robo_movie.isValid():
            self.robo_label.setMovie(self.robo_movie)
            self.robo_movie.start()
        else:
            self.robo_label.setText(f"Processando {action_name}...")
        self.set_buttons_enabled(False)
        return True # Indica que o processamento pode começar

    def _finish_processing_ui(self, action_name: str, success: bool, message: str):
        """Restaura a UI após o término do processamento."""
        print(f"UI: Concluído {action_name} - Sucesso: {success}, Mensagem: {message}")
        if success:
            self.loading_bar.setValue(self.loading_bar.maximum()) # Garante que a barra vá até o fim
            self.loading_bar.setFormat(f"{action_name}: Concluído!")
            QMessageBox.information(self, "Sucesso", message)
        else:
            self.loading_bar.setFormat(f"{action_name}: Erro!")
            QMessageBox.warning(self, "Erro", message)


        if self.robo_movie and self.robo_movie.isValid():
            self.robo_movie.stop()
            if self.static_robo_pixmap:
                self.robo_label.setPixmap(self.static_robo_pixmap)
        elif self.static_robo_pixmap: # Se o filme não era válido, mas temos o pixmap
            self.robo_label.setPixmap(self.static_robo_pixmap)
        else: # Fallback
            self.robo_label.setText("Pronto")

        # Considerar esconder a caixa de execução após um tempo ou deixar visível com o status final
        if self.execution_box:
            self.execution_box.setVisible(False) # Para esconder imediatamente

        self.set_buttons_enabled(True)

    # --- Métodos de Coleta (Delegam ao Scraper) ---
    def collect_general_data(self):
        """
            Collect the general data from the geoex website
            and send it to the google sheets.
            The function is called when the user clicks on the
            collect_general_button.
        """
        if not self._start_processing_ui("Dados Gerais"):
            self.set_buttons_enabled(True)
            return

        project_ids = self._get_project_ids_from_table()
        cookies = self.cookies_input.text()
        session_id = self.session_id_input.text()
        bot_id = self.bot_id_input.text()

        if not all([cookies, session_id, bot_id]):
            QMessageBox.warning(
                self,
                "Entradas Faltando",
                "Por favor, preencha todos os campos de Credenciais Geoex."
                )
            self._finish_processing_ui("Dados Gerais", False, "Entradas Geoex incompletas.")
            return

        try:
            success, message = self.scraper.scrape_projects_infos(
                {
                    "cookies": cookies,
                    "gxsessao": session_id,
                    "gxbot": bot_id,
                },
                project_ids,
                self.gs_id_input.text(),
                self.gs_range_input.text(),
                self._update_progress_from_scraper,
            )
        except Exception as e: # pylint: disable=<W0718>
            print(f"Erro ao chamar scraper.scrape_general_data: {e}")
            success = False
            message = f"Erro inesperado na interface: {e}"
        finally:
            self._finish_processing_ui("Dados Gerais", success, message)

    def collect_budget_data(self):
        """
            Collect the budget data from the geoex website
            and send it to the google sheets.
            The function is called when the user clicks on the
            collect_budget_button.
        """
        if not self._start_processing_ui("Orçamento"):
            self.set_buttons_enabled(True)
            return
        project_ids = self._get_project_ids_from_table()
        cookies = self.cookies_input.text()
        session_id = self.session_id_input.text()
        bot_id = self.bot_id_input.text()
        if not all([cookies, session_id, bot_id]):
            QMessageBox.warning(self, "Entradas Faltando", "Por favor, preencha todos os campos de Credenciais Geoex.")
            self._finish_processing_ui("Orçamento", False, "Entradas Geoex incompletas.")
            return
        try:
            success, message = self.scraper.scrape_projects_budgets(
                {
                    "cookies": cookies,
                    "gxsessao": session_id,
                    "gxbot": bot_id,
                },
                project_ids,
                self.gs_id_input.text(),
                self.gs_range_input.text(),
                self._update_progress_from_scraper,
            )
        except Exception as e: # pylint: disable=<W0718>
            success = False
            message = f"Erro inesperado na interface: {e}"
        finally:
            self._finish_processing_ui("Orçamento", success, message)

    def collect_rejections_data(self):
        """
            Collect the rejections data from the geoex website
            and send it to the google sheets.
            The function is called when the user clicks on the
            collect_rejections_button.
        """
        if not self._start_processing_ui("Rejeições"):
            self.set_buttons_enabled(True)
            return
        project_ids = self._get_project_ids_from_table()
        cookies = self.cookies_input.text()
        session_id = self.session_id_input.text()
        bot_id = self.bot_id_input.text()
        if not all([cookies, session_id, bot_id]):
            QMessageBox.warning(
                self,
                "Entradas Faltando",
                "Por favor, preencha todos os campos de Credenciais Geoex."
                )
            self._finish_processing_ui(
                "Rejeições",
                False,
                "Entradas Geoex incompletas.")
            return
        try:
            success, message = self.scraper.scrape_projects_rejection_details(
                {
                    "cookies": cookies,
                    "gxsessao": session_id,
                    "gxbot": bot_id,
                },
                project_ids,
                self.gs_id_input.text(),
                self.gs_range_input.text(),
                self._update_progress_from_scraper,
            )
        except Exception as e: # pylint: disable=<W0718>
            success = False
            message = f"Erro inesperado na interface: {e}"
        finally:
            self._finish_processing_ui("Rejeições", success, message)

    def set_buttons_enabled(
        self,
        enabled: bool
        ):
        """
            Enable or disable the buttons on the page.

        Args:
            enabled (bool): True to enable the buttons, False to disable them
        """
        if self.collect_general_button:
            self.collect_general_button.setEnabled(enabled)
        if self.collect_budget_button:
            self.collect_budget_button.setEnabled(enabled)
        if self.collect_rejections_button:
            self.collect_rejections_button.setEnabled(enabled)

class PasteAwareTableWidget(QTableWidget):
    """
    A QTableWidget subclass that handles pasting (Ctrl+V) from the clipboard.
    Assumes single-column data separated by newlines.
    """

    def keyPressEvent(self, event): # pylint: disable=<C0103>
        """
        Handle key press events. If Ctrl+V (or Cmd+V on Mac) is pressed,
        paste the text from the clipboard into the table.
        This function does't conform with snake_case naming convention
        because it overrides the keyPressEvent method of QTableWidget.
        Args:
            event (_type_): Keyboard event to handle

        """
        # This overrides only applys to the paste action
        if event.matches(QKeySequence.StandardKey.Paste):
            clipboard = QApplication.clipboard()
            mime_data = clipboard.mimeData()

            if mime_data.hasText():
                text = mime_data.text()
                lines = text.strip().split('\n')
                pasted_data = [line.strip() for line in lines if line.strip()]

                if pasted_data:
                    self.setRowCount(0)
                    self.setRowCount(len(pasted_data))

                    for row, value in enumerate(pasted_data):
                        cell_value = value.split('\t')[0]
                        item = QTableWidgetItem(cell_value)
                        self.setItem(row, 0, item)

                    event.accept()
                    return

        # For any other key press, call the default handler
        super().keyPressEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GeoexPage(GeoexScraper())
    window.show()
    sys.exit(app.exec())
