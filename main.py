import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 50
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress +=0.12
        self.gladness -=3

    def to_sleep(self):
        print("I want to sleep")
        self.gladness +=3

    def to_chill(self):
        print("Rest time")
        self.gladness +=5
        self.progress -=0.1
        self.money -=0.5

    def to_magazin(self):
        print("I want to Magazin")
        self.gladness +=3
        self.money -=3

    def to_work(self):
        print("I want to Working")
        self.progress -=0.2
        self.money +=20

    def is_alive(self):
        if self.progress <-0.5 :
            print("Tebe vidraxovano!")
            self.alive = False
        elif self.gladness <-0 :
            print("Depression...")
            self.alive = False
        elif self.progress > 5 :
            print("Tu zdav (alive = False)")
            self.alive = False
        elif self.money < 0 :
            print("Tu Bomж (alive = False)")
            self.alive = False
        elif self.money > 100 :
            print("Tu Bogat (alive = False)")
            self.alive = False

    def end_of_day(self):
        print(f"gladness = {self.gladness}")
        print(f"progress {round(self.progress,2)}")
        print(f"Money = {round(self.money,2)}")

    def live(self, day):
        day = "Day" + str(day) + "of" +self.name + "life"
        print(f"{day:=^50}")
        vupadkova = random.randint(1,5)
        if vupadkova == 1 :
            self.to_study()
        elif vupadkova == 2 :
            self.to_sleep()
        elif vupadkova ==3 :
            self.to_chill()
        elif vupadkova ==4 :
            self.to_work()
        elif vupadkova ==5 :
            self.to_magazin()
        self.end_of_day()
        self.is_alive()

Pablj = Student(name = "Pablj")

for day in range(365):
    if Pablj.alive == False:
        break
    Pablj.live(day)