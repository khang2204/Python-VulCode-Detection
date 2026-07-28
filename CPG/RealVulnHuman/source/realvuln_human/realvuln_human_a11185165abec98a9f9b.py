# Presence of context only matters for Protect.
        context = contrast.CS__CONTEXT_TRACKER.current()

        # The goal here is to ensure that a request context
        # still exists in a child thread even if the parent thread exited.
        if context is None:
            # If context is None we will not finish the thread's work.
            print("Context is None")
            sys.exit(1)

    cmd = "echo " + str(user_input)
    os.system(cmd)

    # Do NOT remove this print as it is used in a testing assertion.
    print("finished background thread")


class ThreadView(object):
    def on_get(self, req, resp):
        """View that creates a child thread for some work"""
        user_input = req.get_param("user_input") or ""
        threading.Thread(target=thread_function, args=(user_input,)).start()
