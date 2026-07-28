from bs4 import BeautifulSoup
import requests
import re
from typing import Dict, TYPE_CHECKING
from pshtt.pshtt import inspect_domains
import tldextract
from django.utils import timezone
from directory.models import ScanResult, DirectoryEntry
from scanner.utils import url_to_domain
if TYPE_CHECKING:
from directory.models import DirectoryEntryQuerySet
def pshtt_data_to_result(securedrop: DirectoryEntry, pshtt_results: Dict...
"""docstring"""
page, soup = request_and_scrape_page(securedrop.landing_page_url)
return ScanResult(securedrop=securedrop, live=pshtt_results['Live'],
    http_status_200_ok=False)
return ScanResult(landing_page_url=securedrop.landing_page_url, live=
    pshtt_results['Live'], http_status_200_ok=validate_200_ok(
    no_redirects_page), forces_https=bool(pshtt_results[
    'Strictly Forces HTTPS']), hsts=pshtt_results['HSTS'], hsts_max_age=
    validate_hsts_max_age(pshtt_results['HSTS Max Age']),
    hsts_entire_domain=validate_hsts_entire_domain(pshtt_results[
    'HSTS Entire Domain']), hsts_preloaded=pshtt_results['HSTS Preloaded'],
    subdomain=validate_subdomain(securedrop.landing_page_url), no_cookies=
    validate_no_cookies(page), safe_onion_address=
    validate_onion_address_not_in_href(soup), no_cdn=validate_not_using_cdn
    (page), http_no_redirect=validate_no_redirects(no_redirects_page),
    expected_encoding=validate_encoding(page), no_analytics=
    validate_not_using_analytics(page), no_server_info=
    validate_server_software(page), no_server_version=
    validate_server_version(page), csp_origin_only=validate_csp(page),
    mime_sniffing_blocked=validate_no_sniff(page), noopen_download=
    validate_download_options(page), xss_protection=validate_xss_protection
    (page), clickjacking_protection=validate_clickjacking_protection(page),
    good_cross_domain_policy=validate_cross_domain_policy(page),
    http_1_0_caching_disabled=validate_pragma(page), expires_set=
    validate_expires(page), cache_control_set=validate_cache_control_set(
    page), cache_control_revalidate_set=validate_cache_must_revalidate(page
    ), cache_control_nocache_set=validate_nocache(page),
    cache_control_notransform_set=validate_notransform(page),
    cache_control_nostore_set=validate_nostore(page),
    cache_control_private_set=validate_private(page),
    referrer_policy_set_to_no_referrer=validate_no_referrer_policy(page))
no_redirects_page, _ = request_and_scrape_page(securedrop.landing_page_url,
    allow_redirects=False)
