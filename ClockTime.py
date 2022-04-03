class clockTime:

    # Constructor to initialize the hours, minutes, seconds
    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    # Set hours Function
    def setHours(self, hours):
        self.hours = hours

    # Set minutes Function
    def setMinutes(self, minutes):
        self.minutes = minutes

    # Set seconds Function
    def setSeconds(self, seconds):
        self.seconds = seconds

    # Set hours, minutes, seconds Function
    def setTime(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    # Display time function in the format of hours:minutes:seconds
    def showTime(self):
        print("Time is {}:{}:{}".format(self.hours, self.minutes, self.seconds))


# This program will only accept
# hours : from 0 to 24 in integer
# minutes & seconds : from 0 to 60 in integer
if __name__ == '__main__':
    hours = -1
    minutes = -1
    seconds = -1

    # A loop to continue to other functions only if the input for hours
    # is more than or equal 0 or less than and equal to 24
    while hours > 24 or hours < 0:
        hours = int(input("Enter hours: "))
        if hours > 24 or hours < 0:
            print("Invalid input for number of hours. Please try again.")

    # A loop to continue to other functions only if the input for minute
    # is more than or equal 0 or less than and equal to 60
    while minutes > 60 or minutes < 0:
        minutes = int(input("Enter minutes: "))
        if minutes > 60 or minutes < 0:
            print("Invalid input for number of minutes. Please try again.")

    # A loop to continue to other functions only if the input for seconds
    # is more than or equal 0 or less than and equal to 60
    while seconds > 60 or seconds < 0:
        seconds = int(input("Enter seconds: "))
        if seconds > 60 or seconds < 0:
            print("Invalid input for number of seconds. Please try again.")

    c = clockTime()

    # Function call to set the hours, minutes and seconds of the time.
    c.setTime(hours, minutes, seconds)

    # Function call to show the formatted time
    c.showTime()
