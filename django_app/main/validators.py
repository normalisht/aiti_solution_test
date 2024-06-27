from django.core.exceptions import FieldError


def validate_video_parameters(data):
    data = dict(data)

    integer_fields = [
        ('frame_width', 1920),
        ('frame_height', 1080),
        ('fps', 120),
        ('duration', 60),
        ('font', 16),
        ('font_scale', 1000),
        ('font_thickness', 1000),
    ]
    rgb_fields = ['background_color', 'font_color']

    for field, max_value in integer_fields:
        try:
            if el := data.get(field):
                el = int(el[0])
                if el > max_value:
                    raise ValueError
                data[field] = el
        except (ValueError, TypeError):
            raise FieldError(
                f'`{field}` must be an integer and less than {max_value}'
            )

    for field in rgb_fields:
        try:
            if values := data.get(field):
                values = tuple(map(int, values[0].split(',')))
                if len(values) != 3:
                    raise ValueError
                for value in values:
                    if not (0 <= int(value) <= 255):
                        raise ValueError
                data[field] = values
        except Exception:
            raise FieldError(f'`{field}` must be an RGB tuple')

    text = data.get('text')
    if not text or len(text[0]) > 256:
        raise FieldError(
            '`text` is required and must be less than 256 characters'
        )
    data['text'] = text[0]

    return data
