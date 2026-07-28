def test_xml(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 1, 'HIGH': 4}, 'CONFIDENCE': {'HIGH': 1,
    'MEDIUM': 4}}
self.check_example('xml_etree_celementtree.py', expect)
expect = {'SEVERITY': {'LOW': 1, 'HIGH': 2}, 'CONFIDENCE': {'HIGH': 1,
    'MEDIUM': 2}}
self.check_example('xml_expatbuilder.py', expect)
expect = {'SEVERITY': {'LOW': 3, 'HIGH': 1}, 'CONFIDENCE': {'HIGH': 3,
    'MEDIUM': 1}}
self.check_example('xml_lxml.py', expect)
expect = {'SEVERITY': {'LOW': 2, 'HIGH': 2}, 'CONFIDENCE': {'HIGH': 2,
    'MEDIUM': 2}}
self.check_example('xml_pulldom.py', expect)
expect = {'SEVERITY': {'HIGH': 1}, 'CONFIDENCE': {'HIGH': 1}}
self.check_example('xml_xmlrpc.py', expect)
expect = {'SEVERITY': {'LOW': 1, 'HIGH': 4}, 'CONFIDENCE': {'HIGH': 1,
    'MEDIUM': 4}}
self.check_example('xml_etree_elementtree.py', expect)
expect = {'SEVERITY': {'LOW': 1, 'HIGH': 1}, 'CONFIDENCE': {'HIGH': 1,
    'MEDIUM': 1}}
self.check_example('xml_expatreader.py', expect)
expect = {'SEVERITY': {'LOW': 2, 'HIGH': 2}, 'CONFIDENCE': {'HIGH': 2,
    'MEDIUM': 2}}
self.check_example('xml_minidom.py', expect)
expect = {'SEVERITY': {'LOW': 2, 'HIGH': 6}, 'CONFIDENCE': {'HIGH': 2,
    'MEDIUM': 6}}
self.check_example('xml_sax.py', expect)
