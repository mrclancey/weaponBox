class Fireball:
    def __init__(self, size, power, flame_color, material="gasoline"):
        self.size = size
        self.power = power
        self.flame_color = flame_color
        self.material = material

    def fire(self, target):
        if target in Inventory.targets:
            print(f"Firing the fireball at {target}! 🔥🔥🔥")
            Inventory.fireball_charges -= 5
        else:
            print(f"Target {target} not found.")
        
    def change_material(self, new_material):
        print(f"Changing the material of the fireball to {new_material}...")
        self.material = new_material

    def grow(self, increase_size):
        print(f"Increasing the size of the fireball by {increase_size} units...")
        self.size += increase_size


class Shield:
    def __init__(self, strength):
        self.strength = strength

    def deflect(self, weapon_power):
        if weapon_power <= self.strength:
            print("Shield successfully deflected the attack!")
        else:
            print("Shield was not strong enough to deflect the attack.")


class LaserGun:
    def __init__(self, laser_color, dist, max_charge=25):
        self.charge = 0
        self.laser_color = laser_color
        self.targets = Inventory.targets
        self.dist = dist
        self.max_charge = max_charge

    def fire(self, target):
        if target in self.targets:
            if self.charge == self.max_charge:
                if self.targets[target] <= self.dist:
                    print(f"Firing laser at {target}! 🔫💥")
                    self.charge -= 5
                else:
                    print(f"{target} is out of range.")
            else:
                print("Laser gun not fully charged.")
        else:
            print(f"Target {target} not found.")

    def charge_up(self):
        if self.charge < self.max_charge:
            self.charge += 1
        else:
            print("Laser gun already fully charged.")

    def add_target(self, name, dist):
        self.targets[name] = dist

    def change_color(self, new_color):
        self.laser_color = new_color

    def check_gun(self):
        print(f"Laser gun charge level: {self.charge/self.max_charge*100:.2f}%")
        print(f"Laser color: {self.laser_color}")
        print(f"Range: {self.dist}")


class Inventory:
    fireball_charges = 0
    targets = {}

    @classmethod
    def add_fireball(cls, size, power, flame_color, material="gasoline"):
        fireball = Fireball(size, power, flame_color, material)
        cls.fireball_charges += 1
        return fireball

    @classmethod
    def add_target(cls, name, dist):
        cls.targets[name] = dist
