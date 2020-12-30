# coding=utf-8
from __future__ import absolute_import, unicode_literals

import octoprint.plugin
import RPi.GPIO as GPIO


import os


class OctoBuddyPlugin(octoprint.plugin.StartupPlugin, octoprint.plugin.ShutdownPlugin):

    def on_after_startup(self):
        self._logger.info("OctoBuddy Alive Now!")
        self._logger.info(buttonpressed)
        self._logger.info(self._printer.get_state_id())
        self._logger.info(GPIO.RPI_INFO)
        self._setup_sensor()
        self.setup_GPIO();

    def on_shutdown(self):
        GPIO.cleanup();
        self._logger.info("OctoBuddy Going to Bed Now!")
        self._logger.info("Test")

    def button_callback(self):
        self._logger.info("test")
        self._logger.info("and I have to type this again")

    def setup_GPIO(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(22, GPIO.RISING, callback=self.button_callback(self), bouncetime = 400)




__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = OctoBuddyPlugin()
