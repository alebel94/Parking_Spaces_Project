class Garage():

    def __init__(self, tickets = [i for i in range(1, 11)], parkingSpaces = 10, currentTicket = {}):
        self.tickets = [i for i in range(1, 11)]
        self.parkingSpaces = 10
        self.currentTicket = {}

    def takeTicket(self):
        while True:
            if len(self.tickets) == 0:
                print("Sorry, there are no more spaces available :(((\n")
                break   
            else:
                givenTicket = self.tickets.pop(0)
                print(f"Your ticket is ticket #{givenTicket}! Please park safely!\n")
                self.parkingSpaces -= 1 
                self.currentTicket[str(givenTicket)] = False
                break

    def payForParking(self):
        payParkNum = input("What is your ticket number?\n\n")
        while True:
            while payParkNum.isnumeric() == False or int(payParkNum) < 1:
                print("Beep Boop Beep Boop dOeS nOt CoMpUtE. Please enter a number between 1 and 10.\n")
                payParkNum = input()
            while int(payParkNum) not in range(1,11):
                print("Sorry, our modest parking lot can only accommodate so many drivers. Please enter a number between 1 and 10.\n")
                payParkNum = input()
            break
        while int(payParkNum) in self.tickets:
            print('Sorry that cannot be your space.\n')
            print(f'Please choose from one of the following unpaid tickets: {[key for key in self.currentTicket.keys()]}')
            payParkNum = input()
        while self.currentTicket[payParkNum] == True:
            print("We would love more money, but this ticket has already been paid!\n")  
            payParkNum = input()
        else:
            self.currentTicket[payParkNum] = True
            print("Ticket has been paid. Please exit carefully to the right!\n")

    def leaveGarage(self):
        leave_number = input("What is your ticket number?\n\n")
        while leave_number not in self.currentTicket:
            print("That ticket is not in use.\n")
            print(f'The following tickets have been paid but have yet to leave the garage: ' 
                f'{[key for key, value in self.currentTicket.items() if value == True]}'
                '\n\nWhich ticket would you like to pay for?: ')
            leave_number = input()
        if self.currentTicket[leave_number] == True:
            print("\nThank you for parking at SuperLot!\n")
            del self.currentTicket[leave_number]
            self.parkingSpaces += 1
            self.tickets.append(int(leave_number))
        elif self.currentTicket[leave_number] == False:
            print("Parking isn't free! Please pay at your nearest kiosk!\n")
        
def park():

    take = Garage()

    while True:
        choice = input("Welcome to SuperLot!" f" These are the spaces currently available: {sorted(take.tickets)}\n\n"
            "Would you like to get a 'ticket', 'pay', or 'leave'?\n\n")
        if choice.lower() == "ticket":
            take.takeTicket() 
        elif choice.lower() == "pay":
            if take.currentTicket == {}:
                print("There are no tickets to pay for.")
            else:
                take.payForParking()
        elif choice.lower() == "leave":
            if take.currentTicket == {}:
                print("There are no tickets in use to leave.")
            elif True not in [value for key, value in take.currentTicket.items()]:
                print("No tickets have been paid for. You must pay for your ticket before leaving.")
            else:
                take.leaveGarage()
        else:
            print(f"It seems that '{choice}' is not a valid input. Please make sure you type 'ticket', 'pay', or 'leave'.\n\n")
park()
