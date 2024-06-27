# Генерация видео с бегущей строкой

## Запуск проекта

```bash
cd infra
```

```bash
docker compose up --build -d
```

## Endpoints

```http request
GET /create_video/?text=some_text
```

Параметры

* text - текст бегущей строки (256 символов максимум)
* frame_width - ширина видео
* frame_height - высота видео
* fps - кол-во кадров в секунду
* duration - продолжительность видео
* font - шрифт (см. opencv docs)
* font_scale - масштаб шрифта
* font_thickness - толщина шрифта
* font_color - цвет текста (RGB). Например, font_color=255,255,255
* background_color - цвет фона (RGB). Например, background_color=0,0,0

[opencv docs](https://github.com/opencv/opencv-python)


Доступ к файлу есть по полному имени файлу с расширением
```http request
GET /media/{file_name}
```
