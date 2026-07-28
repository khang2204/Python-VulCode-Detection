def validate_row(self, input_row):...
length_exceeded = [data for data in input_row if len(data) > max_data_length]
if length_exceeded:
return False, length_exceeded
return True, []
