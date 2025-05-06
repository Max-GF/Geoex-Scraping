"""
    Main entry point for the application.
"""
import pandas as pd

from src.modules.consult_builders.folders_status_consult import consult_folder_status_in_geoex
from src.modules.consult_builders.project_consult import consult_project_in_geoex
from src.modules.load_configs.load_env_configs import load_env_credentials
from src.modules.load_configs.load_project_list import load_project_list
from src.modules.utils.fix_geoex_returned_dates import fix_geoex_returned_date
from src.modules.utils.safe_get_for_body import safe_get
from src.modules.google_sheets.sheets_python import SheetsPython

class GeoexScraper:
    """
    Initialize the GeoexScraper class.
    This class is responsible for scraping data from Geoex.
    """
    def __init__(self):
        self.geoex_credentials = load_env_credentials()
        self.projects_to_consult = load_project_list()
        self.folder_status_reversed_enum = {
            118: "PASTA ACEITA E FINALIZADA",
            30: "ACEITO",
            22: "PENDENTE",
            32: "REJEITADO",
            35: "VALIDADO",
            31: "ACEITO COM RESTRIÇÕES",
            99: "ERRO DE SUBGRUPO",
            1: "CRIADO",
            }
    def scrape_projects_infos(
        self,
        google_sheet_id: str,
        google_sheet_range: str,
        ):
        """
        Scrape project information from Geoex.
        This method iterates through the list of projects to consult
        and retrieves their information using the Geoex API.
        """
        scraped_data = []
        for project in self.projects_to_consult:
            print(f"Project: {project}")
            result = consult_project_in_geoex(
                project_numbers=project,
                cookies=self.geoex_credentials["cookies"],
                gxsessao=self.geoex_credentials["gxsessao"],
                gxbot=self.geoex_credentials["gxbot"]
            )

            if result['response_status'] == 200:
                folder_status_result = consult_folder_status_in_geoex(
                    safe_get(result, ['response_body', 'ProjetoId']),
                    cookies=self.geoex_credentials["cookies"],
                    gxsessao=self.geoex_credentials["gxsessao"],
                    gxbot=self.geoex_credentials["gxbot"]
                )

                correct_send = next(
                    (element for element in folder_status_result['response_body']["Envios"] if element["Empresa"] == "ECOELÉTRICA"),
                    None)
                folder_status1 = self.folder_status_reversed_enum.get(safe_get(folder_status_result, ['response_body','HistoricoStatusId']))
                folder_status2 = self.folder_status_reversed_enum.get(safe_get(correct_send, ['HistoricoStatus'],99))
                folder_date = safe_get(correct_send, ['Ultimo', 'DataValidacao'])
                folder_down_date = safe_get(correct_send, ['Ultimo', 'DataBaixa'])
                folder_n_attempts = len(safe_get(correct_send, ['EnvioPastas'],[]))

                scraped_data.append([
                                safe_get(result, ['response_body', 'ProjetoText']),
                                safe_get(result, ['response_body', 'Titulo']),
                                safe_get(result, ['response_body', 'Nota', 'Numero']),
                                safe_get(result, ['response_body', 'Empresa']),
                                safe_get(result, ['response_body', 'Municipio']),
                                safe_get(result, ['response_body', 'Localidade']),
                                safe_get(result, ['response_body', 'StatusProjeto', 'Descricao']),
                                fix_geoex_returned_date(safe_get(result, ['response_body', 'StatusProjetoData'])),
                                fix_geoex_returned_date(safe_get(result, ['response_body', 'DtZps09'])),
                                safe_get(result, ['response_body', 'Termo', 'Serial']),
                                safe_get(result, ['response_body', 'Termo', 'Status']),
                                fix_geoex_returned_date(safe_get(result, ['response_body', 'Termo', 'StatusData'])),
                                safe_get(result, ['response_body', 'GseProjeto', 'Status', 'Nome']),
                                fix_geoex_returned_date(safe_get(result, ['response_body', 'GseProjeto', 'StatusData'])),
                                safe_get(result, ['response_body', 'VlProjeto']),
                                safe_get(result, ['response_body', 'PosicaoInvestimento']),
                                f'{folder_status1} - {folder_status2}',
                                safe_get(result, ['response_body', 'CarteirasObras', 0, 'Criterio']),
                                safe_get(result, ['response_body', 'ArquivoTipologia', 'Nome']),
                                safe_get(result, ['response_body', 'ResponsavelCarteiraProgramacaoUsuario', 'Nome']),
                                safe_get(result, ['response_body', 'ProjetoMedidor']),
                                safe_get(result, ['response_body', 'ProjetoKit']),
                                fix_geoex_returned_date(folder_date),
                                safe_get(result, ['response_body', 'Etiquetas', 0, 'Nome']),
                                fix_geoex_returned_date(folder_down_date),
                                folder_n_attempts
                            ])
        print(pd.DataFrame(scraped_data))
        SheetsPython().update_sheets_data(
            data_frame=pd.DataFrame(scraped_data),
            id_sheets=google_sheet_id,
            range_sheets=google_sheet_range,
            append=True,
            append_col_ref="A",
        )

if __name__ == "__main__":
    GeoexScraper().scrape_projects_infos(
        "1JFyGqnTuxnPSN7grmf8SHpHS2NnxSClj2p1Uxa-KRJE",
        "Base!A:Z"
    )
