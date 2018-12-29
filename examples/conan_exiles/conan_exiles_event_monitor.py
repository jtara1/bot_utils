import pyautogui
import keyboard
import time
import os
import discord
try:
    from misc_scripts.image_to_text import image_to_text
except ModuleNotFoundError:
    from image_to_text import image_to_text

try:
    from misc_scripts.conan_exiles_event_monitor_secrets import token
except ModuleNotFoundError:
    from conan_exiles_event_monitor_secrets import token


class CE:
    def __init__(self, polling_period=5, toggle_pause_hotkey='ctrl+q'):
        self.pause_execution = False
        self.polling_period = polling_period
        self.previous_text = ''
        self.discord_bot = DiscordBot()

        keyboard.add_hotkey(toggle_pause_hotkey, self.toggle_pause)

    def toggle_pause(self):
        self.pause_execution = not self.pause_execution

    def start(self):
        while not self.pause_execution:
            time.sleep(self.polling_period)
            self.show_event_log()

            text = self.take_ss_and_apply_ocr()
            if self.text_changed(text):
                self.discord_bot.send_message('WE GOT RAIDED?\n{}'.format(text))

    def show_event_log(self):
        pyautogui.press('esc')
        pyautogui.click(780, 495)
        pyautogui.click(1, 1)

    def take_ss_and_apply_ocr(self):
        # take a screenshot, apply ocr
        region_1080p = (425, 285, 1075, 660)
        im = pyautogui.screenshot(region=region_1080p)

        image_path = os.path.join(os.getcwd(), 'ce.png')
        im.save(image_path)
        text = image_to_text(image_path)
        print('-' * 50)
        return text

    def text_changed(self, new_text):
        if self.previous_text == '':
            self.previous_text = new_text
        elif self.previous_text != new_text:
            return True
        return False


class DiscordBot:
    def __init__(self):
        self.client = discord.Client()
        self.client.run(token)

    async def send_message(self, message):
        await self.client.send_message(
            discord.Object(472843669649489921),
            message
        )


if __name__ == '__main__':
    ce = CE()
    ce.start()
    # ce.discord_bot.client.close()
