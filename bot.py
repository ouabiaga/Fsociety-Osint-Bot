import discord
import api
import username_check
import json
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
token= json.load(open("api_key.json"))[0]["Bot Token"]
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!username'):
        username = message.content.split(' ')[1]
        finded_platforms = await username_check.check_username(username)
        if finded_platforms:
            response = f"Username '{username}' found on the following platforms:\n" + "\n".join(finded_platforms)
        else:
            response = f"Username '{username}' not found on any platform."
        await message.channel.send(response)
    if message.content.startswith('!domain'):
        domain = message.content.split(' ')[1]
        data = await api.domainOsint(domain)
        await message.channel.send(f"Domain OSINT for '{domain}':\n{data}")
    if message.content.startswith('!gmail'):
        email = message.content.split(' ')[1]
        data = await api.GmailOsint(email)
        await message.channel.send(f"Gmail OSINT for '{email}':\n{data}")
    if message.content.startswith('!whatsapp'):
        phone_number = message.content.split(' ')[1]
        data = await api.WatsappOsint(phone_number)
        await message.channel.send(f"WhatsApp OSINT for '{phone_number}':\n{data}")
    if message.content.startswith('!whois'):
        domain = message.content.split(' ')[1]
        data = await api.Whois(domain)
        await message.channel.send(f"Whois information for '{domain}':\n{data}")
    if message.content.startswith('!subdomain'):
        domain = message.content.split(' ')[1]
        data = await api.subdomainOsint(domain)
        await message.channel.send(f"Subdomain OSINT for '{domain}':\n{data}")
    if message.content.startswith('!ip'):
        ip_address = message.content.split(' ')[1]
        data = await api.ipOsint(ip_address)
        await message.channel.send(f"IP OSINT for '{ip_address}':\n{data}")
    if message.content.startswith('!dns'):
        domain = message.content.split(' ')[1]
        data = await api.dnsOsint(domain)
        await message.channel.send(f"DNS OSINT for '{domain}':\n{data}")
    if message.content.startswith('!help'):
        help_message = (
            "Available commands:\n"
            "!username <username> - Check username availability across multiple platforms.\n"
            "!domain <domain> - Get OSINT information for a domain.\n"
            "!gmail <email> - Get OSINT information for a Gmail address.\n"
            "!whatsapp <phone_number> - Get OSINT information for a WhatsApp number.\n"
            "!whois <domain> - Get Whois information for a domain.\n"
            "!subdomain <domain> - Get subdomain OSINT information for a domain.\n"
            "!ip <ip_address> - Get OSINT information for an IP address.\n" 
            "!dns <domain> - Get DNS OSINT information for a domain.\n"
            "!help - Display this help message."
        )
        await message.channel.send(help_message)
client.run(token)
