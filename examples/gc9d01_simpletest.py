# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Tyler Crumpton
#
# SPDX-License-Identifier: Unlicense

import board
import displayio
from gc9d01 import GC9D01

spi = board.SPI()
while not spi.try_lock():
    pass
spi.configure(baudrate=24000000)  # Configure SPI for 24MHz
spi.unlock()
cs = board.D10
dc = board.D13
reset = board.D11

displayio.release_displays()
display_bus = displayio.FourWire(spi, command=dc, chip_select=cs, reset=reset)

display = GC9D01(
    display_bus, width=160, height=40, rotation=90, backlight_pin=board.IO16
)

# Make the display context
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(160, 40, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x03C2FC

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

while True:
    pass
