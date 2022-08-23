import os
import json
import socket
import sys
import random

try:
    import discord
    import asyncio
    import requests
    import discum
    from discord.ext import commands
    from colorama import init, Fore
except Exception as e:
    print(f"Error, a module is missing, info below:\n{e}")
    exit()

token = "Token goes here, obviously"
proxycheckkey = 'proxycheck.io API Key here (OPTIONAL)'
abuseipdbkey = 'AbuseIPDB API Key here (OPTIONAL)'
prefix = ">>"

sys.tracebacklimit = 0
init()
bot = commands.Bot(prefix, self_bot=True)
apiurl = 'https://discordapp.com/api/v6/users/@me'
headers = { 'Authorization': f'{token}', 'Content-Type': 'application/json' }
info = requests.get(apiurl, headers=headers).json()
username = f'{info["username"]}#{info["discriminator"]}'
userid = f'{info["id"]}'

def random_ua():
    userAgents = ["Mozilla/5.0 (Windows NT 6.2;en-US) AppleWebKit/537.32.36 (KHTML, live Gecko) Chrome/56.0.3075.83 Safari/537.32", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.1", "Mozilla/5.0 (Windows NT 8.0; WOW64) AppleWebKit/536.24 (KHTML, like Gecko) Chrome/32.0.2019.89 Safari/536.24", "Mozilla/5.0 (Windows NT 5.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.41 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3058.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3258.0 Safari/537.36", "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36", "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2599.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.35 (KHTML, like Gecko) Chrome/27.0.1453.0 Safari/537.35", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.139 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/6.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.0.9757 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.1", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3258.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/6.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.1", "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2151.2 Safari/537.36", "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1204.0 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/67.0.3387.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.0.9757 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3359.181 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3251.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/538 (KHTML, like Gecko) Chrome/36 Safari/538", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.18 Safari/535.1", "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.355.0 Safari/533.3", "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.4 Safari/532.0", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.35 (KHTML, like Gecko) Chrome/27.0.1453.0 Safari/537.35", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3359.181 Safari/537.36", "Mozilla/5.0 (Windows NT 10.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36", "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3057.0 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.14", "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36 TC2", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3058.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3258.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2531.0 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Safari/537.36", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36,gzip(gfe)", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2264.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.29 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.150 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.45 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.14", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2714.0 Safari/537.36", "24.0.1284.0.0 (Windows NT 5.1) AppleWebKit/534.0 (KHTML, like Gecko) Chrome/24.0.1284.0.3.742.3 Safari/534.3", "Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1864.6 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Chrome/36.0.1985.125 CrossBrowser/36.0.1985.138 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Avast/70.0.917.102", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1615.0 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.14", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/6.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3608.0 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3251.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/54.2.133 Chrome/48.2.2564.133 Safari/537.36", "24.0.1284.0.0 (Windows NT 5.1) AppleWebKit/534.0 (KHTML, like Gecko) Chrome/24.0.1284.0.3.742.3 Safari/534.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/54.2.133 Chrome/48.2.2564.133 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/54.2.133 Chrome/48.2.2564.133 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.18 Safari/535.1", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2427.7 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.61 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Chrome/36.0.1985.125 CrossBrowser/36.0.1985.138 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.45 Safari/537.36", "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/2.0.174.0 Safari/530.6", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.29 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.104 Safari/537.36", "24.0.1284.0.0 (Windows NT 5.1) AppleWebKit/534.0 (KHTML, like Gecko) Chrome/24.0.1284.0.3.742.3 Safari/534.3", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko; Google Web Preview) Chrome/27.0.1453 Safari/537.36,gzip(gfe)", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.29 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.45 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.45", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.150 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.102 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2419.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Chrome/36.0.1985.125 CrossBrowser/36.0.1985.138 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1204.0 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2700.0 Safari/537.36#", "Mozilla/5.0 (Windows NT 10.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36", "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.16 (KHTML, like Gecko) Chrome/5.0.335.0 Safari/533.16", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.68 Safari/537.36", "Mozilla/5.0 (Windows; U; Windows 95) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.43 Safari/535.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2700.0 Safari/537.36#", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.114 Safari/537.36", "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/2.0.174.0 Safari/530.6", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/538 (KHTML, like Gecko) Chrome/36 Safari/538", "Mozilla/5.0 (Windows; U; Windows 95) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.43 Safari/535.1", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.18 Safari/535.1", "Mozilla/5.0 (X11; Linux x86_64; 6.1) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/17.0.1410.63 Safari/537.31", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2583.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2151.2 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.18 Safari/535.1", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/536.36 (KHTML, like Gecko) Chrome/67.2.3.4 Safari/536.36", "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.0 Safari/530.5", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.69 Safari/537.36", "Mozilla/5.0 (Windows NT 10.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Safari/537.36 EdgA/41.0.0.1662", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.1"]
    userAgent = random.choice(userAgents)
    return userAgent

def title():
    print(f"""{Fore.BLUE}            
              $$\                                       
              $$ |                                      
   $$$$$$$\ $$$$$$\   $$\   $$\  $$$$$$\  $$$$$$\$$$$\  
  $$  _____|\_$$  _|  \$$\ $$  |$$  __$$\ $$  _$$  _$$\ 
  \$$$$$$\    $$ |     \$$$$  / $$ |  \__|$$ / $$ / $$ |
   \____$$\   $$ |$$\  $$  $$<  $$ |      $$ | $$ | $$ |
  $$$$$$$  |  \$$$$  |$$  /\$$\ $$ |      $$ | $$ | $$ |
  \_______/    \____/ \__/  \__|\__|      \__| \__| \__|{Fore.WHITE}

{Fore.BLUE}Logged in as {Fore.RED}>> {Fore.WHITE}{username}
{Fore.BLUE}User ID {Fore.RED}>> {Fore.WHITE}{userid}
{Fore.BLUE}Prefix {Fore.RED}>> {Fore.WHITE}{prefix}
⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
""")

@bot.event
async def on_ready():
    os.system('cls;clear')
    title()
    print(f"{Fore.YELLOW}stxrm {Fore.RED}>> {Fore.WHITE}Ready!")
    

@bot.command()
async def commands(ctx):
    if str(ctx.message.author) == username:
        await ctx.message.edit(content=f"stxrm >> Check your console!")
        print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Executing Help command")
        print(f"""
{Fore.YELLOW}stxrm Selfbot, {Fore.BLUE}developed by {Fore.RED}synth
{Fore.WHITE}Commands:

{Fore.YELLOW}clearconsole {Fore.RED}>> {Fore.WHITE}Clears the terminal/console
{Fore.YELLOW}consoletest {Fore.RED}>> {Fore.WHITE}Tests if the terminal/console is printing properly
{Fore.YELLOW}changehypesquad (bravery/brilliance/balance) {Fore.RED}>> {Fore.WHITE}Changes your Hypesquad house to Bravery, Brilliance or Balance
{Fore.YELLOW}avatar (@mention) {Fore.RED}>> {Fore.WHITE}Grabs mentioned users avatar
{Fore.YELLOW}identitygen {Fore.RED}>> {Fore.WHITE}Generates a fake identity via a random data API
{Fore.YELLOW}passwordgen (length) {Fore.RED}>> {Fore.WHITE}Generates a secure password with given length
{Fore.YELLOW}tokeninfo (token){Fore.RED}>> {Fore.WHITE}Gets information about provided token
{Fore.YELLOW}userinfo (@user){Fore.RED}>> {Fore.WHITE}Gets information about pinged user
{Fore.YELLOW}proxycheck (ip){Fore.RED}>> {Fore.WHITE}Checks provided IP to see if it is a proxy or VPN
{Fore.YELLOW}geoip (ip){Fore.RED}>> {Fore.WHITE}Grabs information about given IP
{Fore.YELLOW}ping (IP/Domain) {Fore.RED}>> {Fore.WHITE}Pings the provided domain/IP
{Fore.YELLOW}length (string){Fore.RED}>> {Fore.WHITE}Returns the length of a given string
{Fore.YELLOW}friendbackup {Fore.RED}>> {Fore.WHITE}Backs up a list of all your friends, including blocked users and outgoing friend requests
{Fore.YELLOW}serverbackup {Fore.RED}>> {Fore.WHITE}Backs up a list of all your servers, including their IDs
{Fore.YELLOW}ghostping (@user) {Fore.RED}>> {Fore.WHITE}Quickly deletes the previous message, essentially ghost pinging someone
{Fore.YELLOW}webhookinfo (webhook) {Fore.RED}>> {Fore.WHITE}Obtains info on a given webhook
{Fore.YELLOW}spamwebhook (amount) (webhook) (message){Fore.RED}>> {Fore.WHITE}Spams provided webhook a certain amount of times with given message
{Fore.YELLOW}createwebhook {Fore.RED}>> {Fore.WHITE}Creates a new webhook in the channel its executed in, prints the URL in console
{Fore.YELLOW}deletewebhook (webhook){Fore.RED}>> {Fore.WHITE}Self explanatory, deletes the provided webhook
{Fore.YELLOW}nukeserver {Fore.RED}>> {Fore.WHITE}Attempts to nuke the server (Requires Administrator permissions)
{Fore.YELLOW}spacechannel (Channel Name) {Fore.RED}>> {Fore.WHITE}Creates a channel with a space in it
{Fore.YELLOW}quit {Fore.RED}>> {Fore.WHITE}Self explanatory, quits stxrm
""")

@bot.command()
async def clearconsole(ctx):
    if str(ctx.message.author) == username:
        print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Clearing Console..")
        os.system('cls;clear')
        title()
        print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Cleared Console")
        await ctx.message.edit(content=f"stxrm >> Cleared Console")

@bot.command()
async def consoletest(ctx):
    if str(ctx.message.author) == username:
         print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Console is working")

@bot.command()
async def changehypesquad(ctx, house):
    if str(ctx.message.author) == username:
        houses = ["bravery", "brilliance", "balance"]
        if house in houses:
            DiscumClient = discum.Client(token=token, user_agent=random_ua(), log=False)
            DiscumClient.setHypesquad(house)
            await ctx.message.edit(content=f"stxrm >> Hypesquad house changed to {house[:1].upper() + house[1:].lower()} successfully")
            print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Changed Hypesquad house to {house[:1].upper() + house[1:].lower()} successfully")
        else:
            await ctx.message.edit(content="stxrm >> Invalid Hypesquad house.. Available houses: `bravery`, `brilliance`, `balance`")
            print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Invalid Hypesquad house.. Available houses: bravery, brilliance, balance")

@bot.command()
async def quit(ctx):
    if str(ctx.message.author) == username:
        print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Quitting stxrm.. Goodbye.")
        await ctx.message.edit(content="stxrm >> Quitting stxrm.. Goodbye.")
        exit()

@bot.command()
async def avatar(ctx, member: discord.User = None):
    if str(ctx.message.author) == username:
        if not member:
            member = ctx.message.author
        userAvatar = member.avatar_url
        await ctx.message.edit(content=f"`{member}` Avatar: {userAvatar}")
        print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Grabbed avatar from {member}")

@bot.command()
async def servericon(ctx):
    if str(ctx.message.author) == username:
        guildicon = ctx.guild.icon_url
        print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Grabbed server icon from {ctx.guild.name}")
        await ctx.message.edit(content=f"stxrm >> Server Icon: {guildicon}")

@bot.command()
async def serverinfo(ctx):
    if str(ctx.message.author) == username:
        print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Grabbed information from '{ctx.guild.name}'")
        await ctx.message.edit(content=f"stxrm >> Server information:\n```Server Name: {ctx.guild.name}\nOwner: {ctx.guild.owner}\nCreated on: {ctx.guild.created_at}\nMember Count: {ctx.guild.member_count}\nChannel Count: {len(ctx.guild.text_channels)}\nRegion: {ctx.guild.region}\nServer ID: {ctx.guild.id}\nServer Icon: {ctx.guild.icon_url}```")

@bot.command()
async def identitygen(ctx):
    if str(ctx.message.author) == username:
        await ctx.message.edit(content=f"stxrm >> Generating Fake Identity...")
        print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Generating Fake Identity...")
        r = requests.get('https://random-data-api.com/api/users/random_user').json()
        first = r["first_name"]
        last = r["last_name"]
        phonenum = r["phone_number"]
        addy = r["address"]["street_address"]
        dob = r["date_of_birth"]
        state = r["address"]["state"]
        gender = r["gender"]
        sin = r["social_insurance_number"]
        print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Fake Identity Generated Successfully")
        await ctx.message.edit(content=f"stxrm >> Fake Identity Generated!\n```First Name: {first}\nLast Name: {last}\nDate of Birth: {dob}\nGender: {gender}\nSocial Insurance Number: {sin}\nPhone Number: {phonenum}\nState: {state}\nAddress: {addy}```")

@bot.command()
async def passwordgen(ctx, length: int):
    if str(ctx.message.author) == username:
        await ctx.message.edit(content=f"stxrm >> Generating secure password...")
        print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Generating secure password...")
        password = ''.join(random.choice('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789!@#$%^&*()[];/.,<>?:"|{}') for i in range(length))
        await ctx.message.edit(content=f"sxtrm >> Password generated. Check your console.")
        print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Generated Password: {password}")

@bot.command()
async def tokeninfo(ctx, *, token):
    if str(ctx.message.author) == username:
        print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Grabbing token information")
        r = requests.get(apiurl, headers=headers)
        if r.status_code == 200:
            r = r.json()
            username = r["username"]
            tag = r["discriminator"]
            userid = r["id"]
            email = r["email"]
            phonenum = r["phone"]
            publicflags = r["public_flags"]
            avatar = r["avatar"]
            nitro = ""
            if "premium_type" in r:
                if r["premium_type"] == 0:
                    nitro = "None"
                elif r["premium_type"] == 1:
                    nitro = "Nitro CLassic"
                elif r["premium_type"] == 2:
                    nitro = "Nitro"
            else:
                nitro = "None"
            bio = r["bio"]
            if bio == "":
                bio = " "
            print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Token info grabbed successfully")
            await ctx.message.edit(content=f"stxrm >> Grabbed information about token:\n```Username: {username}#{tag}\nID: {userid}\nEmail: {email}\nPhone Number: {phonenum}\nAvatar: {avatar}\nPublic Flags: {publicflags}\nNitro Type: {nitro}")
            await ctx.send(f"```Bio (if any): {bio}")
        else:
            print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Failed to obtain token info, the token is either invalid or belongs to a terminated/deleted user.")
            await ctx.message.edit(content=f"stxrm >> Failed to obtain information about the token. This token is either invalid or belongs to a terminated/deleted user.")

@bot.command()
async def userinfo(ctx, *, user: discord.User):
    if str(ctx.message.author) == username:
        createdat = user.created_at.strftime("%d %B, %Y")
        print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Grabbed information about {str(user.name)}#{str(user.discriminator)}")
        await ctx.message.edit(content=f"stxrm >> User information:\n```Username: {str(user.name)}#{str(user.discriminator)}\nUser ID: {str(user.id)}\nAccount Created At: {createdat}\nAvatar URL: {user.avatar_url}```")

@bot.command()
async def ghostping(ctx, *, user: discord.User):
    if str(ctx.message.author) == username:
        print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Ghost pinged {str(user.name)}#{str(user.discriminator)}")
        await ctx.message.delete()

@bot.command()
async def length(ctx, *, string):
    if str(ctx.message.author) == username:
        stringlength = len(string)
        print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Length of given string: {stringlength}")
        await ctx.message.edit(content=f"stxrm >> Length of string: {stringlength}\nGiven string: `{string}`")

@bot.command()
async def proxycheck(ctx, *, string):
    if str(ctx.message.author) == username:
        print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Checking if given IP ({string}) is proxy or VPN")
        l = requests.get(f"http://ip-api.com/json/{string}?fields=66846719").json()
        xs = l["as"].split()[0]
        try:
            x = open('data/asn-list.txt', 'r')
            f = x.read().splitlines()
            asn = xs
            if xs in f:
                print(f'{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Detected possible proxy via ASN comparison - IP: {string}')
                await ctx.message.edit(content=f'stxrm >> Detected possible proxy via ASN comparison - Info: \n```IP: {string} \nCountry: {l["country"]}, \nISP: {l["isp"]}, \nASN: {l["as"]}, \nRegion Name: {l["regionName"]}, \nCity: {l["city"]}```')
                x.close()
            else:
                try:
                    x.close()
                    query = { 'ipAddress': f'{string}', 'maxAgeInDays': '365', }
                    headers = { 'Accept': 'application/json', 'Key': f'{abuseipdbkey}', }
                    apx = requests.get("https://api.abuseipdb.com/api/v2/check", headers=headers, params=query)
                    apxr = json.loads(apx.text)
                    with open('abuseipdb.json', 'w') as f:                
                        apxd = json.dump(apxr, f, sort_keys=True)
                        f.close()
                    with open('abuseipdb.json', 'r') as f:
                        apxd = json.load(f)
                        score = apxd["data"]["abuseConfidenceScore"]
                        reports = apxd["data"]["totalReports"]

                    px = requests.get(f"http://proxycheck.io/v2/{string}?key={proxycheckkey}&vpn=1&asn=1").json()
                    proxy = px[f"{string}"]["proxy"]
                    iptype = px[f"{string}"]["type"]
                    if proxy == "yes":
                        print(f'{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Detected possible proxy via proxycheck.io - IP: {string}')
                        await ctx.message.edit(content=f'stxrm >> Detected possible proxy via proxycheck.io - Info:\n```IP: {string} \nCountry: {l["country"]}, \nISP: {l["isp"]}, \nASN: {l["as"]}, \nRegion Name: {l["regionName"]}, \nCity: {l["city"]}\n\nType: {iptype}\nAbuse Confidence Score: {score}\nTotal Reports: {reports}```')
                    elif iptype == "VPN":
                        print(f'{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Detected possible VPN via proxycheck.io - IP: {string}')
                        await ctx.message.edit(content=f'stxrm >> Detected possible VPN via proxycheck.io - Info:\n```IP: {string} \nCountry: {l["country"]}, \nISP: {l["isp"]}, \nASN: {l["as"]}, \nRegion Name: {l["regionName"]}, \nCity: {l["city"]}\n\nType: {iptype}\nAbuse Confidence Score: {score}\nTotal Reports: {reports}```')
                    elif score > 5 or reports > 2:
                        print(f'{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Detected possible malicious IP via AbuseIPDB - IP: {string}')
                        await ctx.message.edit(content=f'stxrm >> Detected possible malicious IP via AbuseIPDB - Info:\n```IP: {string} \nCountry: {l["country"]}, \nISP: {l["isp"]}, \nASN: {l["as"]}, \nRegion Name: {l["regionName"]}, \nCity: {l["city"]}\n\nType: {iptype}\nAbuse Confidence Score: {score}\nTotal Reports: {reports}```')
                    else:
                        print(f'{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Detected no Proxy/VPN, if you are 100% sure this is a Proxy then it may be a Residental Proxy.')
                        await ctx.message.edit(content=f'stxrm >> No Proxy/VPN Detected. IP Info:\n```Country: {l["country"]}, \nISP: {l["isp"]}, \nASN: {l["as"]}, \nRegion Name: {l["regionName"]}, \nCity: {l["city"]}\n\nType: {iptype}\nAbuse Confidence Score: {score}\nTotal Reports: {reports}```')

                except Exception as e:
                    print(f'{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} An error has occured whilst checking `{string}`\n{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Info: `{e}`')
                    await ctx.message.edit(content=f'stxrm >> An error has occured whilst checking `{string}`, check your console')
                    
        except Exception as e:
            print(f'{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} An error has occured whilst checking `{string}`\n{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Info: `{e}`')
            await ctx.message.edit(content=f'stxrm >> An error has occured whilst checking `{string}`, check your console')

@bot.command()
async def geoip(ctx, *, string):
    if str(ctx.message.author) == username:
        ip = string
        l = requests.get(f"http://ip-api.com/json/{ip}?fields=66846719").json()
        print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Grabbed IP Info for: {ip}")
        await ctx.message.edit(content='stxrm >> IP Info:\n```Country: {l["country"]}, \nISP: {l["isp"]}, \nASN: {l["as"]}, \nRegion Name: {l["regionName"]}, \nCity: {l["city"]}')

@bot.command()
async def friendbackup(ctx):
    if str(ctx.message.author) == username:
        await ctx.message.edit(content='stxrm >> Backing up all friends')
        print(f"{Fore.YELLOW}stxrm - Friends Backup {Fore.RED}>>{Fore.WHITE} Backing up friends list")
        print(f"{Fore.YELLOW}stxrm - Friends Backup {Fore.RED}>>{Fore.WHITE} Getting list of all friends")
        r = requests.get('https://discord.com/api/v6/users/@me/relationships', headers=headers).json()
        ids = []
        blockedIds = []
        incoming = []
        outgoing = []
        for item in r:
            if item["type"] == 1:
                print(f'{Fore.YELLOW}stxrm - Friends Backup {Fore.RED}>>{Fore.WHITE} Backed up {str(item["user"]["username"])}#{str(item["user"]["discriminator"])}')
                ids.append(str(item["id"]) + " : " + str(item["user"]["username"]) + "#" + str(item["user"]["discriminator"]))
            if item["type"] == 2:
                print(f'{Fore.YELLOW}stxrm - Friends Backup {Fore.RED}>>{Fore.WHITE} Backed up blocked user: {str(item["user"]["username"])}#{str(item["user"]["discriminator"])}')
                blockedIds.append(str(item["id"]) + " : " + str(item["user"]["username"]) + "#" + str(item["user"]["discriminator"]))
            if item["type"] == 3:
                print(f'{Fore.YELLOW}stxrm - Friends Backup {Fore.RED}>>{Fore.WHITE} Skipping over incoming friend requests')
            if item["type"] == 4:
                print(f'{Fore.YELLOW}stxrm - Friends Backup {Fore.RED}>>{Fore.WHITE} Backed up an outgoing friend request: {str(item["user"]["username"])}#{str(item["user"]["discriminator"])}')
        print(f'{Fore.YELLOW}stxrm - Friends Backup {Fore.RED}>>{Fore.WHITE} Backed up friends list successfully!')
        await ctx.send('stxrm >> Backed up friends list successfully, info:\n```Friends - {len(ids)}\nBlocked - {len(blockedIds)}\nOutgoing Friend Requests: {len(outgoing)}```')

        if not ids:
            ids.append("Could not find any friends")
        if not blockedIds:
            blockedIds.append("Could not find any blocked users")
        if not outgoing:
            outgoing.append("Could not find any outgoing friend requests")

        f = codecs.open('data/friends.txt', 'w', encoding='utf-8')
        f.write("Current Friends\n---------------\n" + "\n".join(ids) + "\n \nOutgoing Friend Requests\n---------------\n" + "\n".join(outgoing) + "\n \nBlocked Users\n---------------\n" + "\n".join(blockedIds))
        f.close()

@bot.command()
async def serverbackup(ctx):
    if str(ctx.message.author) == username:
        await ctx.message.edit(content="stxrm >> Backing up a list of all servers")
        print(f"{Fore.YELLOW}stxrm - Server Backup {Fore.RED}>>{Fore.WHITE} Backing up server list")
        DiscumClient = discum.Client(token=token, user_agent=random_ua(), log=False)
        print(f"{Fore.YELLOW}stxrm - Server Backup {Fore.RED}>>{Fore.WHITE} Saving and creating invites for your servers with a 3 second timeout interval...")
        r = requests.get('https://discordapp.com/api/v6/users/@me/guilds', headers=headers).json()
        print(f"{Fore.YELLOW}stxrm - Server Backup {Fore.RED}>>{Fore.WHITE} Grabbing list of all servers")
        guildIdsAndInvites = []
        for item in guilds:
            guildid = item["id"]
            guildname = item["name"]
            invite = ""
            print(f"{Fore.YELLOW}stxrm - Server Backup {Fore.RED}>>{Fore.WHITE} Attempting to create invite for {guildname}")
            server = discord.utils.get(bot.guilds, id=int(guildid))
            for channel in server.text_channels:
                if invite == "":
                    invite = DiscumClient.createInvite(str(channel.id))
                    if invite.status_code == 200:
                        invite = invite.json()["code"]
                    else:
                        invite = ""
                    break
                if invite == "":
                    invite = f"Failed to create an invite for {guildname}"
                guildIdsAndInvites.append(item["name"] + " : " +str(item["id"]) + " : discord.gg/" + str(invite))
                await asyncio.sleep(3)
            print(f"{Fore.YELLOW}stxrm - Server Backup {Fore.RED}>>{Fore.WHITE} Saved list of servers successfully")
            f = codecs.open('data/servers.txt', 'w', encoding='utf-8')
            f.write("\n".join(guildIdsAndInvites))
            f.close()
            await ctx.send("stxrm >> Backed up a list of all your servers including their IDs")

@bot.command()
async def webhookinfo(ctx, *, string):
    if str(ctx.message.author) == username:
        print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Getting information about webhook...")
        await ctx.message.edit(content="stxrm >> Grabbing webhook info...")
        r = requests.get(string)
        if r.status_code == 401:
            print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Could not obtain info on webhook due to it being invalid")
            await ctx.message.edit(content="stxrm >> Invalid Webhook!")
        if r.status_code == 200:
            print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Got information on webhook successfully")
            rj = r.json()
            name = rj["name"]
            avatar = rj["avatar"]
            guildid = rj["guild_id"]
            chanid = rj["channel_id"]
            hookid = rj["id"]
            await ctx.message.edit(content=f"stxrm >> Webhook Information:\n```Webhook Name: {name}\nAvatar: {avatar}\nServer ID: {guildid}\nChannel ID: {chanid}\nWebhook ID: {hookid}```")

@bot.command()
async def deletewebhook(ctx, *, string):
    if str(ctx.message.author) == username:
        print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Attempting to delete provided webhook...")
        await ctx.message.edit(content="stxrm >> Attempting to delete webhook...")
        r = requests.delete(string)
        if r.status_code == 404:
            print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Could not delete webhook as it is invalid")
            await ctx.message.edit(content="stxrm >> Could not delete the webhook as it is invalid")
        if r.status_code == 204:
            print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Successfully deleted provided webhook")
            await ctx.message.edit(content="stxrm >> Successfully deleted webhook")

@bot.command()
async def spamwebhook(ctx, amount: int, url, *, message=None):
    if str(ctx.message.author) == username:
        print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Spamming webhook {amount} amount of time(s)")
        await ctx.message.edit(content=f"stxrm >> Spamming provided webhook {amount} amount of time(s)")
        if message is None:
            for i in range(amount):
                spamMessage = ''.join(random.choice('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789!@#$%^&*()[];/.,<>?:"|{}') for i in range(2000))
                payload = { 'username': 'stxrm', 'avatar_url': 'https://cdn.discordapp.com/icons/725377441740095489/44f2d1df0af75fd0d8748e56c5847742.webp', 'content': f'{spamMessage}' }
                r = requests.post(url, json=payload)
        else:
            for i in range(amount):
                payload = { 'username': 'stxrm', 'avatar_url': 'https://cdn.discordapp.com/icons/725377441740095489/44f2d1df0af75fd0d8748e56c5847742.webp', 'content': f'{message}' }
        print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Finished spamming webhook")
        await ctx.send(f"stxrm >> Finished spamming webhook {amount} amount of times")

@bot.command()
async def createwebhook(ctx):
    if str(ctx.message.author) == username:
        print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Attempting to create new webhook")
        await ctx.message.edit(content="stxrm >> Attempting to create new webhook")
        try:
            webhook = await ctx.channel.create_webhook(name="stxrm", reason="stxrm Selfbot")
            print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Successfully created new webhook\n{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} {webhook.url}")
            await ctx.message.edit(content="stxrm >> Successfully created a new webhook, check console")
        except Exception as e:
            print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} An error has occured whilst trying to create the webhook")
            await ctx.message.edit("stxrm >> An error has occured whilst trying to create the webhook")

