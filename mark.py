import argparse
from watermark import Watermark

parser = argparse.ArgumentParser(description='Script used to add watermark and reverse the process.')
parser.add_argument('--image', '-i', help='Path to the input image.', default='sample/sample_image.png')
parser.add_argument('--text', '-t', help='Text for watermark.', default='Monkey D Luffy')
process_type = parser.add_mutually_exclusive_group(required=False)
process_type.add_argument('--add', dest='add_watermark', action='store_true')
process_type.add_argument('--remove', dest='add_watermark', action='store_false')
parser.set_defaults(add_watermark=True)

args = parser.parse_args()

# Default parameters for Watermark class are:
#     text='Sample watermark'
#     alpha=0.3
#     color=(0, 0, 255)
#     path_to_save='./result'

watermark = Watermark(text=args.text)
if args.add_watermark:
    watermarked_image = watermark.add_watermark(args.image)
else:
    un_watermarked_image = watermark.remove_watermark(args.image)
