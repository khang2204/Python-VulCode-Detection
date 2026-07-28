"""
Smoke test to see if Spinnaker can interoperate with Amazon Web Services.

See testable_service/integration_test.py and spinnaker_testing/spinnaker.py
for more details.

The smoke test will use ssh to peek at the spinnaker configuration
to determine the managed project it should verify, and to determine
the spinnaker account name to use when sending it commands.

Sample Usage:
    Assuming you have created $PASSPHRASE_FILE (which you should chmod 400)
    and $CITEST_ROOT points to the root directory of this repository
    (which is . if you execute this from the root)

  PYTHONPATH=$CITEST_ROOT:$CITEST_ROOT/spinnaker     python $CITEST_ROOT/spinnaker/spinnaker_system/smoke_test.py     --gce_ssh_passphrase_file=$PASSPHRASE_FILE     --gce_project=$PROJECT     --gce_zone=$ZONE     --gce_instance=$INSTANCE
    --test_aws_zone=$AWS_ZONE     --aws_profile=$AWS_PROFILE
or
  PYTHONPATH=$CITEST_ROOT:$CITEST_ROOT/spinnaker     python $CITEST_ROOT/spinnaker/spinnaker_system/smoke_test.py     --native_hostname=host-running-smoke-test
    --test_aws_zone=$AWS_ZONE     --aws_profile=$AWS_PROFILE

  Note that the $AWS_ZONE is not directly used, rather it is a standard
  parameter being used to infer the region. The test is going to pick
  some different availability zones within the region in order to test kato.
  These are currently hardcoded in.
"""
import sys
import citest.aws_testing as aws
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
