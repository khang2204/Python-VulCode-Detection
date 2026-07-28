def verify(data, expected):...
print('Expected: ', expected)
actual = [{'name': doc['name_info']['name']} for doc in data['names']]
print('Actual: ', actual)
assert_that(len(actual), equal_to(len(expected)))
for i in range(len(actual)):
assert_that(actual[i]['name'], equal_to(expected[i]['name']))
