def _check_pods_count():...
pods = kube_utils.get_pods(host, label, namespace='kube-system',
    status_phase='Running')
assert len(pods) >= min_pods_count
