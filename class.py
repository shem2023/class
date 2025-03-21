# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.__battery = battery  # Encapsulated attribute

    def charge(self, amount):
        """Charges the battery by a specified amount."""
        self.__battery = min(100, self.__battery + amount)
        print(f"{self.brand} {self.model} charged to {self.__battery}%")

    def call(self, minutes):
        """Simulates a call that drains battery."""
        drain = minutes * 2  # 2% per minute
        if self.__battery > drain:
            self.__battery -= drain
            print(f"Called for {minutes} min. Battery now at {self.__battery}%")
        else:
            print("Battery too low for a call!")

    def check_battery(self):
        """Displays the current battery level."""
        print(f"{self.brand} {self.model} battery: {self.__battery}%")

# Subclass: GamingSmartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, battery, cooling_system):
        super().__init__(brand, model, battery)
        self.cooling_system = cooling_system  # Extra feature for gaming

    def play_game(self, hours):
        """Simulates playing a game, which drains more battery."""
        drain = hours * 20  # 20% per hour
        if self.check_battery_level() > drain:
            self._Smartphone__battery -= drain  # Accessing private attribute
            print(f"Played for {hours} hours. Battery now at {self.check_battery_level()}%")
        else:
            print("Battery too low for gaming!")

    def check_battery_level(self):
        """Accessing private battery level."""
        return self._Smartphone__battery

# Creating objects
phone1 = Smartphone("Samsung", "Galaxy S22", 50)
phone1.charge(30)
phone1.call(10)
phone1.check_battery()

gaming_phone = GamingSmartphone("Asus", "ROG Phone 7", 80, "Advanced Liquid Cooling")
gaming_phone.play_game(3)
gaming_phone.check_battery()
