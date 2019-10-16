import time
import serial
import db_fnc
import config

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600)

ser.isOpen()




def ser_cmd(cmd):
        ser.write(cmd + '\r')
        out = ''
        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(1)
        while ser.inWaiting() > 0:
            out += ser.read(1)

        out = out.replace("\r","")
        out = out.replace("\n","")
        if out != '':
            print out
        return out

def store_voltage(cell,voltage):
        fields = "cell,voltage"
        values = "{},{}".format(cell,voltage)
        db_fnc.insert_record(config.voltages_table_name,fields,values)



def check_voltages():
        for i in config.cell_adresses:
                out  = ser_cmd("{}voltage".format(i))
                tmp = out.split()
                try:
                        voltage = tmp[1].replace("V","")
                        store_voltage(i,voltage)
                except:
                        print ("Can't find V for cell {} with output {}".format(i,out))
        

def main():
        #while (1):
        check_voltages()

if __name__ == "__main__":
        main()
ser.close()
