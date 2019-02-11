import mouse

from bot_utils.image_template_matching import get_matches_from_screen
from bot_utils.exceptions import TemplateImageNotFound


def click(img_path, double_click=False):
    regions = get_matches_from_screen(img_path, threshold=0.95, write_output_image=True)
    print(regions)
    if not regions:
        raise TemplateImageNotFound('template image not found: {}'.format(img_path))

    region = regions[0]
    x = (region[0] + region[2]) / 2
    y = (region[1] + region[3]) / 2

    mouse.move(x, y, duration=0.3)
    if double_click:
        mouse.double_click()
    else:
        mouse.click()


def double_click(img_path):
    click(img_path, True)
