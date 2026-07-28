@app.route(...
app.logger.debug('moving sequence item {}: direction: {}'.format(
    sequence_item_id, json['direction']))
index = [index for index, item in enumerate(sequence.sequence_items) if 
    item.id == sequence_item_id]
if not index:
index = index[0]
new_index = index - 1 if json['direction'] == 'up' else index + 1
if new_index >= 0 and new_index < len(sequence.sequence_items):
sequence.sequence_items.insert(new_index, sequence.sequence_items.pop(index))
return sequence.to_map()
