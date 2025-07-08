import os
import shutil

def copy_images():
    # Create output/images directory if it doesn't exist
    os.makedirs('output/images', exist_ok=True)
    
    # List of images to copy
    images_to_copy = [
        'hero-bg.png',
        '_smallbusiness.png',
        '_podcast.png',
        '_invideo.png',
        'aipowered-visuals-nobg.png',
        'ai_powered_writing.png',
        'ai_power_video.png'
    ]
    
    # Copy each image if it exists
    for image in images_to_copy:
        src = os.path.join('backup/images', image)
        dst = os.path.join('output/images', image)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"Copied {image}")
        else:
            print(f"Warning: {image} not found in source directory")

if __name__ == '__main__':
    copy_images() 