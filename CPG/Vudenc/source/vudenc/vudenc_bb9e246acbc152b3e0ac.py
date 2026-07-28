def _cliq_run_xml(self, verb, cliq_args, check_cliq_result=True):...
"""docstring"""
cliq_args['output'] = 'XML'
out, _err = self._cliq_run(verb, cliq_args, check_cliq_result)
LOG.debug(_('CLIQ command returned %s'), out)
result_xml = etree.fromstring(out)
if check_cliq_result:
response_node = result_xml.find('response')
return result_xml
if response_node is None:
msg = _(
    'Malformed response to CLIQ command %(verb)s %(cliq_args)s. Result=%(out)s'
    ) % {'verb': verb, 'cliq_args': cliq_args, 'out': out}
result_code = response_node.attrib.get('result')
if result_code != '0':
msg = _('Error running CLIQ command %(verb)s %(cliq_args)s.  Result=%(out)s'
    ) % {'verb': verb, 'cliq_args': cliq_args, 'out': out}
