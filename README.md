# Solar Water Bot Raspberry Pi Automatic Plant Watering System
Solar Water Bot is a solar powered plant watering system built with a Raspberry Pi, sensors, motor, pump and Python code. This was created for my sons 6th grade science project.

#### Click To Watch Demo Video (opens new window to YouTube)
<a href="https://youtu.be/-uzUE10D6S4" target="_blank"><img src="https://img.youtube.com/vi/-uzUE10D6S4/0.jpg" 
alt="Raspberry Pi Plan Watering System" style="max-width:550px" border="10" /></a>

## Open Top Of Tub When It Rains
This is Python code that will trigger the motor to turn on when the rain sensor detects rain. The motor will open the top of the tub so rain can be captured in the tub. The code also detects when the rain sensor is dry and will trigger the motor to spin the opposite way to close the top of the tub. This assures the water does not get polluted with outside elements when it is not raining. [Download Rain Sensor Code](RainSensor.py)

Note: this is the main script you want to call to run the rain sensor code. This script also imports [motor_function.py](motor_function.py) which controls the motor so you will need to download both files for the rain sensor to work.

## Turn On Water Pump When Soil Is Dry
This is Python code that will trigger the water pump to turn on when the soil sensor is dry. The pump will turn on pulling water from the tub through water lines up to the plants. The code also detects when the soil sensor is wet and will trigger the pump to turn off. This assures the plants are only watered when the plant soild is dry and not overwatered when the soil is wet. [Download Soil Sensor Code](SoilSensor.py)

### Other Python Files
We also included files [PumpBack.py](PumpBack.py) and [PumpForward.py](PumpBack.py). We used these when we were testing the pump. The pump forward code pulls the water from the tub forward to the plans. The pump back code pulls the water back into the tubs. This is useful if you want to empty out your water lines.

#### Check out videos and more details about this project from [SolarWaterBot.com](SolarWaterBot.com)





