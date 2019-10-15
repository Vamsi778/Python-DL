class Person(object):
    count_of_person=0
    def __init__(self,Name,Age,Sex):
        self.Name=Name
        self.Age=Age
        self.Sex=Sex
        Person.count_of_person += 1
        
    def printPersonDetails(self):
        return str((self.Name,self.Sex,self.Age))
    
    def getPersonCount(self):
        print("Total People: ",self.count_of_person)
        
class Flight(object):
    count_of_flights=0
    def __init__(self,Airlines_Code,From,To,Date):
        self.Airlines_Code=Airlines_Code
        self.From_Loc=From
        self.To_Loc=To
        self.Date=Date
        Flight.count_of_flights += 1
        
    def getFlightDetails(self):
        return self.Airlines_Code,self.From_Loc,self.To_Loc,self.Date
    
    def getFlightCount(self):
        print("No of Flights: ",self.count_of_flights)

class Employee(Person):
    count_of_employees=0
    def __init__(self, Name, Age, Sex, ID):
        super().__init__(Name,Age,Sex)
        
        self.ID=ID
        Employee.count_of_employees += 1
        
    def outputEmployeeDetails(self):
        print("Here are the Employee Details: ",self.printPersonDetails(),self.ID)
        
    def getEmployeeCount(self):
        print("No of Employees: ",self.count_of_employees)
        

        
class Passenger(Person):
    flight_Details = None
    passenger_count=0
    def __init__(self,Name,Age,Sex,ID_No,flight):
        Person.__init__(self,Name,Age,Sex)
        self.ID_No=ID_No
        self.flight_Details=flight.getFlightDetails()
        Passenger.passenger_count += 1
        
    def printPassengerDetails(self):
        print("Here are the Passenger Details ===> ",self.Name,"who's age is ",self.Age,",who's is a ",self.Sex,",ID is ",self.ID_No,"and flight details are",self.flight_Details)
        
    def getPassengerCount(self):
        print("No of Passengers: ",self.passenger_count)
        

        
class Pilot(Person, Flight):
    pilot_count=0
    assigned_flight=None
    def __init__(self,Name,Age,Sex,Pilot_ID,flight):
        Person.__init__(self,Name,Age,Sex)
        self.assigned_flight=flight.getFlightDetails()
        self.Pilot_ID=Pilot_ID
        Pilot.pilot_count += 1
        
    def pilotDetails(self):
        print("Pilot Details: ",Person.printPersonDetails(self),self.Pilot_ID,"and the assigned flight details are",self.assigned_flight)
        
    def getPilotCount(self):
        print("No of Pilots: ",self.pilot_count)
        
if __name__ == "__main__":
    
    flight1=Flight(9893,'Dubai','Ukraine','Mar-31-20')
    flight2=Flight(1235,'LA','DTW','May-23-20')
    flight3=Flight(6754,'NYC','Boston','Feb-25-20')
    flight4=Flight(5646,'ORD','HYD','Jan-25-20')
    passenger1=Passenger('Timberlake',23,'Male','Q412',flight1)
    passenger2=Passenger('Charles',42,'Male','P412',flight2)
    passenger3=Passenger('Tracey',34,'Male','B4812',flight3)
    Employee1=Employee('Jason',56,'Male','Amazon')
    Employee2=Employee('Maseerah',51,'Female','Microsoft')
    Employee3=Employee('Ahmed',51,'Male','IBM')
    Employee4=Employee('Vamsi',22,'Male','Cerner')

    pilot1=Pilot('Montana',33,'Female','O5463',flight1)
    pilot2=Pilot('Kiara',31,'Female','M5765',flight2)
    pilot3=Pilot('Justin',32,'Male','L0985',flight3)
    pilot4=Pilot('John',34,'Male','A6754',flight4)
    
    Employee1.outputEmployeeDetails()
    Employee2.outputEmployeeDetails()
    Employee3.outputEmployeeDetails()
    Employee4.outputEmployeeDetails()
    

    passenger1.printPassengerDetails()
    passenger2.printPassengerDetails()
    passenger3.printPassengerDetails()
    pilot1.pilotDetails()
    
    pilot2.pilotDetails()
    
    pilot3.pilotDetails()
    
    pilot4.pilotDetails()
    
    
    pilot4.getPilotCount()
    
    flight3.getFlightCount()
    passenger3.getPersonCount()
    Employee3.getEmployeeCount()
    
    
    
        
