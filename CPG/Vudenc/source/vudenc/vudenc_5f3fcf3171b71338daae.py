def header(app):...
print(
    """
    [{header}{bold}YunoHost App Package Linter{end}]

 App packaging documentation - https://yunohost.org/#/packaging_apps
 App package example         - https://github.com/YunoHost/example_ynh
 Official helpers            - https://yunohost.org/#/packaging_apps_helpers_en
 Experimental helpers        - https://github.com/YunoHost-Apps/Experimental_helpers

    Analyzing package {header}{app}{end}"""
    .format(header=c.HEADER, bold=c.BOLD, end=c.END, app=app))
