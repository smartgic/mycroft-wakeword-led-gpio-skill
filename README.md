
[![Build Status](https://travis-ci.com/smartgic/mycroft-wakeword-led-gpio-skill.svg?branch=20.8.1)](https://travis-ci.com/github/smartgic/mycroft-wakeword-led-gpio-skill) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![contributions welcome](https://img.shields.io/badge/contributions-welcome-pink.svg?style=flat)](https://github.com/smartgic/mycroft-wakeword-led-gpio-skill//pulls) [![Skill: MIT](https://img.shields.io/badge/mycroft.ai-skill-blue)](https://mycroft.ai) [![Discord](https://img.shields.io/discord/809074036733902888)](https://discord.gg/Vu7Wmd9j) 


# <img src="docs/raspberry-pi.png" card_color="#0000" width="50" height="60" style="vertical-align:bottom"/> Wake Word GPIO LED

A light _(LED)_ indicator for Mycroft on Raspberry Pi.

## About

The [Raspberry Pi](https://rapsberrypi.org) is a tiny and affordable computer that you can use to interact with `GPIO` _(General Purpose Input/Output)_ such as button, sensor, LED, etc...

This skill interacts with a LED connected to a GPIO to let you know if Mycroft is listening. When a wake word is detected the LED is turning on and when the recording is done the LED is turning off.

## Examples

There is no example because there is no interaction with the Mycroft.

## Installation

Make sure to be within the Mycroft `virtualenv` before running the `msm` command.

```
$ . mycroft-core/venv-activate.sh
$ msm install https://github.com/smartgic/mycroft-wakeword-led-gpio-skill.git
```

## Configuration

This skill utilizes the `settings.json` file which allows you to configure this skill via `home.mycroft.ai` after a few seconds of having the skill installed you should see something like below in the https://home.mycroft.ai/#/skill location:

<img src='docs/wakeword-led-gpio-config.png' width='450'/>

Fill this out with your appropriate information and hit save.

## Credits

Smart'Gic

## Category

**IoT**

## Tags

#wakeword
#raspberrypi
#led
#gpio
#smarthome
#picroft
