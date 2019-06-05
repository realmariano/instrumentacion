arduino-qt-continuous
=====================

This example shows:
- how to build an instrument that communicates via
exchanging text messages using arduino and lantz.
- how to query that instrument periodically
- how to plot the results in a chart


Requirements
------------

- Install the latest version of lantz

- Install arduino-cli
  https://github.com/arduino/arduino-cli

  _windows:_ 
  Make sure you included the arduino-cli in your enviroment variables PATH.
  From the command prompt:
   * Check your installation by doing `arduino-cli`
   * Install the AVR dependencies `arduino-cli core install arduino:avr`


- (optionally) Install pyqtgraph if you want to run the run_plot example
  
- Copy all the content of this folder to your computer

If you do not have the NI-VISA installed, you need to install `pyvisa-py`
(the pure python backend for pyvisa) and tell lantz to use it by default

In the command line:

    pip install pyvisa-py
    pip install pyserial
    lantz config core.visa_backend '@py'


Step 1: Create arduino sketch template
--------------------------------------

In the console, go to the folder containing this project and execute the following
command:

    lantz ino new drivers:TemperatureSensor
    
This will generate a arduino sketch template for the class `TemperatureSensor`
located in the `run` module. You will find it in the TemperatureSensor folder.
It additionally creates a "packfile" named `TemperatureSensor.pack.yaml` that
contains information to compile and upload the project.


Step 2 (optional): Add your own code to the arduino sketch
----------------------------------------------------------

You can customize the arduino code by editing `inodriver_user.cpp` and 
`inodriver_user.h` within the sketch folder. 

You will find the following functions:

- user_setup: this will be executed during the setup of the arduino just before starting
  the communication with the serial command.
  
- user_loop: this will be executed every time the main loop is executed

- ... and one function for each getter/setter you have in your lantz code.

You can just use the default code to get working but dummy example.


Step 3: Run it
--------------
 
In the console, go to the folder containing this project and execute the following
command:

    python run_display.py

If you get a __json error__ read carfully the notes it states you should update the index using `arduino-cli core-update index`
    
    
Step 4 (optional): Change something in the arduino sketch
---------------------------------------------------------

Edit `inodriver_user.cpp`, for example to return 42.0 from `get_TEMP`
and run the code again. Notice that lanz recompiles and upload the sketch!


Step 5 (optional): Run the plotting example
-------------------------------------------

In the console, go to the folder containing this project and execute the following
command:

    python run_plot.py
