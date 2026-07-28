@app.route('/api/sequences/<id>', methods=['DELETE'])...
sequence = controller.sequences.lookup(id)
sequence_json = sequence.to_map()
sequence_json.update({'status': 'deleted'})
controller.sequences.remove(sequence)
return sequence_json
