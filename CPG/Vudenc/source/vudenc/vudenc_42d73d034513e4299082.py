def show_unlock_failed_revealer(self):...
unlock_failed_box = self.builder.get_object('unlock_failed_box')
context = unlock_failed_box.get_style_context()
context.add_class('NotifyRevealer')
unlock_failed_revealer = self.builder.get_object('unlock_failed_revealer')
unlock_failed_revealer.set_reveal_child(not unlock_failed_revealer.
    get_reveal_child())
revealer_timer = threading.Timer(3.0, self.hide_unlock_failed_revealer)
revealer_timer.start()
