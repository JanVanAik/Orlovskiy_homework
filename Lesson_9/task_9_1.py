from time import sleep


class TrafficLight:
    __color = "traffic lighter"


    def running(self):
        print("\033[31m{}".format(self.__color))
        sleep(7)
        print('\033[33m\033[6m{}'.format(self.__color))
        sleep(2)
        print('\033[32m{}'.format(self.__color))
        sleep(7)
        print("\033[31m{}".format(self.__color))


a = TrafficLight()
a.running()
