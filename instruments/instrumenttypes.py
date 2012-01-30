
try:
    import visa
except:
    print "Warning VISA library import failed"
import telnetlib
import socket
import time
import serial

class Instrument(object):
    """
    A subclass of Instrument is an instrument which communicates over a certain
    channel. The subclass must define the methods write and read, for
    communication over that channel
    """
    # (Phil) Are these class variables ever set? Looks like everything used is
    # part of the object rather than the class 
    # (i.e. self.address vs Instrument.address)
    address=''                #Address of instrument
    name=''                   #Instrument Name
    enabled=False             #If enabled=False commands should not be sent
    instrument_type=''        #Instrument type
    protocol=''               #Protocol 
    id_string=''              #id string
    timeout=0                 #timeout for commands
    query_sleep=0             #seconds to wait between write and read
    term_char='\n'            #character to be appended to all writes
    #operation_range={}        #map to hold the operation range
    
    def  __init__(self,name,address='',enabled=True):
        self.name=name
        self.address=address
        self.enabled=enabled
        
    def query(self,cmd):
        self.write(cmd)
        time.sleep(self.query_sleep)
        return self.read()
        
    def set_timeout(self,timeout):
        self.timeout=timeout
    
    def get_timeout(self):
        return self.timeout

    def get_settings(self):
        settings={}
        settings['name']=self.name
        settings['address']=self.address
        settings['instrument_type']=self.instrument_type
        settings['protocol']=self.protocol
        return settings
        
    def set_settings(self,settings):
        print settings

    #def set_operation_range(self, operation_range):
    #    self.operation_range = operation_range
    
    #def get_operation_range(self):
    #    return self.operation_range

class VisaInstrument(Instrument):
    def __init__(self,name,address='',enabled=True):
        Instrument.__init__(self,name,address,enabled)
        if self.enabled:
            self.protocol='GPIB'
            self.instrument=visa.instrument(address)
            
    def write(self, s):
        if self.enabled: self.instrument.write(s+self.term_char)
    def read(self):
        if self.enabled: return self.instrument.read()
        
    def close(self):
        if self.enabled: self.instrument.close()
        
#    def __del__(self):
#        if self.enabled: self.close()

class TelnetInstrument(Instrument):
    def __init__(self,name,address='',enabled=True,timeout=10):
        Instrument.__init__(self,name,address,enabled)
        self.protocol='Telnet'
        if len(address.split(':')) >1:
            self.port=int(address.split(':')[1])
        if self.enabled:
            self.tn=telnetlib.Telnet(address.split(':')[0],self.port)    
        
    def write(self, s):
        if self.enabled: self.tn.write(s+self.term_char)
    def read(self):
        if self.enabled: return self.tn.read_some()       
    def close(self):
        if self.enabled: self.tn.close()       
#    def __del__(self):
#        if self.enabled: self.tn.close()
        
class SocketInstrument(Instrument):
    def __init__(self,name,address='',enabled=True,timeout=10, recv_length=1024):
        Instrument.__init__(self,name,address,enabled)
        self.protocol='socket'
        self.recv_length = recv_length       
        if len(address.split(':')) >1:
            self.port=int(address.split(':')[1])
        if self.enabled:
            self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.socket.connect((address.split(':')[0],self.port))

    def set_timeout(self,timeout):
        Instrument.set_timeout(self,timeout)
        if self.enabled: self.socket.settimeout(self.timeout)
    
    def write(self, s):
        if self.enabled: self.socket.send(s+self.term_char)
        
    def read(self):
        if self.enabled: return self.socket.recv(self.recv_length)

#    def __del__(self):
#        if self.enabled: self.socket.close()

class SerialInstrument(Instrument):
    
    def __init__(self, name, address, enabled=True, timeout=.1, 
                 recv_length=1024, baudrate=9600, querysleep=1):
        Instrument.__init__(self, name, address, enabled)
        self.protocol='serial'
        self.enabled=enabled
        if self.enabled:
            try:
                self.ser = serial.Serial(int(address[-1])-1, baudrate)
            except serial.SerialException:
                print 'Cannot create a connection to port '+str(address)+'.\n'
        self.set_timeout(timeout)
        self.recv_length = recv_length
        self.query_sleep = querysleep
    
    def set_timeout(self,timeout):
        Instrument.set_timeout(self,timeout)
        if self.enabled: self.ser.setTimeout(self.timeout)
        
    def set_query_sleep(self, querysleep):            
        self.query_sleep = querysleep
        
    def write(self, s):
        if self.enabled: self.ser.write(s+self.term_char)
        
    def read(self):
        if self.enabled: return self.ser.read(self.recv_length)

#    def __del__(self):
#        if self.enabled: self.ser.close()
        
