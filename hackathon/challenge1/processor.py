from PIL import Image

class ImageAssembler:
    def __init__(self, fragments):
        self.fragments = fragments
        self.images = []
        self.assembled_image = None

    def load_images(self):
        """
        Load all images from the fragment paths.
        """
        for f in self.fragments:
            img = Image.open(f)
            if len(self.images) > 0:
                self.images.append(img)

    def assemble_image(self, grid_size):
        self.load_images()

        width, height = self.images[0].size

        self.assembled_image = Image.new('RGB', (width * grid_size[0], height * grid_size[1]))

        positions = []

        for row in range(grid_size[0]):
            for col in range(grid_size[1]):
                positions.append((col * height, row * width))

        for i, pos in enumerate(positions):
            self.assembled_image.paste(self.images[i], pos)

    def save(self, path):
        self.assembled_image_path.save(path, 'JPG')
