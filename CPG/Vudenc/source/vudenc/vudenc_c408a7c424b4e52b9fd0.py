def add_image_args(self, image_mode):...
"""docstring"""
parlai = self.add_argument_group('ParlAI Image Preprocessing Arguments')
parlai.add_argument('--image-size', type=int, default=256, help=
    'resizing dimension for images')
parlai.add_argument('--image-cropsize', type=int, default=224, help=
    'crop dimension for images')
