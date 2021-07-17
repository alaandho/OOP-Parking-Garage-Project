import random

class ParkingGarage():
    def __init__(self, tickets, parkingSpaces, paidTickets):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.paidTickets = paidTickets
        
        
    def takeTickets(self):
        park_space = input('Please enter parking space: ')
        rand_ticket = random.choice(self.tickets)
        if park_space.upper() in self.parkingSpaces and rand_ticket in self.tickets:
            self.parkingSpaces.remove(park_space.upper())
            self.tickets.remove(rand_ticket)
            print(f'Your ticket number is {rand_ticket} and your parking space is {park_space.upper()}')
        else:             
            print(f'Error, parking space {park_space.upper()} is occupied. Please try again')
        return (rand_ticket, park_space)
        
            
# # ParkingGarage([1,2,3,4,5], ['A','B','C','D','E'], {})
# checkspace.takeTicket(['A','B','C','D','E'])


    def payForParking(self, rand_ticket):
        cell = "pay" # --> Testing for pay
        if cell.lower() == "pay":
            self.paidTickets[rand_ticket] = 'paid'
            print(f'Thank you, your ticket has been paid: {self.paidTickets}')
        else:
            print("Error: please enter valid response")
            
    def leaveGarage(self, rand_ticket, park_space):
        if "paid" in self.paidTickets.values():
            print('You have 15 minutes to leave. Have a nice day!')
            self.parkingSpaces.append(park_space.upper())
            self.tickets.append(rand_ticket)

            
# res=ParkingGarage([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ["A", 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J'], {})      
# x, y = res.takeTickets()
# res.payForParking(x) # passing x from function takeTickets to other functions 
# res.leaveGarage(x, y)



def runGarage():
    res = ParkingGarage([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ["A", 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J'], {})
    x = 0 # 0 is a placeholder --> x needs to be declared
    y = '' # empty string is a placeholder --> y needs to be declared
    
    while True:
        cell = input("Please enter what you would like to do: 'park', 'pay', 'leave' ")
        if cell.lower() == "park":
            x, y = res.takeTickets()
        elif cell.lower() == "pay":
            res.payForParking(x)
        elif cell.lower() == "leave":
            res.leaveGarage(x, y)
            break
            
runGarage() 