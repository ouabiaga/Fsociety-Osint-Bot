# Fsociety OSINT Bot

A Python-powered Discord bot for basic OSINT lookups using publicly available sources. It checks username matches across multiple platforms and performs domain, IP, DNS, WHOIS, email, and phone number lookups through third-party services.

> This project is intended for educational and portfolio purposes. Use it only with proper authorization and in compliance with applicable laws.

## Features

- Check a username across nearly 40 social and online platforms
- Query domain, Gmail, WhatsApp, WHOIS, and subdomain information through RapidAPI services
- Look up IP and DNS information using ip-api.com
- Run queries with Discord message commands

## Requirements

- Python 3
- A Discord bot token
- A RapidAPI key and access to the APIs you intend to use

Install the Python dependencies:

```bash
python -m pip install discord.py aiohttp colorama
```

## Setup

1. Clone the repository and enter the project directory:

   ```bash
   git clone https://github.com/<your-username>/fsociety-osint-bot.git
   cd fsociety-osint-bot
   ```

2. Create an `api_key.json` file in the project directory. The code reads the Discord bot token from `Bot Token` and the RapidAPI key from `rapidapi-key`:

   ```json
   [
     {
       "Bot Token": "YOUR_DISCORD_BOT_TOKEN",
       "rapidapi-key": "YOUR_RAPIDAPI_KEY"
     }
   ]
   ```

   **Never upload real tokens or API keys to GitHub.** Add `api_key.json` to `.gitignore`. If a real key has already been exposed publicly, revoke it with the provider and create a new one.

3. In the Discord Developer Portal, enable **Message Content Intent** for your bot and invite it to your server with the permissions needed to read and send messages.

4. Start the bot:

   ```bash
   python bot.py
   ```

## Commands

| Command | Description | Example |
|---|---|---|
| `!username <username>` | Check a username across supported platforms. | `!username octocat` |
| `!domain <domain>` | Run an OSINT lookup for a domain. | `!domain example.com` |
| `!gmail <email>` | Run an OSINT lookup for a Gmail address. | `!gmail user@gmail.com` |
| `!whatsapp <phone_number>` | Run a WhatsApp lookup for a phone number. | `!whatsapp +15551112233` |
| `!whois <domain>` | Look up WHOIS/hosting information. | `!whois example.com` |
| `!subdomain <domain>` | Look up subdomains for a domain. | `!subdomain example.com` |
| `!ip <ip_address>` | Look up information about an IP address. | `!ip 8.8.8.8` |
| `!dns <domain>` | Look up DNS information. | `!dns example.com` |
| `!help` | Show the available commands. | `!help` |

## Limitations and Privacy

- Username checks rely on HTTP response codes from platform pages; they cannot conclusively confirm whether an account exists. Platform responses, access policies, and URL formats may change.
- OSINT results are provided by third-party services. Accuracy, availability, quotas, and access requirements depend on those providers.
- Usernames, domains, email addresses, and phone numbers may be sent to external services. Do not query sensitive personal data or data you are not authorized to use.
- Keep API keys private. Before using the bot in public servers, consider restricting command access and review the applicable service terms.

## Built With

Python · discord.py · aiohttp · colorama · RapidAPI
