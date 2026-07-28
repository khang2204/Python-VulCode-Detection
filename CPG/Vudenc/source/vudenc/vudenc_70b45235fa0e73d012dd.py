def QuantizeModel(model_path, output_file_name):...
print('Quantizing model')
converter = tf.contrib.lite.TocoConverter.from_saved_model(model_path)
converter.post_training_quantize = True
quant_model = converter.convert()
open(output_file_name + '.tflite', 'wb').write(quant_model)
