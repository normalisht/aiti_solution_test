import argparse
import os

import cv2 as cv
import numpy as np


def parse_args():
    parser = argparse.ArgumentParser(
        description='Создание видео с бегущей строкой.'
    )
    parser.add_argument(
        '--text',
        type=str,
        default='Default Text',
        help='Текст для бегущей строки',
    )
    return parser.parse_args()


def create_video(
    text: str = 'Default Text',
    frame_width: int = 100,
    frame_height: int = 100,
    fps: int = 30,
    duration: int = 3,
    background_color: tuple[int] = (91, 217, 192),
    font: int = cv.FONT_HERSHEY_COMPLEX,
    font_scale: int = 3,
    font_thickness: int = 6,
    font_color: tuple[int] = (111, 26, 9),
    file_path: str = './media/',
    file_name: str = 'result',
) -> None:
    num_frames = fps * duration
    text_size = cv.getTextSize(text, font, font_scale, font_thickness)[0]

    x_pos = frame_width
    x_pos_float = x_pos
    y_pos = frame_height // 2 + text_size[1] // 2
    one_frame_shift = (frame_width + text_size[0]) / num_frames

    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    output = cv.VideoWriter(
        os.path.join(file_path, f'{file_name}.mp4'),
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


if __name__ == '__main__':
    args = parse_args()
    create_video(args.text)
