class TimeInvalid(Exception):
    pass

# Personnal Time python class implementation.
class Time:
    def __init__(self, hour=0 ,minute=0, seconde=0):

        for elt in [hour,minute,seconde]:
            if elt == hour:
                if elt>23 or elt<0:
                    raise TimeInvalid
            else:
                if elt>59 or elt <0:
                    raise TimeInvalid
        self.hour = hour
        self.minute = minute
        self.seconde = seconde

    def __str__(self):
        if self.hour <=9:
            heure="0"+str(self.hour)
        else:
            heure = str(self.hour)

        if self.minute <=9:
            minute="0"+str(self.minute)
        else:
            minute = str(self.minute)

        if self.seconde <= 9:
            seconde = "0" + str(self.seconde)
        else:
            seconde = str(self.seconde)
        return "{}:{}:{}".format(heure,minute,seconde)

    def __add__(self,other):

        if type(other) == type(self):
            return self + (other.hour*60*60 + other.minute*60 + other.seconde)

        elif type(other)==type(int()):

            RESERVE = self.hour *3600 + self.minute*60 + self.seconde + other

            h = int( RESERVE //3600)
            RESERVE -= h*3600
            m = int (RESERVE //60)
            RESERVE -=  m*60
            s = RESERVE
            #Normaliser les heures

            h = ((h*3600) %86400)//3600

            return Time(h, m, s)
    def __sub__(self,other):

        if type(other) == type(self):
            return self - (other.hour*60*60 + other.minute*60 + other.seconde)

        elif type(other)==type(int()):

            RESERVE = self.hour *3600 + self.minute*60 + self.seconde - other

            h = int( RESERVE //3600)
            RESERVE -= h*3600
            m = int (RESERVE //60)
            RESERVE -=  m*60
            s = RESERVE
            #Normaliser les heures

            h = ((h*3600) %86400)//3600

            return Time(h, m, s)
    def __eq__(self,other):
        if type(other) == type(self):
            return (self.hour*60*60+self.minute*60+self.seconde) == (other.hour*60*60 + other.minute*60 + other.seconde)

        elif type(other)==type(int()):
            return (self.hour*60*60+self.minute*60+self.seconde) == other

    def __gt__(self,other):
        if type(other) == type(self):
            return (self.hour*60*60+self.minute*60+self.seconde) > (other.hour*60*60 + other.minute*60 + other.seconde)

        elif type(other)==type(int()):
            return (self.hour*60*60+self.minute*60+self.seconde) > other

    def __lt__(self,other):
        if type(other) == type(self):
            return (self.hour*60*60+self.minute*60+self.seconde) < (other.hour*60*60 + other.minute*60 + other.seconde)

        elif type(other)==type(int()):
            return (self.hour*60*60+self.minute*60+self.seconde) < other

    def __ne__(self,other):
        if type(other) == type(self):
            return (self.hour*60*60+self.minute*60+self.seconde) != (other.hour*60*60 + other.minute*60 + other.seconde)

        elif type(other)==type(int()):
            return (self.hour*60*60+self.minute*60+self.seconde) != other

    def __ge__(self,other):
        if type(other) == type(self):
            return (self.hour*60*60+self.minute*60+self.seconde) >= (other.hour*60*60 + other.minute*60 + other.seconde)

        elif type(other)==type(int()):
            return (self.hour*60*60+self.minute*60+self.seconde) >= other

    def __le__(self,other):
        if type(other) == type(self):
            return (self.hour*60*60+self.minute*60+self.seconde) <= (other.hour*60*60 + other.minute*60 + other.seconde)

        elif type(other)==type(int()):
            return (self.hour*60*60+self.minute*60+self.seconde) <= other

    def __key(self):
        return (self.hour*60*60 + self.minute*60 + self.seconde,)
    def __hash__(self):
        return hash(self.__key())
