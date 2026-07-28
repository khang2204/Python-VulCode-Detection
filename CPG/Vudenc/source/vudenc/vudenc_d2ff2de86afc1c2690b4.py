def hide_unlock_failed_revealer(self):...
unlock_failed_revealer = self.builder.get_object('unlock_failed_revealer')
unlock_failed_revealer.set_reveal_child(not unlock_failed_revealer.
    get_reveal_child())
