import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Asegúrate de importar ttk correctamente 
from tkinter import colorchooser

class Objeto:
    def __init__(self, nombre, caracteristicas):
        self.nombre = nombre
        self.caracteristicas = caracteristicas

    def multiplicar_caracteristicas(self, cantidad):
        for caracteristica, valor in self.caracteristicas.items():
            self.caracteristicas[caracteristica] = valor * cantidad
            
    def __str__(self):
        caracteristicas_str = "\n".join([f"{car}: {int(val)}" for car, val in self.caracteristicas.items()])
        return f"Crafteo: {self.nombre}\nItems:\n{caracteristicas_str}"


class ObjetoEspecial(Objeto):
    def __init__(self, nombre, caracteristicas, mensaje_extra=""):
        super().__init__(nombre, caracteristicas)
        self.mensaje_extra = mensaje_extra

    def multiplicar_caracteristicas(self, cantidad):
        super().multiplicar_caracteristicas(cantidad)
        for caracteristica, valor in self.caracteristicas.items():
            self.caracteristicas[caracteristica] = valor / 3  # Dividir entre tres
            parte_entera = int(self.caracteristicas[caracteristica])
            if parte_entera % 4 != 0:
                self.caracteristicas[caracteristica] += (4 - parte_entera % 4)  # Ajustar para que sea múltiplo de 4

    def __str__(self):
        caracteristicas_str = "\n".join([f"{car}: {int(val)}" for car, val in self.caracteristicas.items()])
        return f"Crafteo: {self.nombre}\nItems:\n{caracteristicas_str}\nImportante: {self.mensaje_extra}"
    
class ObjetoDividirEntreCuatro(Objeto):
    def multiplicar_caracteristicas(self, cantidad):
        super().multiplicar_caracteristicas(cantidad)
        for caracteristica, valor in self.caracteristicas.items():
            self.caracteristicas[caracteristica] /= 4  # Dividir entre cuatro

class ObjetoDividirEntreTres(Objeto):
    def multiplicar_caracteristicas(self, cantidad):
        super().multiplicar_caracteristicas(cantidad)
        for caracteristica, valor in self.caracteristicas.items():
            self.caracteristicas[caracteristica] /= 3  # Dividir entre cuatro

class ObjetoDividirEntreDos(Objeto):
    def multiplicar_caracteristicas(self, cantidad):
        super().multiplicar_caracteristicas(cantidad)
        for caracteristica, valor in self.caracteristicas.items():
            self.caracteristicas[caracteristica] /= 2  # Dividir entre dos

class ObjetoDividirEntreSeis(Objeto):
    def multiplicar_caracteristicas(self, cantidad):
        super().multiplicar_caracteristicas(cantidad)
        for caracteristica, valor in self.caracteristicas.items():
            self.caracteristicas[caracteristica] /= 6  

class ObjetoDividirEntreOcho(Objeto):
    def multiplicar_caracteristicas(self, cantidad):
        super().multiplicar_caracteristicas(cantidad)
        for caracteristica, valor in self.caracteristicas.items():
            self.caracteristicas[caracteristica] /= 8

class ObjetoDividirEntreDiezYSeis(Objeto):
    def multiplicar_caracteristicas(self, cantidad):
        super().multiplicar_caracteristicas(cantidad)
        for caracteristica, valor in self.caracteristicas.items():
            self.caracteristicas[caracteristica] /= 16 
    def __init__(self, nombre, caracteristicas, mensaje_extra=""):
        super().__init__(nombre, caracteristicas)
        self.mensaje_extra = mensaje_extra
    def __str__(self):
        caracteristicas_str = "\n".join([f"{car}: {int(val)}" for car, val in self.caracteristicas.items()])
        return f"Crafteo: {self.nombre}\nItems:\n{caracteristicas_str}\nimportant: {self.mensaje_extra}"

class ObjetoDividirEntreNueve(Objeto):
    def multiplicar_caracteristicas(self, cantidad):
        super().multiplicar_caracteristicas(cantidad)
        for caracteristica, valor in self.caracteristicas.items():
            self.caracteristicas[caracteristica] /= 9  # Dividir entre dos
    def __init__(self, nombre, caracteristicas, mensaje_extra=""):
        super().__init__(nombre, caracteristicas)
        self.mensaje_extra = mensaje_extra
    def __str__(self):
        caracteristicas_str = "\n".join([f"{car}: {int(val)}" for car, val in self.caracteristicas.items()])
        return f"Crafteo: {self.nombre}\nItems:\n{caracteristicas_str}\nimportant: {self.mensaje_extra}"
    
class ObjetoImportante(Objeto):
    def __init__(self, nombre, caracteristicas, mensaje_extra=""):
        super().__init__(nombre, caracteristicas)
        self.mensaje_extra = mensaje_extra
    def __str__(self):
        caracteristicas_str = "\n".join([f"{car}: {int(val)}" for car, val in self.caracteristicas.items()])
        return f"Crafteo: {self.nombre}\nItems:\n{caracteristicas_str}\nimportant: {self.mensaje_extra}"    


