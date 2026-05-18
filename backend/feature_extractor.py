import re
def extract_features(url):

    features = []

    # URL Length
    features.append(len(url))

    # Dot Count
    features.append(url.count('.'))

    # Hyphen Count
    features.append(url.count('-'))

    # @ Count
    features.append(url.count('@'))

    # Digit Count
    features.append(sum(c.isdigit() for c in url))

    # HTTPS
    features.append(1 if "https" in url else 0)

    # IP Address
    ip_pattern = r'(\d{1,3}\.){3}\d{1,3}'
    features.append(1 if re.search(ip_pattern, url) else 0)

    # Suspicious Words
    suspicious_words = [
        'login',
        'verify',
        'secure',
        'bank',
        'update',
        'free',
        'bonus'
    ]

    suspicious_count = sum(
        word in url.lower()
        for word in suspicious_words
    )

    features.append(suspicious_count)

    return features