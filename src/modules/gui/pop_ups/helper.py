"""
    Help Pop-Up module
"""
from PySide6.QtWidgets import (
    QPushButton, QApplication, QDialog,
    QVBoxLayout, QScrollArea, QWidget,
    QLabel, QHBoxLayout)
from PySide6.QtCore import Qt
from src.modules.gui.style_sheet import StyleSheets
from src.modules.load_configs.load_env_configs import load_env_configs

class HelpPopUp:
    """
        Help Pop-Up class with necessary functions
        
    """

    def show_message(self, app_name : str) -> None:
        """
            Build Help Pop-Up window and show it
            
            Returns:
                QMessageBox.AcceptRole (bool): User choice
        """

        dialog = QDialog()
        dialog.setWindowTitle("Help")
        dialog.setFixedSize(640, 480)
        dialog.setStyleSheet(StyleSheets.privacy_policies_popup)

        layout = QVBoxLayout(dialog)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        content_widget = QWidget()
        scroll_layout = QVBoxLayout(content_widget)

        informative_text = f"""
<h1 style="display:block; margin-inline:auto; text-align:center; font-weight:bold; font-size:16px;">Requisitos do Sistema</h1>
<div style="text-align: left;">
    <p style="line-height: 1.4;">Para o funcionamento adequado do aplicativo <b>"{app_name}"</b>, são necessárias as seguintes configurações:</p>
    
    <h3 style="font-weight:bold; margin-top:10px;">Credenciais do Geoex:</h3>
    <p style="line-height: 1.4;">
        <b>- Cookies de autenticação válidos</b><br>
        <b>- GxSessão</b><br>
        <b>- GxBot</b><br>
        <b>- Permissões:</b> O usuário deve ter permissão para acessar as rotas do Geoex<br>
    </p>

    <h3 style="font-weight:bold; margin-top:10px;">Configuração do Google Sheets:</h3>
    <p style="line-height: 1.4;">
        <b>- Id da planilha onde os dados serão inseridos</b><br>
        <b>- Invervalo onde os dados serão inseridos</b><br>
        <b>- Usuário deve ter acesso de editor no invervalo e na planilha fornecidos</b><br>
    </p>

    <h3 style="font-weight:bold; margin-top:10px;">Requisitos Adicionais:</h3>
    <p style="line-height: 1.4;">
        <b>- Credenciais de acesso do google sheets</b><br>
        <b>- Conexão com a internet</b><br>
    </p>
</div>
"""

        label = QLabel()
        label.setTextFormat(Qt.TextFormat.RichText)
        label.setText(informative_text)
        label.setWordWrap(True)

        scroll_layout.addWidget(label)
        scroll_area.setWidget(content_widget)

        button_layout = QHBoxLayout()
        agree_button = QPushButton("  OK  ")
        agree_button.setCursor(Qt.PointingHandCursor)
        agree_button.setStyleSheet(StyleSheets.ppp_accept_btn)
        button_layout.addWidget(agree_button)

        layout.addWidget(scroll_area)
        layout.addLayout(button_layout)

        agree_button.clicked.connect(dialog.close)
        dialog.exec()

if __name__ == "__main__":
    env_configs = load_env_configs()
    name = env_configs.get("APP_NAME", "Geoex Bot")
    QApplication([])
    HelpPopUp().show_message(name)
