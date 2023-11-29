#!/usr/bin/python3

import sys, subprocess, argparse

# Checking for arguments
argv = False
if len(sys.argv) == 2:
    domain = sys.argv[1]
    if "-h" in domain:
        argv = False
    elif "." not in domain:
        sys.exit("Not a valid argument. Type '-h' to print out the help menu.")
    else:
        argv = True

def discover_subdomains(subdomain, discovered_subdomains):
    # ffuf commands
    if argv == True:
        ffuf_command = f"ffuf -u https://FUZZ.{subdomain} -w {default_wordlist}"
    else:
        ffuf_command = f"ffuf -u https://FUZZ.{subdomain} -w {wordlist} {ffuf_options}"

    try:
        ffuf_output = subprocess.check_output(ffuf_command, stderr=subprocess.DEVNULL, shell=True).decode().split('\n')
    except subprocess.CalledProcessError as e:
        sys.exit(f"{str(e)} Does the wordlist exist?")

    new_subdomains = []

    for l in ffuf_output:
        # Regex for retrieving only the domains for the output
        if "FUZZ" in l:
            sub = l.split("FUZZ: ")[1]
            full_subdomain = f"{sub}.{subdomain}"
            if full_subdomain not in discovered_subdomains:
                discovered_subdomains.add(full_subdomain)
                new_subdomains.append(full_subdomain)
    # Loop for recursive enumeration
    for sub in new_subdomains:
        print(sub)
        discover_subdomains(sub, discovered_subdomains)

default_wordlist = "wordlist.txt" # << Change this with the path of your desired default wordlist

# Runs if you provided argparse arguments
if not argv:
    parser = argparse.ArgumentParser(description='Recursive subdomain bruteforcing using FFUF.')
    parser.add_argument('-d', '--domains', nargs='+', help='Your domain(s).', required=True)
    parser.add_argument('-w', '--wordlist', default=default_wordlist, help='Your wordlist. Default wordlist used if no wordlist is provided.')
    parser.add_argument('-ff', help='FFUF flags as a single string. Example: -ff "-mc 200 -fc 302 -fw 80"')
    args = parser.parse_args()

    ffuf_options = args.ff or ""
    domains = args.domains
    wordlist = args.wordlist

    for domain in domains:
        initial_subdomain = domain
        discovered_subdomains = {initial_subdomain}
        discover_subdomains(initial_subdomain, discovered_subdomains)

# Runs if you only provided one argument and already have the default wordlist set
else:
    initial_subdomain = domain
    discovered_subdomains = {initial_subdomain}
    discover_subdomains(initial_subdomain, discovered_subdomains)

# Tested with ffuf version v2.0.0-dev
# Quick usage if the default wordlist is set: ./tool.py target.com
# Basic usage: ./tool.py -d target.com -w wordlist.txt -ff '-mc 200'
