class Garage():
        
    def __init__(self, tickets, parkingSpaces = 10, currentTicket):
        self.tickets = [i for i in range(9)]
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket
        
           
    def takeTicket(self):
        givenTicket = self.tickets.pop(0)
        print(f"Your ticket is ticket #{givenTicket}! Please park safely!")
        self.parkingSpaces -= 1            
        
    def payForParking(self):
    
    
    def leaveGarage(self):
        
        
def park():
    choice = input("Welcome to SuperLot! Would you like get a 'ticket', 'pay', or 'leave'? ")
    if choice.lower() == "ticket":
        takeTicket() 
    
    if choice.lower() == "pay":
        payForParking()
    
    if choice.lower() == "leave":
        leaveGarage()
        