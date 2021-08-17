import requests

dns_cache = {}

def add_to_cache(domain, data):
    dns_cache[domain] = data

def resolve(domain):
    if domain in dns_cache:
        return dns_cache[domain]

    query = {
        'name': domain,
        'type': 'A',
        'ct': 'application/dns-json'
    }

    res = requests.get('https://cloudflare-dns.com/dns-query', params=query)

    if res.status_code == 200:
        answers = res.json()['Answer']
        last_data = domain
        for answer in answers:
            if answer['name'] == last_data:
                last_data = answer['data']
                if last_data[-1] == '.':
                    last_data = last_data[:-1]

        add_to_cache(domain, last_data)
        return last_data
    else:
        return domain