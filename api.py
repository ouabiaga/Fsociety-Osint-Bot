import asyncio
import aiohttp
import json

api_key=json.load(open("api_key.json"))[0]["rapidapi-key"]
async def domainOsint(domain):
    async with aiohttp.ClientSession() as session:
        url = "https://domain-osint.p.rapidapi.com/api/domain"
        
        payload = { "domain": domain }
        headers = {
                "x-rapidapi-key": api_key,
                "x-rapidapi-host": "domain-osint.p.rapidapi.com",
                "Content-Type": "application/json"
            }
        async with session.post(url, json=payload, headers=headers) as response:
            data = await response.json()
            return data
    
async def GmailOsint(email):
    async with aiohttp.ClientSession() as session:
        url = "https://gmail-osint.p.rapidapi.com/gmail"
        
        payload = { "email": email }
        headers = {
                "x-rapidapi-key": api_key,
                "x-rapidapi-host": "gmail-osint.p.rapidapi.com",
                "Content-Type": "application/json"
            }
        async with session.post(url, json=payload, headers=headers) as response:
            data = await response.json()
            return data
async def WatsappOsint(phone_number):
    async with aiohttp.ClientSession() as session:
            url = "https://whatsapp-osint.p.rapidapi.com/bizos"
            
            payload = { "phone": phone_number }
            headers = {
                    "x-rapidapi-key": api_key,
                    "x-rapidapi-host": "whatsapp-osint.p.rapidapi.com",
                    "Content-Type": "application/json"
                }
            async with session.post(url, json=payload, headers=headers) as response:
                data = await response.json()
                return data
async def Whois(domain):
    async with aiohttp.ClientSession() as session:
            url = "https://whois-lookup10.p.rapidapi.com/whoishosting.php"
            
            payload = {"domain": domain}
            headers = {
                    "x-rapidapi-key": api_key,
                    "x-rapidapi-host": "whois-lookup10.p.rapidapi.com",
                }
            async with session.post(url, json=payload, headers=headers) as response:
                data = await response.json()
                return data
async def subdomainOsint(domain):
    async with aiohttp.ClientSession() as session:
        url = "https://subdomain-finder3.p.rapidapi.com/v1/subdomain-finder/"
            
        payload = {"domain":domain}
        headers = {
                    "x-rapidapi-key": api_key,
                    "x-rapidapi-host": "subdomain-finder3.p.rapidapi.com",
                }
        async with session.post(url, json=payload, headers=headers) as response:
            data = await response.json()
            return data
async def IpOsint(ip_address):
       async with aiohttp.ClientSession() as session:
        async with session.get(f'http://ip-api.com/json/{ip_address}') as response:
            data = await response.json()
            return data
async def dnsOsint(dns):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://edns.ip-api.com/json/{dns}') as response:
            data = await response.json()
            return data
async def GithubOsint(username):
    async with aiohttp.ClientSession() as session:
        url = f"https://api.github.com/users/{username}"
        async with session.get(url) as response:
            data = await response.json()
            return data
