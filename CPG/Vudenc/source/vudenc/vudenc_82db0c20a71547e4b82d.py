def create_website_http_handler(purpose, config):...
locale_provider = lambda : None
if config.secure_cookie_salt:
set_secure_cookie_salt(config.secure_cookie_salt)
set_inline_static_files_directory(VEIL_VAR_DIR / 'inline-static-files')
set_external_static_files_directory(VEIL_HOME / 'static')
master_template_directory = config.master_template_directory
if master_template_directory:
register_template_loader('master', FileSystemLoader(master_template_directory))
website_context_managers = [create_stack_context(install_translations,
    locale_provider)]
if config.prevents_xsrf:
register_page_post_processor(set_xsrf_cookie_for_page)
if config.recalculates_static_file_hash:
website_context_managers.append(prevent_xsrf)
website_context_managers.append(clear_static_file_hashes)
if config.clears_template_cache:
website_context_managers.append(clear_template_caches)
website_context_managers.extend(additional_context_managers.get(purpose, []))
return RoutingHTTPHandler(get_routes(purpose), website_context_managers)
