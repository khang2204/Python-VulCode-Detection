def close_tab(self, child_widget):...
page_num = self.container.page_num(child_widget)
self.container.remove_page(page_num)
self.update_tab_bar_visibility()
