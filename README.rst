Introduction
============



.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord


.. image:: https://github.com/tylercrumpton/CircuitPython_GC9D01/workflows/Build%20CI/badge.svg
    :target: https://github.com/tylercrumpton/CircuitPython_GC9D01/actions
    :alt: Build Status


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

displayio driver for GC9D01 TFT LCD displays


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_
or individual libraries can be installed using
`circup <https://github.com/adafruit/circup>`_.

Installing from PyPI
=====================
.. note:: This library is not available on PyPI yet. Install documentation is included
   as a standard element. Stay tuned for PyPI availability!

.. todo:: Remove the above note if PyPI version is/will be available at time of release.

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/circuitpython-gc9d01/>`_.
To install for current user:

.. code-block:: shell

    pip3 install circuitpython-gc9d01

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install circuitpython-gc9d01

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .venv
    source .env/bin/activate
    pip3 install circuitpython-gc9d01

Installing to a Connected CircuitPython Device with Circup
==========================================================

Make sure that you have ``circup`` installed in your Python environment.
Install it with the following command if necessary:

.. code-block:: shell

    pip3 install circup

With ``circup`` installed and your CircuitPython device connected use the
following command to install:

.. code-block:: shell

    circup install gc9d01

Or the following command to update an existing version:

.. code-block:: shell

    circup update

Usage Example
=============

.. code-block:: python

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

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/tylercrumpton/CircuitPython_GC9D01/blob/HEAD/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
