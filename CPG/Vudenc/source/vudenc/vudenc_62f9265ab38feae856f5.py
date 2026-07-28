@then(parsers.parse(...
candidates = kube_utils.get_pods(host, label, namespace)
assert len(candidates
    ) == 1, 'Expected one (and only one) pod with label {l}, found {f}'.format(
    l=label, f=len(candidates))
pod = candidates[0]
cmd = ' '.join(['kubectl', '--kubeconfig=/etc/kubernetes/admin.conf',
    'exec', '--namespace {0}'.format(namespace), pod['metadata']['name'],
    command])
host.check_output(cmd)
