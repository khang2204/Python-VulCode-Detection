def __init__(self):...
print('Creating TensorflowProcessor object')
print('Loading ball detection tflite model')
self.ball_detector_interpreter = interpreter_wrapper.Interpreter(model_path
    =TensorflowProcessor.ball_detector_model_path)
self.ball_detector_interpreter.allocate_tensors()
self.ball_detector_input_details = (self.ball_detector_interpreter.
    get_input_details())
self.ball_detector_output_details = (self.ball_detector_interpreter.
    get_output_details())
print('Loading corner detection tflite model')
self.corner_detector_interpreter = interpreter_wrapper.Interpreter(model_path
    =TensorflowProcessor.corner_detector_model_path)
self.corner_detector_interpreter.allocate_tensors()
self.corner_detector_input_details = (self.corner_detector_interpreter.
    get_input_details())
self.corner_detector_output_details = (self.corner_detector_interpreter.
    get_output_details())
print('TensorflowProcessor object created')
