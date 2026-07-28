def assemble_stack(self):...
self.overlay = Gtk.Overlay()
unlock_failed_overlay = self.builder.get_object('unlock_failed_overlay')
self.overlay.add_overlay(unlock_failed_overlay)
stack = Gtk.Stack()
stack.set_transition_type(Gtk.StackTransitionType.CROSSFADE)
self.unlock_database_stack_box = self.builder.get_object(
    'unlock_database_stack_box')
unlock_database_stack_switcher = self.builder.get_object(
    'unlock_database_stack_switcher')
unlock_database_stack_switcher.set_stack(stack)
password_unlock_stack_page = self.builder.get_object(
    'password_unlock_stack_page')
keyfile_unlock_stack_page = self.builder.get_object('keyfile_unlock_stack_page'
    )
composite_unlock_stack_page = self.builder.get_object(
    'composite_unlock_stack_page')
stack.add_titled(password_unlock_stack_page, 'password_unlock', 'Password')
stack.child_set_property(password_unlock_stack_page, 'icon-name',
    'input-dialpad-symbolic')
stack.add_titled(keyfile_unlock_stack_page, 'keyfile_unlock', 'Keyfile')
stack.child_set_property(keyfile_unlock_stack_page, 'icon-name',
    'mail-attachment-symbolic')
stack.add_titled(composite_unlock_stack_page, 'composite_unlock', 'Composite')
stack.child_set_property(composite_unlock_stack_page, 'icon-name',
    'insert-link-symbolic')
self.overlay.add(stack)
self.unlock_database_stack_box.add(self.overlay)
self.unlock_database_stack_box.show_all()
self.parent_widget.add(self.unlock_database_stack_box)
