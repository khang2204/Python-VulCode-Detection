def random_string():...
"""docstring"""
numpy_state = np.random.get_state()
np.random.seed(None)
random_id = np.random.bytes(ray_constants.ID_SIZE)
np.random.set_state(numpy_state)
return random_id
