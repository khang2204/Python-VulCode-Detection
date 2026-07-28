import json as json_module
import logging
import sys
from citest.service_testing import HttpContractBuilder
from citest.service_testing import NoOpOperation
import citest.gcp_testing as gcp
import citest.json_contract as jc
import citest.service_testing as st
import spinnaker_testing as sk
import spinnaker_testing.kato as kato
use_instance_names = []
use_instance_zones = []
__use_lb_name = ''
__use_lb_tp_name = ''
__use_lb_hc_name = ''
__use_lb_target = ''
__use_http_lb_name = ''
__use_http_lb_proxy_name = ''
__use_http_lb_hc_name = ''
__use_http_lb_bs_name = ''
__use_http_lb_fr_name = ''
__use_http_lb_map_name = ''
__use_http_lb_http_proxy_name = ''
@classmethod...
"""docstring"""
return kato.new_agent(bindings)
