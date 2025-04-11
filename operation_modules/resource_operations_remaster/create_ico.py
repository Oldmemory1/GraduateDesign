import hashlib
import os
import time

import random

from PIL import Image
def create_ico(source_folder,destination_folder):
    file_list = os.listdir(destination_folder)
    for file_name in file_list:
        os.remove(os.path.join(destination_folder, file_name))

    for filename in os.listdir(source_folder):
        if filename.endswith('.ico'):
            with Image.open(os.path.join(source_folder, filename)) as image:

                try:
                    random_width = random.randint(10, 100)
                    random_height = random.randint(10, 100)
                    resized_image = image.resize((random_width, random_height))
                    pixel_data = list(resized_image.getdata())
                    modified_pixel_data = [(r + random.randint(-11, 11), g + random.randint(-11, 11), b + random.randint(-11, 11), a) for (r, g, b, a) in pixel_data]
                    modified_image = Image.new(resized_image.mode, resized_image.size)
                    modified_image.putdata(modified_pixel_data)
                    new_created_date = str(random.randint(0, int(time.time())))
                    file_stats = os.stat(os.path.join(source_folder, filename))
                    os.utime(os.path.join(source_folder, filename), (file_stats.st_atime, int(new_created_date)))
                    hash_value = hashlib.md5(str(random.random()).encode()).hexdigest()
                    new_filename = os.path.join(destination_folder, f"{hash_value}.ico")
                    modified_image.save(new_filename)
                except:
                    pass
if __name__ == '__main__':
    create_ico(source_folder="./source_data",destination_folder="./destination_data")