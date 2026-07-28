@app.route('/api/sequences/<sequence_id>/sequence_items/<sequence_item_id>',...
sequence_item = sequence.item(sequence_item_id)
sequence_item = sequence_item.to_map()
sequence_item.update({'status': 'deleted'})
sequence.sequence_items = [x for x in sequence.sequence_items if x.id !=
    sequence_item_id]
return sequence_item
