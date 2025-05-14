"""
    Privacy policies pop-up window
"""
from PySide6.QtWidgets import (
    QDialog, QLabel, QVBoxLayout, QPushButton, QHBoxLayout,
    QApplication, QScrollArea, QWidget
)
from PySide6.QtCore import Qt
from src.modules.gui.style_sheet import StyleSheets
from src.modules.load_configs.load_env_configs import load_env_configs

class PrivacyPolicies:
    """
    Privacy policies class with necessary functions
    """
    def __init__(self):
        """
        Initialize PrivacyPolicies class
        """
        env_configs = load_env_configs()
        self.app_name = env_configs["APP_NAME"]

    def show_message(self) -> bool:
        """
        Build Privacy policies window and show it

        Returns:
            bool: True if user accepted, False otherwise
        """

        dialog = QDialog()
        dialog.setWindowTitle("Políticas de Privacidade")
        dialog.setFixedSize(640, 480)
        dialog.setStyleSheet(StyleSheets.privacy_policies_popup)

        layout = QVBoxLayout(dialog)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        content_widget = QWidget()
        scroll_layout = QVBoxLayout(content_widget)

        informative_text = f"""
        <h1 style="text-align:center; font-weight:bold; font-size:16px;">Bem-vindo!</h1>
        <div style="text-align: left;">
          <p style="line-height: 1.4;">O app <b>"{self.app_name}"</b> opera exclusivamente com arquivos e diretórios contidos na mesma pasta do executável ou do código-fonte.</p>
          <p style="line-height: 1.4;">Isso significa que:
            <br><b>- Nenhum diretório externo será acessado sem que esteja explicitamente dentro da pasta do app;</b>
            <br><b>- Nenhum arquivo será criado ou lido fora do escopo dessa pasta;</b>
            <br><b>- Todas as interações com arquivos ocorrem localmente, e sob total controle do usuário.</b>
          </p>
          <p style="line-height: 1.4;">
            Os dados utilizados por este app são obtidos diretamente do sistema Geoex. Como essa plataforma pode ser alterada a qualquer momento por seus desenvolvedores, é possível que informações sejam interpretadas de maneira incorreta ou imprevista em futuras versões.
            <br><br>
            Assim, qualquer decisão tomada com base nos dados apresentados deve ser cuidadosamente revisada e validada pelo próprio usuário, que é o único responsável pela análise e uso das informações coletadas.
          </p>
          <strong>Aviso de Isenção de Responsabilidade:</strong>
          <p style="line-height: 1.4;">
            Eu, Max Gambarini Filho, não me responsabilizo por eventuais problemas decorrentes do uso deste aplicativo, incluindo, mas não se limitando a:
            <br>- Acesso indevido a arquivos;
            <br>- Integridade dos dados utilizados;
            <br>- Decisões baseadas nas informações coletadas via API do Geoex;
            <br>- Bloqueio do acesso ao Geoex devido uso excessivo da API;
          </p>
          <details>
            <p style="line-height: 1.4;">Ao concordar com esta declaração, você poderá prosseguir e utilizar o app normalmente.</p>
          </details>
        </div>
        <h4 style="font-weight:bold; text-align:left;">Concorda com os termos? </h4>
        """

        label = QLabel()
        label.setTextFormat(Qt.TextFormat.RichText)
        label.setText(informative_text)
        label.setWordWrap(True)

        scroll_layout.addWidget(label)
        scroll_area.setWidget(content_widget)

        button_layout = QHBoxLayout()
        agree_button = QPushButton("  Concordo  ")
        agree_button.setCursor(Qt.PointingHandCursor)
        agree_button.setStyleSheet(StyleSheets.ppp_accept_btn)

        disagree_button = QPushButton(" Não concordo ")
        disagree_button.setCursor(Qt.PointingHandCursor)
        disagree_button.setStyleSheet(StyleSheets.ppp_denied_btn)

        button_layout.addWidget(disagree_button)
        button_layout.addWidget(agree_button)

        layout.addWidget(scroll_area)
        layout.addLayout(button_layout)

        agree_button.clicked.connect(lambda: dialog.done(1))
        disagree_button.clicked.connect(lambda: dialog.done(0))

        result = dialog.exec()
        return result == 1


if __name__ == "__main__":
    QApplication([])
    privacy_policies = PrivacyPolicies()
    user_agreement = privacy_policies.show_message()
    if user_agreement:
        print("User agreed to the privacy policies.")
    else:
        print("User did not agree to the privacy policies.")
