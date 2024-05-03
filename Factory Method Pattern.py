# Factory Method Pattern

# Character classes
class Character:
    def __init__(self, name):
        self.name = name
        self.appearance = None
        self.abilities = []
        self.equipment = []
        self.attributes = {}


class CharacterFactory:
    def create_character(self, name):
        pass


class WarriorFactory(CharacterFactory):
    def create_character(self, name):
        character = Character(name)
        character.appearance = "Warrior's appearance"
        character.abilities = ["Warrior's abilities"]
        character.equipment = ["Warrior's equipment"]
        character.attributes = {"Strength": 10, "Defense": 8}
        return character


class MageFactory(CharacterFactory):
    def create_character(self, name):
        character = Character(name)
        character.appearance = "Mage's appearance"
        character.abilities = ["Mage's abilities"]
        character.equipment = ["Mage's equipment"]
        character.attributes = {"Intelligence": 10, "Mana": 100}
        return character


class ArcherFactory(CharacterFactory):
    def create_character(self, name):
        character = Character(name)
        character.appearance = "Archer's appearance"
        character.abilities = ["Archer's abilities"]
        character.equipment = ["Archer's equipment"]
        character.attributes = {"Dexterity": 10, "Accuracy": 8}
        return character


class CharacterCreator:
    def __init__(self):
        self.factory = None

    def set_factory(self, factory):
        self.factory = factory

    def create_character(self, name):
        if self.factory:
            return self.factory.create_character(name)


# Data processing modules
class Data:
    def __init__(self, type, content):
        self.type = type
        self.content = content


class DataProcessor:
    def create_data_processor(self, data):
        pass


class TextDataProcessor(DataProcessor):
    def create_data_processor(self, data):
        print("Text data processing:", data.content)


class AudioDataProcessor(DataProcessor):
    def create_data_processor(self, data):
        print("Audio data processing:", data.content)


class VideoDataProcessor(DataProcessor):
    def create_data_processor(self, data):
        print("Video data processing:", data.content)


class DataProcessorCreator:
    def __init__(self):
        self.processor = None

    def set_processor(self, processor):
        self.processor = processor

    def process_data(self, data):
        if self.processor:
            self.processor.create_data_processor(data)


# Abstract Factory Pattern

# Furniture products
class Furniture:
    def __init__(self, name, style, material, price):
        self.name = name
        self.style = style
        self.material = material
        self.price = price


class FurnitureFactory:
    def create_chair(self):
        pass

    def create_table(self):
        pass

    def create_sofa(self):
        pass


class ModernWoodFactory(FurnitureFactory):
    def create_chair(self):
        return Furniture("Modern Wood Chair", "Modern", "Wood", 100)

    def create_table(self):
        return Furniture("Modern Wood Table", "Modern", "Wood", 200)

    def create_sofa(self):
        return Furniture("Modern Wood Sofa", "Modern", "Wood", 300)


class TraditionalMetalFactory(FurnitureFactory):
    def create_chair(self):
        return Furniture("Traditional Metal Chair", "Traditional", "Metal", 120)

    def create_table(self):
        return Furniture("Traditional Metal Table", "Traditional", "Metal", 220)

    def create_sofa(self):
        return Furniture("Traditional Metal Sofa", "Traditional", "Metal", 320)


class IndustrialGlassFactory(FurnitureFactory):
    def create_chair(self):
        return Furniture("Industrial Glass Chair", "Industrial", "Glass", 150)

    def create_table(self):
        return Furniture("Industrial Glass Table", "Industrial", "Glass", 250)

    def create_sofa(self):
        return Furniture("Industrial Glass Sofa", "Industrial", "Glass", 350)


class FurnitureCreator:
    def __init__(self):
        self.factory = None

    def set_factory(self, factory):
        self.factory = factory

    def create_chair(self):
        if self.factory:
            return self.factory.create_chair()

    def create_table(self):
        if self.factory:
            return self.factory.create_table()

    def create_sofa(self):
        if self.factory:
            return self.factory.create_sofa()


# Multi-player online game

# Character products
class Weapon:
    def __init__(self, type, damage, speed, range):
        self.type = type
        self.damage = damage
        self.speed = speed
        self.range = range


class ConcreteCharacter:
    def __init__(self, name, char_class, weapon, health, mana):
        self.name = name
        self.char_class = char_class
        self.weapon = weapon
        self.health = health
        self.mana = mana


class WarriorSwordFactory(CharacterFactory):
    def create_character(self, name):
        weapon = Weapon("Sword", 15, 5, 10)
        return ConcreteCharacter(name, "Warrior", weapon, 100, 50)


class MageStaffFactory(CharacterFactory):
    def create_character(self, name):
        weapon = Weapon("Staff", 10, 8, 15)
        return ConcreteCharacter(name, "Mage", weapon, 80, 100)


class ArcherBowFactory(CharacterFactory):
    def create_character(self, name):
        weapon = Weapon("Bow", 12, 6, 20)
        return ConcreteCharacter(name, "Archer", weapon, 90, 70)


class CharacterCreator:
    def __init__(self):
        self.factory = None

    def set_factory(self, factory):
        self.factory = factory

    def create_character(self, name):
        if self.factory:
            return self.factory.create_character(name)


# Usage examples
if __name__ == "__main__":
    # Exercise 1: Character creation in a video game
    character_creator = CharacterCreator()
    warrior_factory = WarriorFactory()
    character_creator.set_factory(warrior_factory)
    warrior_character = character_creator.create_character("Warrior")
    print(warrior_character.__dict__)

    # Exercise 2: Real-time data processing system
    data_processor_creator = DataProcessorCreator()
    audio_processor = AudioDataProcessor()
    data_processor_creator.set_processor(audio_processor)
    audio_data = Data("Audio", "Audio data")
    data_processor_creator.process_data(audio_data)

    # Exercise 3: Online furniture marketplace
    furniture_creator = FurnitureCreator()
    modern_wood_factory = ModernWoodFactory()
    furniture_creator.set_factory(modern_wood_factory)
    modern_wood_chair = furniture_creator.create_chair()
    print(modern_wood_chair.__dict__)

    # Exercise 4: Multi-player online game
    character_creator = CharacterCreator()
    mage_staff_factory = MageStaffFactory()
    character_creator.set_factory(mage_staff_factory)
    mage_character = character_creator.create_character("Mage")
    print(mage_character.__dict__)
