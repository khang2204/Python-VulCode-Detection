def _GetNumbersOfDataPointGroups(data_points):...
build_level_number = 0
revision_level_number = 0
for data_point in data_points:
if data_point.try_job_url:
return build_level_number, revision_level_number
revision_level_number += 1
build_level_number += 1
