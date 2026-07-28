def test_attributes():...
de = DisclosureExporter(TEST_BW_PROJECT_NAME, TEST_BW_DB_NAME, folder_path=
    TEST_FOLDER, filename=TEST_FILENAME)
assert de.foreground_flows
assert de.background_flows
assert de.emission_flows
assert de.Af
assert de.Ad
assert de.Bf
assert de.cutoffs
