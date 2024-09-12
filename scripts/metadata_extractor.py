from PIL import Image
from PIL.ExifTags import TAGS
import sys

def extract_metadata(image_path):
    try:
        # Open the image file
        img = Image.open(image_path)
        
        # Extract EXIF data
        exif_data = img._getexif()

        if not exif_data:
            print(f"No EXIF metadata found in {image_path}")
            return

        # Dictionary to store readable tag names and values
        metadata = {}

        # Iterate through the EXIF data and extract tag names and values
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)
            metadata[tag_name] = value

        # Display the metadata
        print(f"Metadata for {image_path}:")
        for tag_name, value in metadata.items():
            print(f"{tag_name}: {value}")

        return metadata

    except Exception as e:
        print(f"Error extracting metadata: {str(e)}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python metadata_extractor.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    extract_metadata(image_path)
