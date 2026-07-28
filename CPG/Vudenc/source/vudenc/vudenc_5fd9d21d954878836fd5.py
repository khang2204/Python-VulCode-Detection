def _make_flat_wins_csv_stream(self, win_data_generator):...
stringio = Echo()
yield stringio.write(u'\ufeff')
first = next(win_data_generator)
csv_writer = csv.DictWriter(stringio, first.keys())
header = dict(zip(first.keys(), first.keys()))
yield csv_writer.writerow(header)
yield csv_writer.writerow(first)
for win_data in win_data_generator:
yield csv_writer.writerow(win_data)
