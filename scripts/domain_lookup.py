import socket
import argparse

def domain_lookup(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"Domain: {domain}")
        print(f"IP Address: {ip_address}")
    except socket.gaierror:
        print(f"Unable to get IP for domain: {domain}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Domain Lookup Tool")
    parser.add_argument("--domain", help="Target domain for lookup", required=True)
    args = parser.parse_args()
    
    domain_lookup(args.domain)
