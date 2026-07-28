@app.route(...
app.logger.debug('duplicate item {}'.format(sequence_item_id))
sequence_item = sequence.item(sequence_item_id)
sequence.sequence_items.append(sequence_item.duplicate())
return sequence.to_map()