def obtener_nombres_objetos():
    objetos = [
        "Selec Item",
       "Piston",
        "Dispenser",
        "Arrows",
        "Spectral Arrows",
        "Crossbow",
        "Bow",
        "Wooden Sword",
        "Golden Sword",
        "Stone Sword",
        "Iron Sword",
        "Diamond Sword",
        "Diamond Helmet"
        "Golden Helmet"
        "Iron Helmet"
        "Leather Cap"
        "Turtle Shell"
        "Diamond Chestplate",
        "Golden Chestplate",
        "Iron Chestplate",
        "Leather Tunic",
        "Diamond Leggings",
        "Golden Leggings",
        "Iron Leggings",
        "Leather Pants",
        "Diamond Boots",
        "Golden Boots",
        "Iron Boots",
        "Leather Boots",
        "Diamond Shovel",
        "Iron Shovel",
        "Stone Shovel",
        "Wooden Shovel",
        "Golden Shovel",
        "Diamond Hoe",
        "Iron Hoe",
        "Stone Hoe",
        "Wooden Hoe",
        "Golden Hoe",
        "Diamond Axe",
        "iron Axe",
        "Stone Axe",
        "Wooden Axe",
        "Golden Axe",
        "Diamond Pickaxe",
        "Iron Pickaxe",
        "Stone Pickaxe",
        "Wooden Pickaxe",
        "Golden Pickaxe",
        "FireWorksLV1",
        "FireWorksLV2",
        "FireWorksLV3",
        "Book",
        "Book % Quill",
        "Carrot on a Stick",
        "Clock",
        "Compass",
        "Empty Map",
        "End Crystal",
        "Fishing Rod",
        "Flint And Steel",
        "Glass Bottle",
        "Lead",
        "Shears",
        "Shield",
        "Spyglass",
        "Black Firework Star",
        "Blaze Powder",
        "Blue Firework Star",
        "Bone Meal",
        "Bowl",
        "Brown Firework Star",
        "Cyan Firework Star",
        "Eye of Ender",
        "Fermented Spider Eye",
        "Fire Charge",
        "Glistering Melon",
        "Gold Ingot",
        "Gold Nugget",
        "Gray Firework Star",
        "Green Firework Star",
        "Iron Ingot",
        "Iron Nugget",
        "Light Blue Firework Star",
        "light Gray Firework Star",
        "Lime Firework Star",
        "Magenta Firework Star",
        "Netherite Ingot",
        "Orange Firework Star",
        "Paper",
        "Pink Firework Star",
        "Purple Firework Star",
        "Red Firework Star",
        "Sugar",
        "White Firework Star",
        "Yellow Firework Star",
        "Glow Item Frame",
        "Item Frame",
        "Painting",
        "Acacia Boat",
        "Acacia Boat with Chest",
        "Birch Boat",
        "Birch Boat with Chest",
        "Dark Oak Boat",
        "Dark Oak Boat with Chest",
        "Jungle Boat",
        "Jungle Boat with Chest",
        "Mangrove Boat",
        "Mangrove Boat with Chest",
        "Oak Boat",
        "Oak Boat with Chest",
        "Suprece Boat",
        "Suprece Boat with Chest",
        "Minecart",
        "Minecart with Chest",
        "Minecart with Furnace",
        "Minecart with Hopper",
        "Minecart with TNT",
        "Black Dye",
        "Blue Dye",
        "Brown Dye",
        "Cyan Dye",
        "Gray Dye",
        "Light Blue Dye",
        "Light Gray Dye",
        "Lime Dye",
        "Magenta Dye",
        "Orange Dye",
        "Pink Dye",
        "Purple Dye",
        "Red Dye",
        "White Dye",
        "Yellow Dye",
        "Oak Fence",
        "Oak Fence Gate",
        "Oak Sign",
        "Oak Slab",
        "Oak Stairs",
        "Oak Trapdoor",
        "Stripped Oak Wood",
        "Oak Door",
        "Oak Wood",
        "Oak Planks",
        "Spruce Fence",
        "Spruce Fence Gate",
        "Spruce Sign",
        "Spruce Slab",
        "Spruce Stairs",
        "Spruce Trapdoor",
        "Stripped Spruce Wood",
        "Spruce Door",
        "Spruce Wood",
        "Spruce Planks",
            "Mangrove Fence",
        "Mangrove Fence Gate",
        "Mangrove Sign",
        "Mangrove Slab",
        "Mangrove Stairs",
        "Mangrove Trapdoor",
        "Stripped Mangrove Wood",
        "Mangrove Door",
        "Mangrove Wood",
        "Mangrove Planks",
             "Jungle Fence",
        "Jungle Fence Gate",
        "Jungle Sign",
        "Jungle Slab",
        "Jungle Stairs",
        "Jungle Trapdoor",
        "Stripped Jungle Wood",
        "Jungle Door",
        "Jungle Wood",
        "Jungle Planks",
            "Dark Oak Fence",
        "Dark Oak Fence Gate",
        "Dark Oak Sign",
        "Dark Oak Slab",
        "Dark Oak Stairs",
        "Dark Oak Trapdoor",
        "Stripped Dark Oak Wood",
        "Dark Oak Door",
        "Dark Oak Wood",
        "Dark Oak Planks",
            "Birch Fence",
        "Birch Fence Gate",
        "Birch Sign",
        "Birch Slab",
        "Birch Stairs",
        "Birch Trapdoor",
        "Stripped Birch Wood",
        "Birch Door",
        "Birch Wood",
        "Birch Planks",
            "Acacia Fence",
        "Acacia Fence Gate",
        "Acacia Sign",
        "Acacia Slab",
        "Acacia Stairs",
        "Acacia Trapdoor",
        "Stripped Acacia Wood",
        "Acacia Door",
        "Acacia Wood",
        "Acacia Planks",
        "Blue Ice",
        "Packed Ice",
        "Snow Block",
        "Dried Kelp Block",
        "Dark Prismarine",
        "Dark Prismarine Slab",
        "Dark Prismarine Stairs",
        "Prismarine",
        "Prismarine Brick Slab",
        "Prismarine Brick Stairs",
        "Prismarine Bricks",
        "Prismarine Slab",
        "Prismarine Stairs",
        "Prismarine Wall",
        "Black Banner",
        "Blue Banner",
        "Brown Banner",
        "Cyan Banner",
        "Gray Banner",
        "Green Banner",
        "light Blue Banner",
        "Light Gray Banner",
        "Lime Banner",
        "Magenta Banner",
        "Orange Banner",
        "Pink Banner",
        "Purple Banner",
        "Red Banner",
        "Whiter Banner"
        "Yellow Banner",
        "Black Wool",
        "Blue Wool",
        "Brown Wool",
        "Cyan Wool",
        "Gray Wool",
        "Green Wool",
        "light Blue Wool",
        "Light Gray Wool",
        "Lime Wool",
        "Magenta Wool",
        "Orange Wool",
        "Pink Wool",
        "Purple Wool",
        "Red Wool",
        "Yellow Wool",
        "Black Carpet",
        "Blue Carpet",
        "Brown Carpet",
        "Cyan Carpet",
        "Gray Carpet",
        "Green Carpet",
        "light Blue Carpet",
        "Light Gray Carpet",
        "Lime Carpet",
        "Magenta Carpet",
        "Orange Carpet",
        "Pink Carpet",
        "Purple Carpet",
        "Red Carpet",
        "Whiter Carpet",
        "Yellow Carpet",
        "Black Concrete Powder",
        "Blue Concrete Powder",
        "Brown Concrete Powder",
        "Cyan Concrete Powder",
        "Gray Concrete Powder",
        "Green Concrete Powder",
        "light Blue Concrete Powder",
        "Light Gray Concrete Powder",
        "Lime Concrete Powder",
        "Magenta Concrete Powder",
        "Orange Concrete Powder",
        "Pink Concrete Powder",
        "Purple Concrete Powder",
        "Red Concrete Powder",
        "Whiter Concrete Powder",
        "Yellow Concrete Powder",
        "Black Stained Glass",
        "Blue Stained Glass",
        "Brown Stained Glass",
        "Cyan Stained Glass",
        "Gray Stained Glass",
        "Green Stained Glass",
        "light Blue Stained Glass",
        "Light Gray Stained Glass",
        "Lime Stained Glass",
        "Magenta Stained Glass",
        "Orange Stained Glass",
        "Pink Stained Glass",
        "Purple Stained Glass",
        "Red Stained Glass",
        "Whiter Stained Glass",
        "Yellow Stained Glass",
            "Black Stained Glass Plane",
        "Blue Stained Glass Plane",
        "Brown Stained Glass Plane",
        "Cyan Stained Glass Plane",
        "Gray Stained Glass Plane",
        "Green Stained Glass Plane",
        "light Blue Stained Glass Plane",
        "Light Gray Stained Glass Plane",
        "Lime Stained Glass Plane",
        "Magenta Stained Glass Plane",
        "Orange Stained Glass Plane",
        "Pink Stained Glass Plane",
        "Purple Stained Glass Plane",
        "Red Stained Glass Plane",
        "Whiter Stained Glass Plane",
        "Yellow Stained Glass Plane",
        "End Stone Bricks",
        "End Stone Brick Stairs",
        "End Stone Brick Slab",
        "End Stone Brick Wall",
        "Purpur Block",
        "Purpur Pilar",
        "Purpur Stairs",
        "Purpur Slab",
    ]
    return objetos

