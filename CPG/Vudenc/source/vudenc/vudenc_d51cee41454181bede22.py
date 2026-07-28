"""
Smoke test to see if Spinnaker can interoperate with Google Cloud Platform.

See testable_service/integration_test.py and spinnaker_testing/spinnaker.py
for more details.

The smoke test will use ssh to peek at the spinnaker configuration
to determine the managed project it should verify, and to determine
the spinnaker account name to use when sending it commands.

Sample Usage:
    Assuming you have created $PASSPHRASE_FILE (which you should chmod 400)
    and $CITEST_ROOT points to the root directory of this repository
    (which is . if you execute this from the root)

  PYTHONPATH=$CITEST_ROOT:$CITEST_ROOT/spinnaker     python $CITEST_ROOT/spinnaker/spinnaker_system/google_smoke_test.py     --gce_ssh_passphrase_file=$PASSPHRASE_FILE     --gce_project=$PROJECT     --gce_zone=$ZONE     --gce_instance=$INSTANCE
or
  PYTHONPATH=$CITEST_ROOT:$CITEST_ROOT/spinnaker     python $CITEST_ROOT/spinnaker/spinnaker_system/google_smoke_test.py     --native_hostname=host-running-smoke-test
    --managed_gce_project=$PROJECT     --test_gce_zone=$ZONE
"""
import sys
import citest.gcp_testing as gcp
import citest.json_contract as jc
import citest.service_testing as st
import spinnaker_testing as sk
import spinnaker_testing.gate as gate
"""Defines the scenario for the smoke test.

  This scenario defines the different test operations.
  We're going to:
    Create a Spinnaker Application
    Create a Load Balancer
    Create a Server Group
    Delete each of the above (in reverse order)
  """
@classmethod...
"""docstring"""
return gate.new_agent(bindings)