@bot.command()
async def nukeserver(ctx):
    if str(ctx.message.author) == username:
        print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Attempting to nuke server")
        await ctx.message.delete()
        if ctx.author.guild.permissions.administrator:
            try:
                print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Attempting to delete every channel")
                await channel.delete()
            except:
                pass
            for role in ctx.guild.roles:
                try:
                    print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Attempting to delete every role")
                    await role.delete()
                except:
                    pass
    else:
        print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Missing permissions")
        await ctx.send("stxrm >> Missing permissions", delete_after=1s)

@bot.command()
async def spacechannel(ctx, *, chanName = "Channel Name"):
    if str(ctx.message.author) == username:
        chanName = chanName.replace(" ", "ㅤ")
        await ctx.guild.create_text_channel(name=chanName)
        print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Made a channel with a space in it successfully")
        await ctx.message.edit(content="stxrm >> Made channel with space successfully")

@bot.command()
async def ping(ctx, *, dns):
    if str(ctx.message.author) == username:
        await ctx.message.edit(content="stxrm >> Pinging Domain/IP")
        print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Pinging Domain/IP ({dns})")
        output = subprocess.run(f"ping {dns}, text=True, stdout=subprocess.PIPE").stdout.splitlines()
        values = "".join(output[-1:])[4:].split(", ")
        minimum = values[0][len("Minimum = "):]
        maximum = values[1][len("Maximum = "):]
        avg = values[2][len("Average = "):]
        addy = output[1].replace(f"Pinging {dns} [", "").replace("] with 32 bytes of data:", "")
        await ctx.message.edit(content=f"stxrm >> Finished pinging {dns}\n```IP: {addy}\nMin: {minimum}\nMax: {maximum}\nAvg: {average}```")
        print(f"{Fore.YELLOW}stxrm {Fore.RED}>>{Fore.WHITE} Finished pinging Domain/IP ({dns})")


bot.run(f'{token}', bot=False) 