def obtener_objeto_por_nombre(nombre):
    objetos = {
       "Piston": {"Planks": 3, "CobbleStone": 4, "Iron": 1, "RedStone Dust": 1},
        "Dispenser": {"CobbleStone": 7, "RedStone Dust": 1, "Bow": 1},
        "Arrows": {"Flint": 1, "Sticks": 1,"Feather": 1},
        "Spectral Arrows": {"Glowstone Dust": 4, "Arrows": 1},
        "Crossbow": {"Sticks": 3,"String": 2,"Iron": 1,"Tripwire Hook": 1},
        "Bow": {"Sticks": 3,"String": 3},
        "Wooden Sword": {"Planks": 2, "Palos":1},
        "Stone Sword": {"CobbleStone": 2, "Palos":1},
        "Iron Sword": {"Iron": 2, "Palos":1},
        "Gold Sword": {"Gold": 2, "Palos":1},
        "Diamond Sword": {"Diamonds": 2, "Palos":1},
        "Diamond Helmet": {"Diamonds":5},
        "Golden Helmet": {"Gold":5},
        "Iron Helmet": {"Iron":5},
        "Leather Cap": {"Leather":5},
        "Turtle Shell": {"Scute":5},
        "Diamond Chestplate": {"Diamonds": 8},
        "Golden Chestplate" : {"Gold": 8},
        "Iron Chestplate": {"Iron": 8},
        "Leather Tunic": {"Leather": 8},
        "Diamond Leggings": {"Diamonds" : 7},
        "Golden Leggings": {"Gold" : 7},
        "Iron Leggings": {"Iron" : 7},
        "Leather Pants": {"Leather" : 7},
        "Diamond Boots": {"Diamonds": 4},
        "Golden Boots": {"Gold": 4},
        "Iron Boots": {"Iron": 4},
        "Leather Boots": {"Leather": 4},
        "Diamond Shovel": {"Diamonds": 1,"Sticks":2},
        "Iron Shovel": {"Iron": 1,"Sticks":2},
        "Stone Shovel": {"CobbleStone": 1,"Sticks":2},
        "Wooden Shovel": {"Planks": 1,"Sticks":2},
        "Golden Shovel" : {"Gold": 1,"Sticks":2},
        "Diamond Hoe": {"Diamonds": 2, "Sticks": 2},
        "Iron Hoe": {"Iron": 2, "Sticks": 2},
        "Stone Hoe" :{"CobbleStone": 2, "Sticks": 2},
        "Wooden Hoe":{"Planks": 2, "Sticks": 2},
        "Golden Hoe":{"Golden": 2, "Sticks": 2},
        "Diamond Axe": {"Diamonds": 3,"Sticks": 2},
        "iron Axe": {"Iron": 3,"Sticks": 2},
        "Stone Axe": {"CobbleStone": 3,"Sticks": 2},
        "Wooden Axe": {"Planks": 3,"Sticks": 2},
        "Golden Axe": {"Gold": 3,"Sticks": 2},
        "Diamond Pickaxe": {"Diamonds" : 3, "Sticks": 2},
        "Iron Pickaxe": {"Iron" : 3, "Sticks": 2},
        "Stone Pickaxe": {"CobbleStone" : 3, "Sticks": 2},
        "Wooden Pickaxe": {"Planks" : 3, "Sticks": 2},
        "Golden Pickaxe": {"Gold" : 3, "Sticks": 2},
        "FireWorksLV1": {"Paper": 1, "Gunpowder":1},
        "FireWorksLV2": {"Paper": 1, "Gunpowder":2},
        "FireWorksLV3": {"Paper": 1, "Gunpowder":3},
        "Book": {"Paper": 3, "Leather": 1},
        "Book % Quill": {"Book": 1, "Ink Sac": 1},
        "Carrot on a Stick": {"Fishing Rod": 1, "Carrot": 1},
        "Clock": {"Gold": 4, "RedStone Dust": 1},
        "Compass": {"Iron": 4, "RedStone Dust": 1},
        "Empty Map": {"Compass": 1, "Paper": 8},
        "End Crystal": {"Ghast Taer": 1, "Glass": 7},
        "Fishing Rod": {"Sticks": 3, "String": 2},
        "Flint And Steel": {"Flint": 1, "Iron": 1},
        "Glass Bottle": {"Glass": 3},
        "Lead": {"String": 3, "Slime Ball": 1},
        "Shears": {"Iron": 2},
        "Shield": {"Planks": 6, "Iron": 1},
        "Spyglass": {"Copper Ingot": 2, "Amethyst Shard": 1},
        "Black Firework Star": {"Black Dye": 1,"Gunpowder":1},
        "Blaze Powder": {"Blaze Rod": 1},
        "Blue Firework Star": {"Blue Dye":1,"Gunpowder":1},
        "Bone Meal": {"Bone": 1},
        "Bowl": {"Planks": 3},
        "Brown Firework Star": {"Brown Dye": 1,"GunPowder":1},
        "Cyan Firework Star": {"Cyan Dye": 1,"GunPowder":1},
        "Eye of Ender": {"Ender Pearl": 1,"Blaze Powder":1},
        "Fermented Spider Eye": {"Spider Eye": 1,"Sugar": 1 ,"Brown Mushroom": 1},
        "Fire Charge": {"Gunpowder": 1,"Blaze Powder": 1,"Coal": 1},
        "Glistering Melon": {"Melon Slice":1,"Gold Nuggets":8},
        "Gold Ingot": {"Gold Nuggets":9},
        "Gold Nugget": {"Gold Ingot": 1},
        "Gray Firework Star": {"Gray Dye": 1,"GunPowder":1},
        "Green Firework Star": {"Green Dye": 1,"GunPowder":1},
        "Iron Ingot": {"Iron Nuggets": 9},
        "Iron Nugget": {"Iron Ingot": 1},
        "Light Blue Firework Star": {"Light Blue Dye": 1,"GunPowder":1},
        "light Gray Firework Star": {"Light Gray Dye": 1,"GunPowder":1},
        "Lime Firework Star": {"Lime Dye": 1,"GunPowder":1},
        "Magenta Firework Star": {"Magenta Dye": 1,"GunPowder":1},
        "Netherite Ingot": {"Gold Ingot": 4,"Netherite Scrap": 4},
        "Orange Firework Star": {"Orange Dye": 1,"GunPowder":1},
        "Paper": {"Sugar Cane": 3},
        "Pink Firework Star": {"Pink Dye": 1,"GunPowder":1},
        "Purple Firework Star": {"Purple Dye": 1,"GunPowder":1},
        "Red Firework Star": {"Red Dye": 1,"GunPowder":1},
        "Sugar": {"Sugar Cane": 1},
        "White Firework Star": {"whithe Dye": 1,"GunPowder":1},
        "Yellow Firework Star": {"Yellow Dye": 1,"GunPowder":1},
        "Glow Item Frame": {"Item Frame": 1, "Glow Ink Sac": 1},
        "Item Frame": {"Sticks": 8,"Leather": 1},
        "Painting": {"Sticks": 8,"Wool": 1},
        "Acacia Boat": {"Acacia Planks": 5,},
        "Acacia Boat with Chest": {"Acacia Boat": 1,"Chest":1},
        "Birch Boat": {"Birch Planks": 5,},
        "Birch Boat with Chest": {"Birch Boat": 1,"Chest":1},
        "Dark Oak Boat": {"Dark Oak Planks": 5,},
        "Dark Oak Boat with Chest": {"Dark Oak Boat": 1,"Chest":1},
        "Jungle Boat": {"Jungle Planks": 5,},
        "Jungle Boat with Chest": {"Jungle Boat": 1,"Chest":1},
        "Mangrove Boat": {"Mangrove Planks": 5,},
        "Mangrove Boat with Chest": {"Mangrove Boat": 1,"Chest":1},
        "Oak Boat": {"Oak Planks": 5,},
        "Oak Boat with Chest": {"Oak Boat": 1,"Chest":1},
        "Suprece Boat": {"Suprece Planks": 5,},
        "Suprece Boat with Chest": {"Suprece Boat": 1,"Chest":1},
        "Minecart": {"Iron Ingot": 5},
        "Minecart with Chest": {"Minecart": 1,"Chest":1},
        "Minecart with Furnace": {"Minecart": 1,"Furnace":1},
        "Minecart with Hopper": {"Minecart": 1,"Hopper":1},
        "Minecart with TNT": {"Minecart": 1,"TNT":1},
        "Black Dye": {"Wither Rose": 1,"Ink Sac":1},
        "Blue Dye": {"Lapis Lazuli": 1,"CornFlower":1},
        "Brown Dye": {"Cocoa Beans": 1},
        "Cyan Dye": {"Blue Dye":1,"Green Dye":1},
        "Gray Dye": {"White Dye":1,"Black Dye":1},
        "Light Blue Dye": {"White Dye":1,"BLue Dye":1,"Blue Orchid":1},
        "Light Gray Dye": {"Gray Dye":1,"White Dye":1,"Azure Bluet":1,"Oxeye Daisey":1,"White Tulip":1},
        "Lime Dye": {"Green Dye":1,"White Dye":1},
        "Magenta Dye": {"Pink Dye":1,"Purple Dye":1,"Liac":1,"Allium":1},
        "Orange Dye": {"Yellow Dye":1,"Red Dye":1,"Orange Tulip":1},
        "Pink Dye": {"Red Dye":1,"White Dye":1,"Pink Tulip":1,"Peony":0.5},
        "Purple Dye": {"Blue Dye":1,"Red Dye":1},
        "Red Dye": {"Poppy":1,"Rose Bush":0.5,"Red Tulip":1},
        "White Dye": {"Bone Meal":1},
        "Yellow Dye": {"Dandelion":1,"Sunflower":0.5},
        "Oak Door": {"Oak Planks": 6},
        "Oak Wood": {"Oak Log": 4},
        "Oak Fence": {"Oak planks":4,"Sticks":2},
        "Oak Fence Gate": {"Oak planks":2,"Sticks":4},
        "Oak Sign": {"Oak planks":6,"Sticks":1},
        "Oak Slab": {"Oak planks":3},
        "Oak Stairs": {"Oak planks":6},
        "Oak Trapdoor": {"Oak planks":6},
        "Stripped Oak Wood": {"Stripped Oak Log":4},
        "Oak Planks": {"Oak Log":1},
         "Spruce Door": {"Spruce Planks": 6},
        "Spruce Wood": {"Spruce Log": 4},
        "Spruce Fence": {"Spruce planks":4,"Sticks":2},
        "Spruce Fence Gate": {"Spruce planks":2,"Sticks":4},
        "Spruce Sign": {"Spruce planks":6,"Sticks":1},
        "Spruce Slab": {"Spruce planks":3},
        "Spruce Stairs": {"Spruce planks":6},
        "Spruce Trapdoor": {"Spruce planks":6},
        "Stripped Spruce Wood": {"Stripped Spruce Log":4},
        "Spruce Planks": {"Spruce Log":1},
         "Mangrove Door": {"Mangrove Planks": 6},
        "Mangrove Wood": {"Mangrove Log": 4},
        "Mangrove Fence": {"Mangrove planks":4,"Sticks":2},
        "Mangrove Fence Gate": {"Mangrove planks":2,"Sticks":4},
        "Mangrove Sign": {"Mangrove planks":6,"Sticks":1},
        "Mangrove Slab": {"Mangrove planks":3},
        "Mangrove Stairs": {"Mangrove planks":6},
        "Mangrove Trapdoor": {"Mangrove planks":6},
        "Stripped Mangrove Wood": {"Stripped Mangrove Log":4},
        "Mangrove Planks": {"Mangrove Log":1},
         "Jungle Door": {"Jungle Planks": 6},
        "Jungle Wood": {"Jungle Log": 4},
        "Jungle Fence": {"Jungle planks":4,"Sticks":2},
        "Jungle Fence Gate": {"Jungle planks":2,"Sticks":4},
        "Jungle Sign": {"Jungle planks":6,"Sticks":1},
        "Jungle Slab": {"Jungle planks":3},
        "Jungle Stairs": {"Jungle planks":6},
        "Jungle Trapdoor": {"Jungle planks":6},
        "Stripped Jungle Wood": {"Stripped Jungle Log":4},
        "Jungle Planks": {"Jungle Log":1},
            "Dark Oak Door": {"Dark Oak Planks": 6},
        "Dark Oak Wood": {"Dark Oak Log": 4},
        "Dark Oak Fence": {"Dark Oak planks":4,"Sticks":2},
        "Dark Oak Fence Gate": {"Dark Oak planks":2,"Sticks":4},
        "Dark Oak Sign": {"Dark Oak planks":6,"Sticks":1},
        "Dark Oak Slab": {"Dark Oak planks":3},
        "Dark Oak Stairs": {"Dark Oak planks":6},
        "Dark Oak Trapdoor": {"Dark Oak planks":6},
        "Stripped Dark Oak Wood": {"Stripped Dark Oak Log":4},
        "Dark Oak Planks": {"Dark Oak Log":1},
            "Birch Door": {"Birch Planks": 6},
        "Birch Wood": {"Birch Log": 4},
        "Birch Fence": {"Birch planks":4,"Sticks":2},
        "Birch Fence Gate": {"Birch planks":2,"Sticks":4},
        "Birch Sign": {"Birch planks":6,"Sticks":1},
        "Birch Slab": {"Birch planks":3},
        "Birch Stairs": {"Birch planks":6},
        "Birch Trapdoor": {"Birch planks":6},
        "Stripped Birch Wood": {"Stripped Birch Log":4},
        "Birch Planks": {"Birch Log":1},
            "Acacia Door": {"Acacia Planks": 6},
        "Acacia Wood": {"Acacia Log": 4},
        "Acacia Fence": {"Acacia planks":4,"Sticks":2},
        "Acacia Fence Gate": {"Acacia planks":2,"Sticks":4},
        "Acacia Sign": {"Acacia planks":6,"Sticks":1},
        "Acacia Slab": {"Acacia planks":3},
        "Acacia Stairs": {"Acacia planks":6},
        "Acacia Trapdoor": {"Acacia planks":6},
        "Stripped Acacia Wood": {"Stripped Acacia Log":4},
        "Acacia Planks": {"Acacia Log":1},
        "Blue Ice": {"Packed Ice":9},
        "Packed Ice": {"Ice":9},
        "Snow Block": {"Snow Balls":4},
        "Dried Kelp Block": {"Dried Kelp":9},
        "Dark Prismarine": {"Prismarine Shard":8,"Ink Sac":1},
        "Dark Prismarine Slab": {"Dark Prismarine":3},
        "Dark Prismarine Stairs": {"Dark Prismarine":6},
        "Prismarine": {"Prismarine Shard":4},
        "Prismarine Brick Slab": {"Prismarine Bricks":3},
        "Prismarine Brick Stairs": {"Prismarine Bricks":6},
        "Prismarine Bricks": {"Prismarine Shard":9},
        "Prismarine Slab": {"Primarine":3},
        "Prismarine Stairs": {"Primarine":6},
        "Prismarine Wall": {"Prismarine":6},
        "Black Banner":{"Black Woll":6,"Sticks":1},
        "Blue Banner":{"Blue Woll":6,"Sticks":1},
        "Brown Banner":{"Brown Woll":6,"Sticks":1},
        "Cyan Banner":{"Cyan Woll":6,"Sticks":1},
        "Gray Banner":{"Gray Woll":6,"Sticks":1},
        "Green Banner":{"Green Woll":6,"Sticks":1},
        "light Blue Banner":{"Light Blue Woll":6,"Sticks":1},
        "Light Gray Banner":{"Light Gray Woll":6,"Sticks":1},
        "Lime Banner":{"Lime Woll":6,"Sticks":1},
        "Magenta Banner":{"Magenta Woll":6,"Sticks":1},
        "Orange Banner":{"Orange Woll":6,"Sticks":1},
        "Pink Banner":{"Pink Woll":6,"Sticks":1},
        "Purple Banner":{"Purple Woll":6,"Sticks":1},
        "Red Banner":{"Red Woll":6,"Sticks":1},
        "White Banner":{"Withe Woll":6,"Sticks":1},
        "Yellow Banner":{"White Woll":6,"Sticks":1},
        "Black Wool": {"white Wool":1,"Black Dye":1},
        "Blue Wool": {"white Wool":1,"Blue Dye":1},
        "Brown Wool": {"white Wool":1,"Brown Dye":1},
        "Cyan Wool": {"white Wool":1,"Cyan Dye":1},
        "Gray Wool": {"white Wool":1,"Gray Dye":1},
        "Green Wool": {"white Wool":1,"Greem Dye":1},
        "light Blue Wool": {"white Wool":1,"Light Blue Dye":1},
        "Light Gray Wool": {"white Wool":1,"Light Gray Dye":1},
        "Lime Wool": {"white Wool":1,"Lime Dye":1},
        "Magenta Wool": {"white Wool":1,"Magenta Dye":1},
        "Orange Wool": {"white Wool":1,"Orange Dye":1},
        "Pink Wool": {"white Wool":1,"Pink Dye":1},
        "Purple Wool": {"white Wool":1,"Purple Dye":1},
        "Red Wool": {"white Wool":1,"Red Dye":1},
        "Yellow Wool": {"white Wool":1,"Yellow Dye":1},
        "Black Carpet": {"Black Wool":2},
        "Blue Carpet": {"Blue Wool":2},
        "Brown Carpet": {"Brown Wool":2},
        "Cyan Carpet": {"Cyan Wool":2},
        "Gray Carpet": {"Gray Wool":2},
        "Green Carpet": {"Green Wool":2},
        "light Blue Carpet": {"Light Blue Wool":2},
        "Light Gray Carpet": {"Light Gray Wool":2},
        "Lime Carpet": {"Lime Wool":2},
        "Magenta Carpet": {"Magenta Wool":2},
        "Orange Carpet": {"Orange Wool":2},
        "Pink Carpet": {"Pink Wool":2},
        "Purple Carpet": {"Purple Wool":2},
        "Red Carpet": {"Red Wool":2},
        "Whiter Carpet": {"White Wool":2},
        "Yellow Carpet": {"Yellow Wool":2},
        "Black Concrete Powder": {"Sand":4,"Gravel":4,"Black Dye":1},
        "Blue Concrete Powder": {"Sand":4,"Gravel":4,"Blue Dye":1},
        "Brown Concrete Powder": {"Sand":4,"Gravel":4,"Brown Dye":1},
        "Cyan Concrete Powder": {"Sand":4,"Gravel":4,"cyan Dye":1},
        "Gray Concrete Powder": {"Sand":4,"Gravel":4,"Gray Dye":1},
        "Green Concrete Powder": {"Sand":4,"Gravel":4,"Green Dye":1},
        "light Blue Concrete Powder": {"Sand":4,"Gravel":4,"Light Blue Dye":1},
        "Light Gray Concrete Powder": {"Sand":4,"Gravel":4,"Light Gray Dye":1},
        "Lime Concrete Powder": {"Sand":4,"Gravel":4,"Lime Dye":1},
        "Magenta Concrete Powder": {"Sand":4,"Gravel":4,"Magenta Dye":1},
        "Orange Concrete Powder": {"Sand":4,"Gravel":4,"Orange Dye":1},
        "Pink Concrete Powder": {"Sand":4,"Gravel":4,"Pink Dye":1},
        "Purple Concrete Powder": {"Sand":4,"Gravel":4,"Purple Dye":1},
        "Red Concrete Powder": {"Sand":4,"Gravel":4,"Red Dye":1},
        "Whiter Concrete Powder": {"Sand":4,"Gravel":4,"White Dye":1},
        "Yellow Concrete Powder": {"Sand":4,"Gravel":4,"Yellow Dye":1},
        "Black Stained Glass": {"Glass":8,"Black Dye":1},
        "Blue Stained Glass": {"Glass":8,"Blue Dye":1},
        "Brown Stained Glass": {"Glass":8,"Brown Dye":1},
        "Cyan Stained Glass": {"Glass":8,"Cyan Dye":1},
        "Gray Stained Glass": {"Glass":8,"Gray Dye":1},
        "Green Stained Glass": {"Glass":8,"Green Dye":1},
        "light Blue Stained Glass": {"Glass":8,"Light Blue Dye":1},
        "Light Gray Stained Glass": {"Glass":8,"Light Gray Dye":1},
        "Lime Stained Glass": {"Glass":8,"Lime Dye":1},
        "Magenta Stained Glass": {"Glass":8,"Magenta Dye":1},
        "Orange Stained Glass": {"Glass":8,"Orange Dye":1},
        "Pink Stained Glass": {"Glass":8,"Pink Dye":1},
        "Purple Stained Glass": {"Glass":8,"Purple Dye":1},
        "Red Stained Glass": {"Glass":8,"Red Dye":1},
        "Whiter Stained Glass": {"Glass":8,"White Dye":1},
        "Yellow Stained Glass": {"Glass":8,"Yellow Dye":1},
        "Black Stained Glass Plane": {"Black Stained Glass":6},
        "Blue Stained Glass Plane": {"Blue Stained Glass":6},
        "Brown Stained Glass Plane": {"Brown Stained Glass":6},
        "Cyan Stained Glass Plane": {"Cyan Stained Glass":6},
        "Gray Stained Glass Plane": {"Gray Stained Glass":6},
        "Green Stained Glass Plane": {"Green Stained Glass":6},
        "light Blue Stained Glass Plane": {"Light Blue Stained Glass":6},
        "Light Gray Stained Glass Plane": {"Light Gray Stained Glass":6},
        "Lime Stained Glass Plane": {"Lime Stained Glass":6},
        "Magenta Stained Glass Plane": {"Magenta Stained Glass":6},
        "Orange Stained Glass Plane": {"Orange Stained Glass":6},
        "Pink Stained Glass Plane": {"Pink Stained Glass":6},
        "Purple Stained Glass Plane": {"Purple Stained Glass":6},
        "Red Stained Glass Plane": {"Red Stained Glass":6},
        "Whiter Stained Glass Plane": {"White Stained Glass":6},
        "Yellow Stained Glass Plane": {"Yellow Stained Glass":6},
        "End Stone Bricks": {"End Stone":1},
        "End Stone Brick Stairs": {"End Stone Bricks":6},
        "End Stone Brick Slab": {"End Stone Bricks":3},
        "End Stone Brick Wall": {"End Stone Bricks":6},
        "Purpur Block": {"Popped Chorus Fruit":1},
        "Purpur Pilar": {"Purpur Block":1},
        "Purpur Stairs": {"Purpur Block":6},
        "Purpur Slab": {"Purpur Block":3},

        # Agrega más objetos según sea necesario
    }
    if nombre in objetos:
        if nombre == "Oak Wood":
            return ObjetoEspecial(nombre, objetos[nombre], mensaje_extra=("¡this item may have surplus!"))
        if nombre == "Stripped Oak Wood":
            return ObjetoEspecial(nombre, objetos[nombre], mensaje_extra=("¡this item may have surplus!"))
        if nombre == "Acacia Wood":
            return ObjetoEspecial(nombre, objetos[nombre], mensaje_extra=("¡this item may have surplus!"))
        if nombre == "Stripped Acacia Wood":
            return ObjetoEspecial(nombre, objetos[nombre], mensaje_extra=("¡this item may have surplus!"))
        if nombre == "Birch Wood":
            return ObjetoEspecial(nombre, objetos[nombre], mensaje_extra=("¡this item may have surplus!"))
        if nombre == "Stripped Birch Wood":
            return ObjetoEspecial(nombre, objetos[nombre], mensaje_extra=("¡this item may have surplus!"))
        if nombre == "Dark Oak Wood":
            return ObjetoEspecial(nombre, objetos[nombre], mensaje_extra=("¡this item may have surplus!"))
        if nombre == "Stripped Dark Oak Wood":
            return ObjetoEspecial(nombre, objetos[nombre], mensaje_extra=("¡this item may have surplus!"))
        if nombre == "Spruce Wood":
            return ObjetoEspecial(nombre, objetos[nombre], mensaje_extra=("¡this item may have surplus!"))
        if nombre == "Stripped Spruce Wood":
            return ObjetoEspecial(nombre, objetos[nombre], mensaje_extra=("¡this item may have surplus!"))
        if nombre == "Mangrove Wood":
            return ObjetoEspecial(nombre, objetos[nombre], mensaje_extra=("¡this item may have surplus!"))
        if nombre == "Stripped Mangrove Wood":
            return ObjetoEspecial(nombre, objetos[nombre], mensaje_extra=("¡this item may have surplus!"))
        if nombre == "Jungle Wood":
            return ObjetoEspecial(nombre, objetos[nombre], mensaje_extra=("¡this item may have surplus!"))
        if nombre == "Stripped Jungle Wood":
            return ObjetoEspecial(nombre, objetos[nombre], mensaje_extra=("¡this item may have surplus!"))
        elif nombre == "Arrows":
            return ObjetoDividirEntreCuatro(nombre, objetos[nombre])
        elif nombre == "Oak Planks":
            return ObjetoDividirEntreCuatro(nombre, objetos[nombre])
        elif nombre == "Acacia Planks":
            return ObjetoDividirEntreCuatro(nombre, objetos[nombre])
        elif nombre == "Birch Planks":
            return ObjetoDividirEntreCuatro(nombre, objetos[nombre])
        elif nombre == "Dark Oak Planks":
            return ObjetoDividirEntreCuatro(nombre, objetos[nombre])
        elif nombre == "Spruce Planks":
            return ObjetoDividirEntreCuatro(nombre, objetos[nombre])
        elif nombre == "Mangrove Planks":
            return ObjetoDividirEntreCuatro(nombre, objetos[nombre])
        elif nombre == "Jungle Planks":
            return ObjetoDividirEntreCuatro(nombre, objetos[nombre])
        elif nombre == "Oak Stairs":
            return ObjetoDividirEntreCuatro(nombre, objetos[nombre])
        elif nombre == "Prismarine Stairs":
            return ObjetoDividirEntreCuatro(nombre, objetos[nombre])
        elif nombre == "Acacia Stairs":
            return ObjetoDividirEntreCuatro(nombre, objetos[nombre])
        elif nombre == "Birch Stairs":
            return ObjetoDividirEntreCuatro(nombre, objetos[nombre])
        elif nombre == "Dark Oak Stairs":
            return ObjetoDividirEntreCuatro(nombre, objetos[nombre])
        elif nombre == "Spruce Stairs":
            return ObjetoDividirEntreCuatro(nombre, objetos[nombre])
        elif nombre == "Mangrove Stairs":
            return ObjetoDividirEntreCuatro(nombre, objetos[nombre])
        elif nombre == "Jungle Stairs":
            return ObjetoDividirEntreCuatro(nombre, objetos[nombre])
        elif nombre == "Purpur Stairs":
            return ObjetoDividirEntreCuatro(nombre, objetos[nombre])
        elif nombre == "Spectral Arrows":
            return ObjetoDividirEntreDos(nombre, objetos[nombre])
        elif nombre == "Blaze Rod":
            return ObjetoDividirEntreDos(nombre, objetos[nombre])
        elif nombre == "Bone Meal":
            return ObjetoDividirEntreTres(nombre, objetos[nombre])
        elif nombre == "Oak Sign":
            return ObjetoDividirEntreTres(nombre, objetos[nombre])
        elif nombre == "Oak Fence":
            return ObjetoDividirEntreTres(nombre, objetos[nombre])
        elif nombre == "Acacia Sign":
            return ObjetoDividirEntreTres(nombre, objetos[nombre])
        elif nombre == "Acacia Fence":
            return ObjetoDividirEntreTres(nombre, objetos[nombre])
        elif nombre == "Birch Sign":
            return ObjetoDividirEntreTres(nombre, objetos[nombre])
        elif nombre == "Birch Fence":
            return ObjetoDividirEntreTres(nombre, objetos[nombre])
        elif nombre == "Dark Oak Sign":
            return ObjetoDividirEntreTres(nombre, objetos[nombre])
        elif nombre == "Dark Oak Fence":
            return ObjetoDividirEntreTres(nombre, objetos[nombre])
        elif nombre == "Mangrove Sign":
            return ObjetoDividirEntreTres(nombre, objetos[nombre])
        elif nombre == "Mangrove Fence":
            return ObjetoDividirEntreTres(nombre, objetos[nombre])
        elif nombre == "Spruce Sign":
            return ObjetoDividirEntreTres(nombre, objetos[nombre])
        elif nombre == "Spruce Fence":
            return ObjetoDividirEntreTres(nombre, objetos[nombre])
        elif nombre == "Jungle Sign":
            return ObjetoDividirEntreTres(nombre, objetos[nombre])
        elif nombre == "Jungle Fence":
            return ObjetoDividirEntreTres(nombre, objetos[nombre])
        elif nombre == "Gold Nugget":
            return ObjetoDividirEntreNueve(nombre, objetos[nombre], mensaje_extra=("¡if the quantity to be crafted is less than 9 mark zero!"))
        elif nombre == "Iron Nugget":
            return ObjetoDividirEntreNueve(nombre, objetos[nombre], mensaje_extra=("¡if the quantity to be crafted is less than 9 mark zero!"))
        elif nombre == "Red Dye":
            return ObjetoImportante(nombre, objetos[nombre], mensaje_extra=("¡Any type of flower will work independently for red dyeing and all three are not necessary.!"))
        elif nombre == "Light Gray Dye":
            return ObjetoImportante(nombre, objetos[nombre], mensaje_extra=("¡light gray dye can be obtained by combining gray and white dye or with any type of flower.!"))
        elif nombre == "Yellow Dye":
            return ObjetoImportante(nombre, objetos[nombre], mensaje_extra=("!Sunflower has been configured in such a way that it is possible that it will not display the required number if the required number is not even, I will be working to find a way to display a more accurate answer.¡"))
        elif nombre == "Oak Slab":
            return ObjetoDividirEntreSeis(nombre, objetos[nombre])
        elif nombre == "Purpur Slab":
            return ObjetoDividirEntreSeis(nombre, objetos[nombre])
        elif nombre == "Acacia Slab":
            return ObjetoDividirEntreSeis(nombre, objetos[nombre])
        elif nombre == "Birch Slab":
            return ObjetoDividirEntreSeis(nombre, objetos[nombre])
        elif nombre == "Spruce Slab":
            return ObjetoDividirEntreSeis(nombre, objetos[nombre])
        elif nombre == "Mangrove Slab":
            return ObjetoDividirEntreSeis(nombre, objetos[nombre])
        elif nombre == "Jungle Slab":
            return ObjetoDividirEntreSeis(nombre, objetos[nombre])
        elif nombre == "Dark Oak Slab":
            return ObjetoDividirEntreSeis(nombre, objetos[nombre])
        elif nombre == "Prismarine Slab":
            return ObjetoDividirEntreSeis(nombre, objetos[nombre])
        elif nombre == "Prismarine Wall":
            return ObjetoDividirEntreSeis(nombre, objetos[nombre])
        elif nombre == "Black Carpet":
            return ObjetoDividirEntreTres(nombre, objetos[nombre])
        elif nombre == "Blue Carpet":
            return ObjetoDividirEntreTres(nombre, objetos[nombre])
        elif nombre == "Brown Carpet":
            return ObjetoDividirEntreTres(nombre, objetos[nombre])
        elif nombre == "Cyan Carpet":
            return ObjetoDividirEntreTres(nombre, objetos[nombre])
        elif nombre == "Gray Carpet":
            return ObjetoDividirEntreTres(nombre, objetos[nombre])
        elif nombre == "Green Carpet":
            return ObjetoDividirEntreTres(nombre, objetos[nombre])
        elif nombre == "light Blue Carpet":
            return ObjetoDividirEntreTres(nombre, objetos[nombre])
        elif nombre == "Light Gray Carpet":
            return ObjetoDividirEntreTres(nombre, objetos[nombre])
        elif nombre == "Lime Carpet":
            return ObjetoDividirEntreTres(nombre, objetos[nombre])
        elif nombre == "Magenta Carpet":
            return ObjetoDividirEntreTres(nombre, objetos[nombre])
        elif nombre == "Orange Carpet":
            return ObjetoDividirEntreTres(nombre, objetos[nombre])
        elif nombre == "Pink Carpet":
            return ObjetoDividirEntreTres(nombre, objetos[nombre])
        elif nombre == "Purple Carpet":
            return ObjetoDividirEntreTres(nombre, objetos[nombre])
        elif nombre == "Red Carpet":
            return ObjetoDividirEntreTres(nombre, objetos[nombre])
        elif nombre == "Whiter Carpet":
            return ObjetoDividirEntreTres(nombre, objetos[nombre])
        elif nombre == "Yellow Carpet":
            return ObjetoDividirEntreTres(nombre, objetos[nombre])
        elif nombre == "Black Concrete Powder":
            return ObjetoDividirEntreOcho(nombre, objetos[nombre])
        elif nombre == "Blue Concrete Powder":
            return ObjetoDividirEntreOcho(nombre, objetos[nombre])
        elif nombre == "Brown Concrete Powder":
            return ObjetoDividirEntreOcho(nombre, objetos[nombre])
        elif nombre == "Cyan Concrete Powder":
            return ObjetoDividirEntreOcho(nombre, objetos[nombre])
        elif nombre == "Gray Concrete Powder":
            return ObjetoDividirEntreOcho(nombre, objetos[nombre])
        elif nombre == "Green Concrete Powder":
            return ObjetoDividirEntreOcho(nombre, objetos[nombre])
        elif nombre == "light Blue Concrete Powder":
            return ObjetoDividirEntreOcho(nombre, objetos[nombre])
        elif nombre == "Light Gray Concrete Powder":
            return ObjetoDividirEntreOcho(nombre, objetos[nombre])
        elif nombre == "Lime Concrete Powder":
            return ObjetoDividirEntreOcho(nombre, objetos[nombre])
        elif nombre == "Magenta Concrete Powder":
            return ObjetoDividirEntreOcho(nombre, objetos[nombre])
        elif nombre == "Orange Concrete Powder":
            return ObjetoDividirEntreOcho(nombre, objetos[nombre])
        elif nombre ==  "Pink Concrete Powder":
            return ObjetoDividirEntreOcho(nombre, objetos[nombre])
        elif nombre == "Purple Concrete Powder":
            return ObjetoDividirEntreOcho(nombre, objetos[nombre])
        elif nombre == "Red Concrete Powder":
            return ObjetoDividirEntreOcho(nombre, objetos[nombre])
        elif nombre == "Whiter Concrete Powder":
            return ObjetoDividirEntreOcho(nombre, objetos[nombre])
        elif nombre == "Yellow Concrete Powder":
            return ObjetoDividirEntreOcho(nombre, objetos[nombre])
        elif nombre == "Black Stained Glass":
            return ObjetoDividirEntreOcho(nombre, objetos[nombre])
        elif nombre == "Blue Stained Glass":
            return ObjetoDividirEntreOcho(nombre, objetos[nombre])
        elif nombre == "Brown Stained Glass":
            return ObjetoDividirEntreOcho(nombre, objetos[nombre])
        elif nombre == "Cyan Stained Glass":
            return ObjetoDividirEntreOcho(nombre, objetos[nombre])
        elif nombre == "Gray Stained Glass":
            return ObjetoDividirEntreOcho(nombre, objetos[nombre])
        elif nombre == "Green Stained Glass":
            return ObjetoDividirEntreOcho(nombre, objetos[nombre])
        elif nombre == "light Blue Stained Glass":
            return ObjetoDividirEntreOcho(nombre, objetos[nombre])
        elif nombre == "Light Gray Stained Glass":
            return ObjetoDividirEntreOcho(nombre, objetos[nombre])
        elif nombre == "Lime Stained Glass":
            return ObjetoDividirEntreOcho(nombre, objetos[nombre])
        elif nombre == "Magenta Stained Glass":
            return ObjetoDividirEntreOcho(nombre, objetos[nombre])
        elif nombre == "Orange Stained Glass":
            return ObjetoDividirEntreOcho(nombre, objetos[nombre])
        elif nombre == "Pink Stained Glass":
            return ObjetoDividirEntreOcho(nombre, objetos[nombre])
        elif nombre == "Purple Stained Glass":
            return ObjetoDividirEntreOcho(nombre, objetos[nombre])
        elif nombre == "Red Stained Glass":
            return ObjetoDividirEntreOcho(nombre, objetos[nombre])
        elif nombre == "Whiter Stained Glass":
            return ObjetoDividirEntreOcho(nombre, objetos[nombre])
        elif nombre == "Yellow Stained Glass":
            return ObjetoDividirEntreOcho(nombre, objetos[nombre])
        elif nombre == "Black Stained Glass Plane":
            return ObjetoDividirEntreDiezYSeis(nombre, objetos[nombre], mensaje_extra=("¡the crystal panel crafting implemented is that of the 6 crystal blocks, for the moment this is the only way of crafting the panels, later the panel dyeing crafting will be added.!"))
        elif nombre == "Blue Stained Glass Plane":
            return ObjetoDividirEntreDiezYSeis(nombre, objetos[nombre], mensaje_extra=("¡the crystal panel crafting implemented is that of the 6 crystal blocks, for the moment this is the only way of crafting the panels, later the panel dyeing crafting will be added.!"))
        elif nombre == "Brown Stained Glass Plane":
            return ObjetoDividirEntreDiezYSeis(nombre, objetos[nombre], mensaje_extra=("¡the crystal panel crafting implemented is that of the 6 crystal blocks, for the moment this is the only way of crafting the panels, later the panel dyeing crafting will be added.!"))
        elif nombre == "Cyan Stained Glass Plane":
            return ObjetoDividirEntreDiezYSeis(nombre, objetos[nombre], mensaje_extra=("¡the crystal panel crafting implemented is that of the 6 crystal blocks, for the moment this is the only way of crafting the panels, later the panel dyeing crafting will be added.!"))
        elif nombre == "Gray Stained Glass Plane":
            return ObjetoDividirEntreDiezYSeis(nombre, objetos[nombre], mensaje_extra=("¡the crystal panel crafting implemented is that of the 6 crystal blocks, for the moment this is the only way of crafting the panels, later the panel dyeing crafting will be added.!"))
        elif nombre == "Green Stained Glass Plane":
            return ObjetoDividirEntreDiezYSeis(nombre, objetos[nombre], mensaje_extra=("¡the crystal panel crafting implemented is that of the 6 crystal blocks, for the moment this is the only way of crafting the panels, later the panel dyeing crafting will be added.!"))
        elif nombre == "light Blue Stained Glass Plane":
            return ObjetoDividirEntreDiezYSeis(nombre, objetos[nombre], mensaje_extra=("¡the crystal panel crafting implemented is that of the 6 crystal blocks, for the moment this is the only way of crafting the panels, later the panel dyeing crafting will be added.!"))
        elif nombre == "Light Gray Stained Glass Plane":
            return ObjetoDividirEntreDiezYSeis(nombre, objetos[nombre], mensaje_extra=("¡the crystal panel crafting implemented is that of the 6 crystal blocks, for the moment this is the only way of crafting the panels, later the panel dyeing crafting will be added.!"))
        elif nombre == "Lime Stained Glass Plane":
            return ObjetoDividirEntreDiezYSeis(nombre, objetos[nombre], mensaje_extra=("¡the crystal panel crafting implemented is that of the 6 crystal blocks, for the moment this is the only way of crafting the panels, later the panel dyeing crafting will be added.!"))
        elif nombre == "Magenta Stained Glass Plane":
            return ObjetoDividirEntreDiezYSeis(nombre, objetos[nombre], mensaje_extra=("¡the crystal panel crafting implemented is that of the 6 crystal blocks, for the moment this is the only way of crafting the panels, later the panel dyeing crafting will be added.!"))
        elif nombre == "Orange Stained Glass Plane":
            return ObjetoDividirEntreDiezYSeis(nombre, objetos[nombre], mensaje_extra=("¡the crystal panel crafting implemented is that of the 6 crystal blocks, for the moment this is the only way of crafting the panels, later the panel dyeing crafting will be added.!"))
        elif nombre == "Pink Stained Glass Plane":
            return ObjetoDividirEntreDiezYSeis(nombre, objetos[nombre], mensaje_extra=("¡the crystal panel crafting implemented is that of the 6 crystal blocks, for the moment this is the only way of crafting the panels, later the panel dyeing crafting will be added.!"))
        elif nombre == "Purple Stained Glass Plane":
            return ObjetoDividirEntreDiezYSeis(nombre, objetos[nombre], mensaje_extra=("¡the crystal panel crafting implemented is that of the 6 crystal blocks, for the moment this is the only way of crafting the panels, later the panel dyeing crafting will be added.!"))
        elif nombre == "Red Stained Glass Plane":
            return ObjetoDividirEntreDiezYSeis(nombre, objetos[nombre], mensaje_extra=("¡the crystal panel crafting implemented is that of the 6 crystal blocks, for the moment this is the only way of crafting the panels, later the panel dyeing crafting will be added.!"))
        elif nombre == "Whiter Stained Glass Plane":
            return ObjetoDividirEntreDiezYSeis(nombre, objetos[nombre], mensaje_extra=("¡the crystal panel crafting implemented is that of the 6 crystal blocks, for the moment this is the only way of crafting the panels, later the panel dyeing crafting will be added.!"))
        elif nombre == "Yellow Stained Glass Plane":
            return ObjetoDividirEntreDiezYSeis(nombre, objetos[nombre], mensaje_extra=("¡the crystal panel crafting implemented is that of the 6 crystal blocks, for the moment this is the only way of crafting the panels, later the panel dyeing crafting will be added.!"))
        else:
            return Objeto(nombre, objetos[nombre]) 
    else:
        return None
    

