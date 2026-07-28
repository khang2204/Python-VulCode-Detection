@app.route('/api/sequences/<sequence_id>/sequence_items/<sequence_item_id>',...
app.logger.debug('modifying sequence item {} from sequence'.format(
    sequence_item_id, sequence_id))
new_sequence_item = SequenceItem(json)
sequence.sequence_items = [(new_sequence_item if x.id == sequence_item_id else
    x) for x in sequence.sequence_items]
return new_sequence_item.to_map()
