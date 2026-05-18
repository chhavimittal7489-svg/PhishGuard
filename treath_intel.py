import requests
import whois
from urllib.parse import urlparse


def check_urlhaus(url):

    try:

        response = requests.post(
            "https://urlhaus-api.abuse.ch/v1/url/",
            data={"url": url},
            headers={
                "User-Agent": "PhishGuard"
            },
            timeout=5
        )

        return response.json()

    except Exception as e:

        return {
            "error": str(e)
        }


def get_domain_info(url):

    try:

        domain = urlparse(url).netloc

        info = whois.whois(domain)

        return {

            "domain": domain,

            "registrar": str(info.registrar),

            "creation_date": str(info.creation_date),

            "expiration_date": str(info.expiration_date)

        }

    except Exception as e:

        return {
            "error": str(e)
        }