def calcular_objeto():
    nombre_objeto = nombre_seleccionado.get()
    cantidad = int(entry_cantidad.get())

    objeto = obtener_objeto_por_nombre(nombre_objeto)
    if objeto:
        objeto.multiplicar_caracteristicas(cantidad)
        resultado.config(text=str(objeto))
        historial.append(str(objeto))
        actualizar_historial()
    else:
        messagebox.showerror("Error", "The Item is not found in the database, try to verify the name, look for it in the list of items, if it is not found ask for it to be added in new versions. ;( ")

def actualizar_historial():
    historial_texto.config(state=tk.NORMAL)
    historial_texto.delete('1.0', tk.END)
    for item in historial:
        historial_texto.insert(tk.END, item + "\n\n")
    historial_texto.config(state=tk.DISABLED)

def copiar_historial():
    root.clipboard_clear()
    root.clipboard_append(historial_texto.get('1.0', tk.END))

def cambiar_color():
    color = colorchooser.askcolor(title="Select a color")
    if color:
        root.config(bg=color[1])

#def agregar_objeto():
 #   nombre = entry_nombre_objeto.get()
  #  caracteristicas = eval(entry_caracteristicas_objeto.get())
   # objetos.append(Objeto(nombre, caracteristicas))
    #combo_objetos['values'] = obtener_nombres_objetos()
    #ombo_objetos.current(len(objetos) - 1)

