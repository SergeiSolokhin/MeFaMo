import mefamo
from argparse import ArgumentParser
import importlib

importlib.reload(mefamo)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--input', default='0',
                        help='Video source. Can be an integer for webcam or a string for a video file.')
    parser.add_argument('--width', default=1080,
                        help='Video source width')
    parser.add_argument('--height', default=1920,
                        help='Video source height')
    parser.add_argument('--ip', default='127.0.0.1',
                        help='IP address of the Unreal LiveLink server.')
    parser.add_argument('--port', default=11111,
                        help='Port of the Unreal LiveLink server.')
    parser.add_argument('--show_3d', action='store_true',
                        help='Show the 3d face image (projected into a 2d window')
    parser.add_argument('--hide_image', action='store_true',
                        help='Hide the image window.')
    parser.add_argument('--show_debug', action='store_true',
                        help='Show debug window.')
    args = parser.parse_args()

    print("Starting MeFaMo")
    mediapipe_face = mefamo.Mefamo(args.input, args.width, args.height, args.ip, args.port, args.show_3d, args.hide_image, args.show_debug)
    mediapipe_face.start()