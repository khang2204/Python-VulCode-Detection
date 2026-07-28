def test_bw2_import():...
bw2.projects.set_current(IMPORT_PROJECT_NAME)
di = DisclosureImporter(os.path.join(os.path.dirname(os.path.realpath(
    __file__)), TEST_FOLDER, '{}.json'.format(TEST_FILENAME)))
di.apply_strategies()
assert di.statistics()[2] == 0
di.write_database()
assert len(bw2.Database(di.db_name)) != 0
