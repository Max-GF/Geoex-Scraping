"""
    Module to consult project information in Geoex
    using the provided project numbers and session information.
"""
import cloudscraper

def consult_project_in_geoex(
    project_numbers : str,
    cookies : str,
    gxsessao : str,
    gxbot : str
    ) -> dict:
    """
    Consult a project in Geoex using the
    provided project numbers and session information.
    This function uses the cloudscraper library to
    bypass Cloudflare's anti-bot protection.

    Args:
        project_numbers (str): Project numbers to be consulted.
        cookies (str): Cookies for the request.
        gxsessao (str): GXSession ID for the request.
        gxbot (str): GXBot ID for the request.

    Returns:
        dict: A object containing the response status and body.
    """
    scraper = cloudscraper.create_scraper()

    response = scraper.post(
        'https://geoex.com.br/api/Programacao/ConsultarProjeto/Item',
        json={"id": project_numbers},
        headers={
            "cookie": cookies,
            "gxsessao": gxsessao,
            "gxbot": gxbot,
            # "Content-Type": "application/json;charset=UTF-8",
            # "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        }
    )
    response_data = response.json()

    return {
        "response_status": response.status_code,
        "response_body": response_data.get("Content")
    }
