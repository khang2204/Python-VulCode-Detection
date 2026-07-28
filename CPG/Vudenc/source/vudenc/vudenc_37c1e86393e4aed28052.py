def _check_status():...
pod_info = k8s_client.read_namespaced_pod(name='busybox', namespace='default')
assert pod_info.status.phase == 'Running', "Wrong status for 'busybox' Pod - found {status}".format(
    status=pod_info.status.phase)
