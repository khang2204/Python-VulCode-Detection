@pytest.fixture...
config.load_kube_config(config_file=kubeconfig)
k8s_client = client.CoreV1Api()
pod_manifest = os.path.join(os.path.realpath(os.path.dirname(__file__)),
    'files', 'busybox.yaml')
pod_manifest_content = yaml.safe_load(pod_fd)
k8s_client.create_namespaced_pod(body=pod_manifest_content, namespace='default'
    )
def _check_status():...
pod_info = k8s_client.read_namespaced_pod(name='busybox', namespace='default')
assert pod_info.status.phase == 'Running', "Wrong status for 'busybox' Pod - found {status}".format(
    status=pod_info.status.phase)
utils.retry(_check_status, times=10)
yield 'busybox'
k8s_client.delete_namespaced_pod(name='busybox', namespace='default', body=
    client.V1DeleteOptions())
