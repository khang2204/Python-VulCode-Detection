def bulk_scan(securedrops: 'DirectoryEntryQuerySet') ->None:...
"""docstring"""
securedrops = securedrops.with_domain_annotation()
domains = securedrops.values_list('domain', flat=True)
results = inspect_domains(domains, {'timeout': 10})
results_to_be_written = []
for result_data in results:
securedrop = securedrops.get(domain=result_data['Domain'])
return ScanResult.objects.bulk_create(results_to_be_written)
current_result = pshtt_data_to_result(securedrop, result_data)
current_result.compute_grade()
current_result.securedrop = securedrop
prior_result = securedrop.results.latest()
results_to_be_written.append(current_result)
if prior_result.is_equal_to(current_result):
prior_result.result_last_seen = timezone.now()
results_to_be_written.append(current_result)
prior_result.save()
