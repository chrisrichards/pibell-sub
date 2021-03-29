# pibell-sub

This is part of an over engineered doorbell project. The range of the off the shelf wireless doorbell I bought didn't quite stretch to my office in the shed at the bottom of the garden, so this project was born!

This is the subscriber part of the system, that subscribes to the 'home/doorbell/state' mqtt topic and sound an alarm when pressed.

It comprises a RaspberryPi with a [pibrella](http://pibrella.com) hat installed. When the 'home/doorbell/state' mqtt topic is received with the 'pressed' payload, a buzzer is sounded and LEDs lit.

Deployed to a RaspberryPi via [balena.io](https://www.balena.io).