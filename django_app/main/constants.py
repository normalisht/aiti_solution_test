from django.conf import settings
import cv2 as cv

TEXT: str = 'Default Text'
FRAME_WIDTH: int = 100
FRAME_HEIGHT: int = 100
FPS: int = 30
DURATION: int = 3
BACKGROUND_COLOR: tuple[int] = (91, 217, 192)
FONT: int = cv.FONT_HERSHEY_COMPLEX
FONT_SCALE: int = 3
FONT_THICKNESS: int = 6
FONT_COLOR: tuple[int] = (111, 26, 9)
FILE_PATH: str = settings.MEDIA_ROOT
FILE_NAME: str = 'result'
