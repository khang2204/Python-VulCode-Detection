@classmethod...
if package_manager not in cls.VALID_PACKAGE_MANAGER_LIST.keys():
package_manager = cls.VALID_PACKAGE_MANAGER_LIST[package_manager]
return package_manager
