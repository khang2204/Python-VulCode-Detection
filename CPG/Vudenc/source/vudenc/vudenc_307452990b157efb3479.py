def build_file_aliases():...
return BuildFileAliases(targets={PythonApp.alias(): PythonApp, PythonBinary
    .alias(): PythonBinary, PythonLibrary.alias(): PythonLibrary,
    PythonTests.alias(): PythonTests, PythonDistribution.alias():
    PythonDistribution, 'python_requirement_library':
    PythonRequirementLibrary, Resources.alias(): Resources, UnpackedWheels.
    alias(): UnpackedWheels}, objects={'python_requirement':
    PythonRequirement, 'python_artifact': PythonArtifact, 'setup_py':
    PythonArtifact}, context_aware_object_factories={'python_requirements':
    PythonRequirements, PantsRequirement.alias: PantsRequirement})
