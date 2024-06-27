import os

import cv2 as cv
import numpy as np
import main.constants as constants


def create_video(
    text: str = constants.TEXT,
    frame_width: int = constants.FRAME_WIDTH,
    frame_height: int = constants.FRAME_HEIGHT,
    fps: int = constants.FPS,
    duration: int = constants.DURATION,
    background_color: tuple[int] = constants.BACKGROUND_COLOR,
    font: int = constants.FONT,
    font_scale: int = constants.FONT_SCALE,
    font_thickness: int = constants.FONT_THICKNESS,
    font_color: tuple[int] = constants.FONT_COLOR,
    file_path: str = constants.FILE_PATH,
    file_name: str = constants.FILE_NAME,
) -> dict[str, int]:
    file_extension = 'mp4'

    num_frames = fps * duration
    text_size = cv.getTextSize(text, font, font_scale, font_thickness)[0]

    x_pos = frame_width
    x_pos_float = x_pos
    y_pos = frame_height // 2 + text_size[1] // 2
    one_frame_shift = (frame_width + text_size[0]) / num_frames

    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    output = cv.VideoWriter(
        os.path.join(file_path, f'{file_name}.{file_extension}'),
        fourcc,
        fps,
        (frame_width, frame_height),
    )

    for i in range(num_frames):
        frame = np.full(
            (frame_height, frame_width, 3), background_color, dtype=np.uint8
        )
        x_pos_float -= one_frame_shift
        x_pos = int(x_pos_float)

        cv.putText(
            frame,
            text,
            (x_pos, y_pos),
            font,
            font_scale,
            font_color,
            font_thickness,
            cv.LINE_AA,
        )
        output.write(frame)

    output.release()
    cv.destroyAllWindows()

    return {
        'text': text,
        'frame_width': frame_width,
        'frame_height': frame_height,
        'fps': fps,
        'duration': duration,
        'background_color': background_color,
        'font': font,
        'font_scale': font_scale,
        'font_thickness': font_thickness,
        'font_color': font_color,
        'file_path': file_path,
        'file_name': file_name,
        'file_extension': file_extension,
    }
