"""
Tests to see if CloudDriver/Kato can interoperate with Amazon Web Services.

Sample Usage:
    Assuming you have created $PASSPHRASE_FILE (which you should chmod 400):
    and $CITEST_ROOT points to the root directory of this repository
    (which is . if you execute this from the root)
    and $AWS_PROFILE is the name of the aws_cli profile for authenticating
    to observe aws resources:

    This first command would be used if Spinnaker itself was deployed on GCE.
    The test needs to talk to GCE to get to spinnaker (using the gce_* params)
    then talk to AWS (using the aws_profile with the aws cli program) to
    verify Spinnaker had the right effects on AWS.

    PYTHONPATH=$CITEST_ROOT:$CITEST_ROOT/spinnaker        python $CITEST_ROOT/spinnaker/spinnaker_system/aws_kato_test.py        --gce_ssh_passphrase_file=$PASSPHRASE_FILE        --gce_project=$PROJECT        --gce_zone=$GCE_ZONE        --gce_instance=$INSTANCE        --test_aws_zone=$AWS_ZONE        --aws_profile=$AWS_PROFILE

   or

     This second command would be used if Spinnaker itself was deployed some
     place reachable through a direct IP connection. It could be, but is not
     necessarily deployed on GCE. It is similar to above except it does not
     need to go through GCE and its firewalls to locate the actual IP endpoints
     rather those are already known and accessible.

     PYTHONPATH=$CITEST_ROOT:$CITEST_ROOT/spinnaker        python $CITEST_ROOT/spinnaker/spinnaker_system/aws_kato_test.py        --native_hostname=host-running-kato
       --test_aws_zone=$AWS_ZONE        --aws_profile=$AWS_PROFILE

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
import spinnaker_testing.kato as kato
"""Defines the scenario for the test.

  This scenario defines the different test operations.
  We're going to:
    Create a Load Balancer
    Delete a Load Balancer
  """
__use_lb_name = ''
@classmethod...
"""docstring"""
return kato.new_agent(bindings)
