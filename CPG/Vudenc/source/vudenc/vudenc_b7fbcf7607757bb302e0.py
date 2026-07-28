import json
import time
import pytest
from pytest_bdd import scenario, then, parsers
from tests import kube_utils
from tests import utils
@scenario('../features/pods_alive.feature', 'List Pods')...
@scenario('../features/pods_alive.feature', 'Exec in Pods')...
@scenario('../features/pods_alive.feature', 'Expected Pods')...
@then(parsers.parse(...
cmd = (
    'kubectl --kubeconfig=/etc/kubernetes/admin.conf get {0} --namespace {1} -o custom-columns=:metadata.name'
    )
cmd_res = host.check_output(cmd.format(resource, namespace))
assert len(cmd_res.strip()) > 0, 'No {0} found in namespace {1}'.format(
    resource, namespace)
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
@then(parsers.parse(...
def _check_pods_count():...
pods = kube_utils.get_pods(host, label, namespace='kube-system',
    status_phase='Running')
assert len(pods) >= min_pods_count
utils.retry(_check_pods_count, times=10, wait=3)
