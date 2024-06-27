from uuid import uuid4

from django.conf import settings
from django.http import FileResponse

from .utils import create_video
from .validators import validate_video_parameters
import main.constants as constants
from .models import VideoData


def create_video_view(request):
    file_name = uuid4().hex[: settings.SHORT_UUID_LENGTH]
    data = validate_video_parameters(request.GET)

    video_params = create_video(
        text=data.get('text', constants.TEXT),
        frame_width=data.get('frame_width', constants.FRAME_WIDTH),
        frame_height=data.get('frame_height', constants.FRAME_HEIGHT),
        fps=data.get('fps', constants.FPS),
        duration=data.get('duration', constants.DURATION),
        background_color=data.get(
            'background_color', constants.BACKGROUND_COLOR
        ),
        font=data.get('font', constants.FONT),
        font_scale=data.get('font_scale', constants.FONT_SCALE),
        font_thickness=data.get('font_thickness', constants.FONT_THICKNESS),
        font_color=data.get('font_color', constants.FONT_COLOR),
        file_name=file_name,
    )
    video_data_obj = VideoData.objects.create(**video_params)

    file = open(video_data_obj.file, 'rb')
    return FileResponse(file, as_attachment=True, content_type='video/mp4')
