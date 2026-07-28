def get_cuda_visible_devices():...
"""docstring"""
gpu_ids_str = os.environ.get('CUDA_VISIBLE_DEVICES', None)
if gpu_ids_str is None:
return None
if gpu_ids_str == '':
return []
return [int(i) for i in gpu_ids_str.split(',')]
