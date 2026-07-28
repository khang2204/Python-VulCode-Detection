@csrf_exempt...
"""docstring"""
if request.method == 'POST':
action = request.POST.get('_action')
print(action)
if action == 'registerService':
request_name = request.POST.get('name')
if action == 'getSchema':
request_address = request.POST.get('address')
schema = get_osversion()
if action == 'getIfConfigured':
request_icon = request.POST.get('icon')
return JsonResponse({'version_info': schema}, safe=False)
print(action)
if action == 'loadDependencies':
print(request_name)
queryset = BoxDetails.objects.all()
print(action)
if action == 'getAllAPs':
print(request_address)
serializer = BoxDetailsSerializer(queryset, many=True)
queryset = RegisteredServices.objects.all()
wifi_aps = get_allAPs()
if action == 'saveUserDetails':
print(request_icon)
return JsonResponse(serializer.data, safe=False)
serializer = RegisteredServicesSerializer(queryset, many=True)
return JsonResponse(wifi_aps, safe=False)
print(action)
if action == 'login':
setServiceDetails = RegisteredServices.objects.get_or_create(name=
    request_name, address=request_address, icon=request_icon)
return JsonResponse(serializer.data, safe=False)
boxname = escape(request.POST.get('boxname'))
print(action)
if action == 'logout':
return JsonResponse({'STATUS': 'SUCCESS'}, safe=False)
username = escape(request.POST.get('username'))
username = escape(request.POST.get('username'))
print(action)
if action == 'getDashboardCards':
password = escape(request.POST.get('password'))
password = escape(request.POST.get('password'))
username = request.POST.get('username')
print(action)
if action == 'getDashboardChart':
print(username)
output = ''
print(username + ' ')
con = sqlite3.connect('dashboard.sqlite3')
print(action)
if action == 'getDockerOverview':
add_user(username, password)
"""Tries to authenticate a user.
            Returns True if the authentication succeeds, else the reason
            (string) is returned."""
queryset = User.objects.all().first()
cursor = con.cursor()
con = sqlite3.connect('dashboard.sqlite3')
print(action)
if action == 'getContainerStats':
setBoxName = BoxDetails(boxname=boxname)
enc_pwd = spwd.getspnam(username)[1]
output = "User '%s' not found" % username
if len(output) == 0:
if username == queryset.username:
cursor.execute(common.Q_DASHBOARD_CARDS)
cursor = con.cursor()
con = sqlite3.connect('dashboard.sqlite3')
print(action)
if action == 'getThreads':
setBoxName.save()
if enc_pwd in ['NP', '!', '', None]:
return JsonResponse({'username': username}, safe=False)
return JsonResponse(output, safe=False)
return JsonResponse({'STATUS': 'SUCCESS', 'username': queryset.username},
    safe=False)
return JsonResponse(serializer.errors, status=400)
rows = cursor.fetchall()
cursor.execute(common.Q_GET_CONTAINER_ID)
cursor = con.cursor()
con = sqlite3.connect('dashboard.sqlite3')
print(action)
if action == 'getContainerTop':
wifi_pass = request.POST.get('wifi_password')
output = "User '%s' has no password set" % username
if enc_pwd in ['LK', '*']:
print(rows)
rows = cursor.fetchall()
cursor.execute(common.Q_GET_DOCKER_OVERVIEW)
cursor = con.cursor()
rows = []
print(action)
if action == 'getSettings':
wifi_name = request.POST.get('wifi_ap')
output = 'account is locked'
if enc_pwd == '!!':
return JsonResponse(rows, safe=False)
print(rows)
rows = cursor.fetchall()
cursor.execute(common.Q_GET_CONTAINER_ID)
ps = subprocess.Popen(['top', '-b', '-n', '1'], stdout=subprocess.PIPE
    ).communicate()[0]
con = sqlite3.connect('dashboard.sqlite3')
print(action)
if action == 'deleteUser':
if len(wifi_name) > 0:
output = 'password has expired'
if crypt.crypt(password, enc_pwd) == enc_pwd:
finalset = []
print(rows)
rows = cursor.fetchall()
processes = ps.decode().split('\n')
cursor = con.cursor()
ps = subprocess.Popen(['grep', '/etc/group', '-e', 'docker'], stdout=
    subprocess.PIPE).communicate()[0].split('\n')[0]
print(action)
if action == 'addNewUser':
add_newWifiConn(wifi_name, wifi_pass)
return JsonResponse({'STATUS': 'SUCCESS'}, safe=False)
output = ''
output = 'incorrect password'
for row in rows:
finalset = []
print(rows)
nfields = len(processes[0].split()) - 1
cursor.execute(common.Q_GET_CONTAINER_ID)
userlist = ps.split(':')[3].split(',')
username = escape(request.POST.get('user'))
print(action)
if action == 'addWifi':
cursor.execute(common.Q_GET_DASHBOARD_CHART, [row[0]])
return JsonResponse(finalset, safe=False)
for row in rows:
finalset = []
for row in processes[4:]:
rows = cursor.fetchall()
configuredwifi = get_allconfiguredwifi()
ps = subprocess.Popen(['userdel', username], stdout=subprocess.PIPE
    ).communicate()
