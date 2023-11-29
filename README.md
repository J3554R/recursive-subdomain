# Recursive Subdomain Bruteforcer via Ffuf

## Description
This tool recursivly enumerates for subdomains using ffuf. The tool uses regex to only retrieve the domains.
Make sure to have <a href="https://github.com/ffuf/ffuf">ffuf</a> installed.

## Install

```
git clone https://github.com/J3554R/recursive-subdomain.git
```

# Usage

```
# ./recursive.py -d target.com -w wordlist.txt
```
You can also add custom ffuf options with the "-ff" flag:
```
# ./recursive.py -d target.com -w wordlist.txt -ff "-mc 200 -fw 21"
```

## Tip

Set the "default_wordlist" variable in the script to point to your desired default wordlist so you can run the tool with one argument:
```
# ./recursive.py target.com
```
