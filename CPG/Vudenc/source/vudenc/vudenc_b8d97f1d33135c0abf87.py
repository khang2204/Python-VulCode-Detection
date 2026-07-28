@then(parsers.parse(...
cmd = (
    'kubectl --kubeconfig=/etc/kubernetes/admin.conf get {0} --namespace {1} -o custom-columns=:metadata.name'
    )
cmd_res = host.check_output(cmd.format(resource, namespace))
assert len(cmd_res.strip()) > 0, 'No {0} found in namespace {1}'.format(
    resource, namespace)