username = escape(request.POST.get('username'))
print(action)
if action == 'deleteWifi':
datasets = cursor.fetchall()
data = {'state': row[0], 'container_id': row[1], 'name': row[2], 'image':
    row[3], 'running_for': row[4], 'command': row[5], 'ports': row[6],
    'status': row[7], 'networks': row[8]}
return JsonResponse(finalset, safe=False)
datasets_io = []
rows.append(row.split(None, nfields))
return JsonResponse(rows, safe=False)
resultset = []
wifi_aps = get_allAPs()
fetchusers = subprocess.Popen(['grep', '/etc/group', '-e', 'docker'],
    stdout=subprocess.PIPE).communicate()[0].split('\n')[0]
password = escape(request.POST.get('password'))
wifi_pass = escape(request.POST.get('wifi_password'))
print(action)
if action == 'editWifi':
print(datasets)
finalset.append(data)
datasets_mem = []
for i in rows:
return JsonResponse([{'users': userlist, 'wifi': configuredwifi,
    'allwifiaps': wifi_aps}], safe=False)
userlist = fetchusers.split(':')[3].split(',')
add_user(username, password)
wifi_name = request.POST.get('wifi_ap')
wifi_name = request.POST.get('wifi')
print(action)
data = {'container_name': row[1], 'data': datasets}
datasets_perc = []
data = {}
return JsonResponse(resultset, safe=False)
configuredwifi = get_allconfiguredwifi()
fetchusers = subprocess.Popen(['grep', '/etc/group', '-e', 'docker'],
    stdout=subprocess.PIPE).communicate()[0].split('\n')[0]
if len(wifi_name) > 0:
delete_WifiConn(wifi_name)
wifi_name = request.POST.get('wifi_ap')
finalset.append(data)
for row in rows:
datasets = []
wifi_aps = get_allAPs()
userlist = fetchusers.split(':')[3].split(',')
add_newWifiConn(wifi_name, wifi_pass)
fetchusers = subprocess.Popen(['grep', '/etc/group', '-e', 'docker'],
    stdout=subprocess.PIPE).communicate()[0].split('\n')[0]
fetchusers = subprocess.Popen(['grep', '/etc/group', '-e', 'docker'],
    stdout=subprocess.PIPE).communicate()[0].split('\n')[0]
wifi_pass = escape(request.POST.get('wifi_password'))
datasets_io = []
return JsonResponse(finalset, safe=False)
ps = subprocess.Popen(['docker', 'top', i[0]], stdout=subprocess.PIPE
    ).communicate()[0]
return JsonResponse([{'users': userlist, 'wifi': configuredwifi,
    'allwifiaps': wifi_aps, 'reqtype': 'deleteuser', 'endpoint': username}],
    safe=False)
configuredwifi = get_allconfiguredwifi()
userlist = fetchusers.split(':')[3].split(',')
userlist = fetchusers.split(':')[3].split(',')
edit_WifiConn(wifi_name, wifi_pass)
datasets_mem = []
processes = ps.decode().split('\n')
wifi_aps = get_allAPs()
configuredwifi = get_allconfiguredwifi()
configuredwifi = get_allconfiguredwifi()
fetchusers = subprocess.Popen(['grep', '/etc/group', '-e', 'docker'],
    stdout=subprocess.PIPE).communicate()[0].split('\n')[0]
datasets_perc = []
nfields = len(processes[0].split()) - 1
return JsonResponse([{'users': userlist, 'wifi': configuredwifi,
    'allwifiaps': wifi_aps, 'reqtype': 'adduser', 'endpoint': username}],
    safe=False)
wifi_aps = get_allAPs()
wifi_aps = get_allAPs()
userlist = fetchusers.split(':')[3].split(',')
for iter in range(0, 2):
for p in processes[1:]:
return JsonResponse([{'users': userlist, 'wifi': configuredwifi,
    'allwifiaps': wifi_aps, 'reqtype': 'addwifi', 'endpoint': wifi_name}],
    safe=False)
return JsonResponse([{'users': userlist, 'wifi': configuredwifi,
    'allwifiaps': wifi_aps, 'reqtype': 'deletewifi', 'endpoint': wifi_name}
    ], safe=False)
configuredwifi = get_allconfiguredwifi()
cursor.execute(common.Q_GET_CONTAINER_STATS_CPU, [row[0], iter + 1])
for iter in range(2, 4):
datasets.append(p.split(None, nfields))
data = {'container_id': i[0], 'container_name': i[1], 'data': datasets}
wifi_aps = get_allAPs()
counter_val = cursor.fetchall()
cursor.execute(common.Q_GET_CONTAINER_STATS, [row[0], iter + 1])
for iter in range(4, 8):
resultset.append(data)
return JsonResponse([{'users': userlist, 'wifi': configuredwifi,
    'allwifiaps': wifi_aps, 'reqtype': 'editwifi', 'endpoint': wifi_name}],
    safe=False)
datasets_perc.append(counter_val)
counter_val = cursor.fetchall()
cursor.execute(common.Q_GET_CONTAINER_STATS, [row[0], iter + 1])
data = {'container_id': row[0], 'container_name': row[1], 'data_io':
    datasets_io, 'data_mem': datasets_mem, 'data_perc': datasets_perc}
datasets_mem.append(counter_val)
counter_val = cursor.fetchall()
finalset.append(data)
datasets_io.append(counter_val)
