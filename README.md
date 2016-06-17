# raspberry-pi-dynamic-leds-blinking
A Python script that allows you to blink LED lights using your Raspberry Pi's GPIO pins

## Build the circut layout
Connect your LED light(s) to your pi. The below circut layout is just an example, but you can add/remove LED lights.
![Screenshot](http://mohammed-radwan.com/uploads/led%203x.jpg?id=1)

## Usage
Once the circut is complete, open the script and adjust the code before running it.

You need to set the correct GPIO pins in the line below
```python
#Registring GPIO pins 11, 12, and 13
connected_gpio_pins = [11, 12, 13]
```

You can also adjust the blinking interval
```python
#Setting up blinking interval
interval = 0.3
```

Finally start the program
```python
#Running the program
blink(connected_gpio_pins, interval)
```

You can play around with pins registration by registring the same pin more than once to have an unordered LED lights
```python
connected_gpio_pins = [11, 11, 13, 12, 11, 13, 13, 12]
```

License & Author
-----------------
- Author:: Mohammed Radwan (<http://mohammed-radwan.com>)

```text
The MIT License (MIT)

Copyright (c) 2016 Mohammed Radwan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
