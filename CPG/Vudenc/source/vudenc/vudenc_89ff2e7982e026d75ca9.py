def get(self):...
"""docstring"""
"""
        # Check the request comes from appropriate location.
        if not utils.validate_ip(request.remote_addr)
            return {}, 403
        """
page = int(request.args.get('page'))
response = db_interac.get_messages(page)
return response, 200
