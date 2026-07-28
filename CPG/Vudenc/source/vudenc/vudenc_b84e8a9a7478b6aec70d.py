from __future__ import absolute_import, division, print_function, with_statement
import os
import sys
import argparse
if __name__ == '__main__':
parser = argparse.ArgumentParser(description='See README')
parser.add_argument('-c', '--count', default=3, type=int, help=
    'with how many failure times it should be considered as an attack')
config = parser.parse_args()
ips = {}
banned = set()
for line in sys.stdin:
if 'can not parse header when' in line:
ip = line.split()[-1].split(':')[-2]
if ip not in ips:
ips[ip] = 1
ips[ip] += 1
print(ip)
if ip not in banned and ips[ip] >= config.count:
sys.stdout.flush()
banned.add(ip)
cmd = 'iptables -A INPUT -s %s -j DROP' % ip
print(cmd, file=sys.stderr)
sys.stderr.flush()
os.system(cmd)