# Crear ventana principal
root = tk.Tk()
root.title("CraftingCalculator")
root.config(bg=("#3a6955"))
root.iconbitmap("C:\\Users\\juahj\\py\\icon.ico")

# Obtener nombres de objetos disponibles
objetos = []

# Crear etiquetas y entradas
label_nombre = tk.Label(root, text="Item to Craft:", font=("ComicSans", 13))
label_nombre.grid(row=0, column=0, padx=5, pady=5)
nombre_seleccionado = tk.StringVar(root)
nombre_seleccionado.set(obtener_nombres_objetos()[0])
combo_objetos = ttk.Combobox(root, textvariable=nombre_seleccionado, values=obtener_nombres_objetos())
combo_objetos.grid(row=0, column=1, padx=5, pady=5)

label_cantidad = tk.Label(root, text="Quantity to be created:", font=("ComicSans", 13))
label_cantidad.grid(row=1, column=0, padx=5, pady=5)
entry_cantidad = tk.Entry(root, width=20, font=("ComicSans", 13))
entry_cantidad.grid(row=1, column=1, padx=5, pady=5)

# Botón para calcular
button_calcular = tk.Button(root, text="Calculate", command=calcular_objeto, font=("ComicSans", 13))
button_calcular.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

# Etiqueta para mostrar el resultado
resultado = tk.Label(root, text="", font=("ComicSans", 13))
resultado.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Botón y área de texto para historial
historial = []
historial_frame = tk.Frame(root)
historial_frame.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

