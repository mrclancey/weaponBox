from arsonal import Inventory,Fireball,LaserGun,Shield

# Testing the Fireball class
print("\nTesting the Fireball class:")
fb = Inventory.add_fireball(size=3, power=10, flame_color="orange")
print("Fireball created.")
print("Fireball material:", fb.material)
fb.change_material("kerosene")
print("Fireball material changed:", fb.material)
print("Fireball size:", fb.size)
fb.grow(2)
print("Fireball size increased:", fb.size)
Inventory.add_target("Just a Guy", 20)
Inventory.add_target("Jack Knife", 5)
fb.fire("Just a Guy")
fb.fire("Jack Knife")
fb.fire("Manimal")

# Testing the Shield class
print("\nTesting the Shield class:")
shield = Shield(strength=15)
print("Shield created.")
shield.deflect(10)
shield.deflect(20)

# Testing the LaserGun class
print("\nTesting the LaserGun class:")
lg = LaserGun(laser_color="red", dist=15, max_charge=25)
print("LaserGun created.")
print("LaserGun color:", lg.laser_color)
lg.change_color("blue")
print("LaserGun color changed:", lg.laser_color)
print("LaserGun distance:", lg.dist)
print("LaserGun charge level:", lg.charge/lg.max_charge*100)
lg.charge_up()
print("LaserGun charge level after charging:", lg.charge/lg.max_charge*100)
lg.add_target("Just a Guy", 20)
lg.add_target("Jack Knife", 5)
print("LaserGun targets:", lg.targets)
lg.fire("Just a Guy")
lg.fire("Jack Knife")
lg.fire("Manimal")
lg.charge = 25
lg.fire("Just a Guy")
