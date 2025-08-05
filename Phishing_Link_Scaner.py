import tldextract
import Levenshtein as levenshtein
from urllib.parse import urlparse

# Safe domains you trust
trusted_sites = [
    'paypal.com',
    'google.com',
    'facebook.com',
    'amazon.com',
    'etc.com'
]

url_list = [
    'http://payp@l.com',
    'https://google.com',
    'http://faceb00k.com',
    'http://amazon.con',
    'http://etc.co',
]

def break_down_url(link):
    parsed_data = urlparse(link)
    host = parsed_data.hostname or ''
    extracted = tldextract.extract(host)
    main = extracted.domain
    sub = extracted.subdomain
    tld = extracted.suffix
    protocol = parsed_data.scheme
    return main, sub, tld, protocol

def check_domain_legitimacy(main, tld, trusted, match_limit=0.98):
    if tld:
        constructed_domain = f"{main}.{tld}"
    else:
        constructed_domain = main

    for valid in trusted:
        similarity_score = levenshtein.ratio(constructed_domain, valid)
        if similarity_score == 1.0:
            return "legit"
        elif similarity_score >= match_limit:
            return "lookalike"
    return "suspicious"

def analyze_link(link, trusted):
    main, sub, tld, protocol = break_down_url(link)
    full_host = f"{main}.{tld}" if tld else main

    print(f"\n🔎 Analyzing: {link}")
    print(f"🔗 Protocol: {protocol.upper()} | Main: {main} | TLD: {tld} | Sub: {sub}")

    if protocol.lower() == "http":
        print("🚨 Caution: Using HTTP — data is not encrypted!")

    result = check_domain_legitimacy(main, tld, trusted)

    if result == "legit":
        print("✅ Safe: Domain matches trusted list.")
    elif result == "lookalike":
        print("⚠️ Alert: Domain closely resembles a trusted one — possible phishing.")
    else:
        print("❌ Danger: Unknown or deceptive domain detected!")

if __name__ == '__main__':
    # url_list = input_urls()
    for link in url_list:
        analyze_link(link, trusted_sites)
