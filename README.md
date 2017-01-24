TinyArcade weather display
====================================

Author: Pablo Jiménez Mateo

![ScreenShot](https://raw.githubusercontent.com/pjimenezmateo/tinyarcade-weather-display/master/preview.gif)

I love my [TinyArcade](https://tinycircuits.com/collections/kits/products/tinyarcade) but I wanted some use of it when I was not playing with it.

So I made a small program that sends the current weather of your city and displays it on its screen! :D

Requirements
--------------

* Python
* Arduino IDE
* A USB to MicroUSB cable
* A TinyArcade
* The [Time](https://github.com/PaulStoffregen/Time) library

Setup
-------------

### Setup your TinyArcade

- Follow [this](https://tinycircuits.com/blogs/learn/158833543-tinyscreen-setup) instructions to setup the TinyScreen

- Connect your TinyArcade to with the USB cable to your computer, turn it off and then turn it on while pressing both buttons at the same time

    - If done correctly the text "TinyArcade Bootloader Mode" should be displayed

- Copy the file font.h in the Arduino library TinyScreen ([how to locate the library](https://www.arduino.cc/en/Guide/Libraries) tl;dr; in /home/user/Arduino/libraries or My Documents/Arduino/libraries) it will overwrite a file inside, this version adds the '-' symbol to the liberationSans_22ptFontInfo font used to display negative temperature values

- Load the weather.ino project and upload it into your TinyArcade

    - Under Tools, make sure the board is TinyScreen+, the Build Option is TinyArcade Menu, you have selected the right port and the Programmer is AVRISP mkll

### Setup your server/computer

- Download the [Time](https://github.com/PaulStoffregen/Time) library on your library folder

- You need the Where On Earth Identifier to know the weather of which city to display. To find the WOEID of your city (or the city you want the weather information of) go to [http://woeid.rosselliot.co.nz/lookup](http://woeid.rosselliot.co.nz/lookup) and search for your city, it will give you a numeric code

- Open the server.py file with a text editor (use something like notepad, not Word), you will need to edit the 6th line to match your WOEID

- Then, making sure your TinyArcade is connected to your PC, just run the server.py file


This program is licensed under Creative commons Attribution 3.0 Unported, more info : 
http://creativecommons.org/licenses/by/3.0/deed.en_US