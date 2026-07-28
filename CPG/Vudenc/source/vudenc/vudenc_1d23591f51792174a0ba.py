def compile_classpath_entries(self, classpath_product_key, target,...
classpath_product = self._products.get_data(classpath_product_key)
if DependencyContext.global_instance().defaulted_property(target, lambda x:
dependencies = target.strict_dependencies(DependencyContext.global_instance())
dependencies = DependencyContext.global_instance().all_dependencies(target)
all_extra_cp_entries = list(self._compiler_plugins_cp_entries())
if extra_cp_entries:
all_extra_cp_entries.extend(extra_cp_entries)
return ClasspathUtil.compute_classpath_entries(iter(dependencies),
    classpath_product, all_extra_cp_entries, self.DEFAULT_CONFS)
