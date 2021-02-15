from flask import Flask, render_template, request, jsonify
USB_PORT1 = "/dev/ttyUSB0"
import serial
import time
import random
app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def template_test():
    try:
        usb = serial.Serial(USB_PORT1, 9600, timeout=2)
    except:
        print("ERROR - Could not open USB serial port.  Please check your port name and permissions.")
         #print("Exiting program.")
         #exit()
        return render_template('error.html')
        
                 
    if request.method == 'POST':
             
             if request.form.get('leftbtn') == 'leftbtn':
                # pass
                print("left");
             elif  request.form.get('rightbtn') == 'rightbtn':
                # pass # do something else
                print("right")
             elif  request.form.get('upbtn') == 'upbtn':
                # pass # do something else
                usb.write(b'yu')
                print("Yup")
             elif  request.form.get('downbtn') == 'downbtn':
                # send 
                usb.write(b'yd')
                print("Ydown")
             elif  request.form.get('Zup') == 'Zup':
                # pass # do something else
                print("Zup")
             elif  request.form.get('Zdown') == 'Zdown':
                # pass # do something else
                print("Zdown")
             elif request.form.get('Humidity') == 'Humidity':
                     usb.write(b'h')  # send command to Arduino
                     line = usb.readline()  # read input from Arduino
                     line = line.decode()  # convert type from bytes to string
                     line = line.strip()  # strip extra whitespace charactersv
                     f = open("humidity.txt", "w") #write humidity in file
                     f.write(line)
                     f.close()
    
    elif request.method == 'GET':
            
            print("No Post Back Call")
            
    
    with open('humidity.txt', 'r') as f: 
                        humidity= f.read()
                        return render_template('farmbot.html', h=humidity) #update page with

    

if __name__ == '__main__':
	app.run(host='192.168.1.12',debug=True, threaded=True)
	
