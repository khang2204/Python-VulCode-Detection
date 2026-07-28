def test_bw2_disclosure():...
de = DisclosureExporter(TEST_BW_PROJECT_NAME, TEST_BW_DB_NAME, folder_path=
    TEST_FOLDER, filename=TEST_FILENAME)
disclosure_file = de.write_json()
print(disclosure_file)
assert os.path.isfile(disclosure_file)
