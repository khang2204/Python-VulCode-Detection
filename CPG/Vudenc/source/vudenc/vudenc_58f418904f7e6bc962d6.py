@app.route('/api/sequences/<id>/sequence_items', methods=['POST'])...
new_sequence_item = SequenceItem(json)
app.logger.debug('adding sequence item {} to id {}'.format(
    new_sequence_item, id))
sequence.sequence_items.append(new_sequence_item)
return new_sequence_item.to_map()
