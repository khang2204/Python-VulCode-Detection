def _DoMD(self, path):...
extensions = ['markdown.extensions.def_list',
    'markdown.extensions.fenced_code', 'markdown.extensions.tables',
    'markdown.extensions.toc', 'gitiles_autolink', 'gitiles_ext_blocks',
    'gitiles_smart_quotes']
extension_configs = {'markdown.extensions.toc': {'slugify': _gitiles_slugify}}
contents = self._Read(path[1:])
md = markdown.Markdown(extensions=extensions, extension_configs=
    extension_configs, tab_length=2, output_format='html4')
has_a_single_h1 = len([line for line in contents.splitlines() if line.
    startswith('#') and not line.startswith('##')]) == 1
md.treeprocessors['adjust_toc'] = _AdjustTOC(has_a_single_h1)
md_fragment = md.convert(contents).encode('utf-8')
self._WriteHeader('text/html')
self._WriteTemplate('header.html')
self.wfile.write('<div class="doc">')
self.wfile.write(md_fragment)
self.wfile.write('</div>')
self._WriteTemplate('footer.html')
