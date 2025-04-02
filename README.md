# Recursive Subdomain Bruteforcer via Ffuf

## Description
This tool recursively enumerates for subdomains using ffuf. The tool uses regex to only retrieve the domains.
Make sure to have <a href="https://github.com/ffuf/ffuf">ffuf</a> installed.

## Install

```
git clone https://github.com/J3554R/recursive-subdomain.git
```

# Usage

```
# ./recursive.py -d target.com -w wordlist.txt
```

You can also set ffuf options with the "-ff" flag:
```
# ./recursive.py -d target.com -w wordlist.txt -ff "-mc 200 -fw 21"
```

#### Note

Set the "default_wordlist" variable in the script to point to your desired wordlist so you can run the tool with one argument:
```
# ./recursive.py target.com
```

This tool may or may not work on your system. I ran it on my Ubuntu VPS, where it worked successfully, but it failed on my Kali VM.
