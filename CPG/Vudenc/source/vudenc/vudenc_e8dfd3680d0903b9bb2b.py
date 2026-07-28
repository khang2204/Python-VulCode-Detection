def run(self, tree):...
for toc_node in tree.findall(".//*[@class='toc']"):
toc_ul = toc_node[0]
if self.has_a_single_h1:
toc_ul_li = toc_ul[0]
ul_with_the_desired_toc_entries = toc_ul
ul_with_the_desired_toc_entries = toc_ul_li[1]
toc_node.remove(toc_ul)
contents = ElementTree.SubElement(toc_node, 'h2')
contents.text = 'Contents'
contents.tail = '\n'
toc_aux = ElementTree.SubElement(toc_node, 'div', {'class': 'toc-aux'})
toc_aux.text = '\n'
toc_aux.append(ul_with_the_desired_toc_entries)
toc_aux.tail = '\n'
