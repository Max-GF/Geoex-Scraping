"""
    Main entry point for the application.
"""
from src.modules.consult_builders.project_consult import consult_project_in_geoex
from src.modules.load_configs.load_env_configs import load_env_credentials
from src.modules.load_configs.load_project_list import load_project_list
from src.modules.utils.safe_get_for_body import safe_get


class GeoexScraper:
    def __init__(self):
        """
        Initialize the GeoexScraper class.
        This class is responsible for scraping data from Geoex.
        """
        self.geoex_credentials = load_env_credentials()
        self.projects_to_consult = load_project_list()
    
    def scrape_projects_infos(self):
        """
        Scrape project information from Geoex.
        This method iterates through the list of projects to consult
        and retrieves their information using the Geoex API.
        """
        for project in self.projects_to_consult:
            print(f"Project: {project}")
            result = consult_project_in_geoex(
                project_numbers=project,
                cookies=self.geoex_credentials["cookies"],
                gxsessao=self.geoex_credentials["gxsessao"],
                gxbot=self.geoex_credentials["gxbot"]
            )
            if result['response_status'] == 200:
                print(result.get('response_body', {}))
                print([
                        safe_get(result, ['response_body', 'ProjetoText']),
                        safe_get(result, ['response_body', 'Titulo']),
                        safe_get(result, ['response_body', 'Nota', 'Numero']),
                        safe_get(result, ['response_body', 'Empresa']),
                        safe_get(result, ['response_body', 'Municipio']),
                        safe_get(result, ['response_body', 'Localidade']),
                        safe_get(result, ['response_body', 'StatusProjeto', 'Descricao']),
                        safe_get(result, ['response_body', 'StatusProjetoData']),
                        safe_get(result, ['response_body', 'DtZps09']),
                        safe_get(result, ['response_body', 'Termo', 'Serial']),
                        safe_get(result, ['response_body', 'Termo', 'Status']),
                        safe_get(result, ['response_body', 'Termo', 'StatusData']),
                        safe_get(result, ['response_body', 'GseProjeto', 'Status', 'Nome']),
                        safe_get(result, ['response_body', 'GseProjeto', 'StatusData']),
                        safe_get(result, ['response_body', 'VlProjeto']),
                        safe_get(result, ['response_body', 'PosicaoInvestimento']),
                        safe_get(result, ['response_body', 'CarteirasObras', 0, 'Criterio']),
                        safe_get(result, ['response_body', 'ArquivoTipologia', 'Nome']),
                        safe_get(result, ['response_body', 'ResponsavelCarteiraProgramacaoUsuario', 'Nome']),
                        safe_get(result, ['response_body', 'ProjetoMedidor']),
                        safe_get(result, ['response_body', 'ProjetoKit']),
                        safe_get(result, ['response_body', 'Etiquetas', 0, 'Nome']),
                    ])

if __name__ == "__main__":
    GeoexScraper().scrape_projects_infos()