historial_texto = tk.Text(historial_frame, wrap=tk.WORD, height=10, width=40, font=("ComicSans", 13))
historial_texto.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
historial_texto.config(state=tk.DISABLED)

scrollbar = tk.Scrollbar(historial_frame, command=historial_texto.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

button_copiar = tk.Button(root, text="Copy Calculations", command=copiar_historial, font=("ComicSans", 13))
button_copiar.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

 #Botón para cambiar el color de la ventana
button_color = tk.Button(root, text="Change Color", command=cambiar_color)
button_color.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Etiqueta y entrada para agregar un nuevo objeto
#label_nuevo_objeto = tk.Label(root, text="Nuevo Objeto:", font=("ComicSans", 13))
#label_nuevo_objeto.grid(row=7, column=0, padx=5, pady=5)
#entry_nombre_objeto = tk.Entry(root, font=("ComicSans", 13))
#entry_nombre_objeto.grid(row=7, column=1, padx=5, pady=5)

#label_caracteristicas_objeto = tk.Label(root, text="Características (dict):", font=("ComicSans", 13))
#label_caracteristicas_objeto.grid(row=8, column=0, padx=5, pady=5)
#entry_caracteristicas_objeto = tk.Entry(root, font=("ComicSans", 13))
#entry_caracteristicas_objeto.grid(row=8, column=1, padx=5, pady=5)

#button_agregar_objeto = tk.Button(root, text="Agregar Objeto", command=agregar_objeto, font=("ComicSans", 13))
#button_agregar_objeto.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

# Ejecutar la aplicación
root.mainloop()
