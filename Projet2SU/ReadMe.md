If you can, it’s better to read the pdf file to understand the functioning of the project better. 
This project is implemented on a linux based os. 
Install Flask and its dependencies for the website version
For the flask version :  run these commands or simply add them to .bashrc to change the default file that will run the server, you'll probably need root rights. 
This is mentioned in the installation manual of flask, check it out for more details and to know if you need to do it or not according to your case (especially if you’re working with a different OS).

export FLASK_APP="ABSOLUTE_PATH_TO_WebServer_FILE"
export FLASK_ENV=development

Before running the FlaskServer make sure your arduino is connected to the right USB port (check ls /de/tty*), you can either change the USB port on the code of the server or configure the port of the arduino to be USB0. 

You can run the flask server with the options you desire but the scrypt runWebserver.sh should make it possible to access the web page from any device connected to the same local network, you just need to know the IP address of your raspberry pi. Read the file to see the command and you can check out the flask documentation to understand more. 

If you want to modify the front of the webpage, it would be better to implement it from scratch because it was only implemented for test purposes and it's a complete mess XD (you'll have to modify the back too in some cases, it depends on what changes you make in the front)

If you want to work with grbl and UGcodeSender : add grbl to arduino IDE and upload it to the arduino  and install UniversalGcodeSender to send Gcode to the arduino (checkout the grbl github for more details). Of course you’ll need to plug the CNC shield (with its driver(s) ) to the arduino.

For the circuit with just the drivers and in order to protect the different parts of the circuit, use the potentiometer of the driver and a to set up  the current limit. (google it).

You don't need to do anything special for protection with  the CNC apart from using a power supply according to its properties. (it normally accepte a 12-36v ~2A power). 

