def main():...
query = init()
print('##################################')
print('#       retail application       #')
print('##################################')
id = get_customer_id(query)
print("""
     type 'help' for query info""")
print("     enter 'quit' to exit\n")
print('>', end='')
line = input()
line.replace('\\s*', ' ')
tok = line.split()
while len(tok) > 0 and tok[0] != 'quit' and tok[0] != 'exit':
handle_query(tok, id, query)
print('>', end='')
line = input()
line = line.replace('\\s*', ' ')
tok = line.split()
