# Theme Park Task
class Attraction:
    def __init__(self, name, capacity):
        self.__name = name 
        self.__capacity = capacity

    def get_details(self):
        return f"Attraction: {self.__name}, Capacity: {self.__capacity}"

    def start(self):
        return "The attraction is starting."

#Thrill Ride
class ThrillRide(Attraction):
    def __init__(self, name, capacity, min_height):
        super().__init__(name, capacity)
        self.__min_height = min_height

    def start(self):
        return f"Thrill Ride {self._Attraction__name} is now starting. Hold on tight!"

    def is_eligible(self, height):
        return height >= self.__min_height

class FamilyRide(Attraction):
    def __init__(self, name, capacity, min_age):
        super().__init__(name, capacity)
        self.__min_age = min_age  

    def start(self):
        return f"Family Ride {self._Attraction__name} is now starting. Enjoy the fun!"

    def is_eligible(self, age):
        return age >= self.__min_age

#Roles
class Staff:
    def __init__(self, name, role):
        self.__name = name
        self.__role = role

    def work(self):
        return f"Staff {self.__name} is performing their role: {self.__role}."

class Visitor:
    def __init__(self, name, age, height):
        self.__name = name
        self.__age = age
        self.__height = height

    def ride(self, attraction):
        if isinstance(attraction, ThrillRide):
            if attraction.is_eligible(self.__height):
                return f"Visitor {self.__name} can ride {attraction._Attraction__name}."
            else:
                return f"Visitor {self.__name} does not meet the height requirement for {attraction._Attraction__name}."
        elif isinstance(attraction, FamilyRide):
            if attraction.is_eligible(self.__age):
                return f"Visitor {self.__name} can ride {attraction._Attraction__name}."
            else:
                return f"Visitor {self.__name} does not meet the age requirement for {attraction._Attraction__name}."
        else:
            return "Unknown attraction type."

 

#Capacity
thrill_ride = ThrillRide("Dragon Coaster", 20, 140)
family_ride = FamilyRide("Merry-Go-Round", 30, 4)

#Staff and Visitor
staff = Staff("Mahdi", "Walkden")
visitor = Visitor("Jin", 16, 173)


print(thrill_ride.get_details())
print(family_ride.get_details())


print(visitor.ride(thrill_ride))
print(visitor.ride(family_ride))


attractions = [thrill_ride, family_ride]
for attraction in attractions:
    print(attraction.start())
