def getBallPosition(self, image):...
image = np.float32(image)
image /= 255.0
image = np.expand_dims(image, axis=0)
image = np.expand_dims(image, axis=3)
self.ball_detector_interpreter.set_tensor(self.ball_detector_input_details[
    0]['index'], image)
self.ball_detector_interpreter.invoke()
return np.squeeze(self.ball_detector_interpreter.get_tensor(self.
    ball_detector_output_details[0]['index']))
