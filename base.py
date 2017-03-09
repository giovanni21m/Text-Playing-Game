from sys import exit
from random import randint



class Scene(object):

    def enter(self):
        print("This scene is not yet configured. Subclass it and implement enter().")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


class Beginning(Scene):

    def enter(self):
        print("Welcome to Text Playing Game,")
        print("also known as TPG.")
        global username = input("Please enter your name, brave one: ")


class Death(Scene):

    quips = [
        "Good game.",
        "Get rekt nerd.",
        "Git gud.",
        "Sleep with the L."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1])
        exit(1)


class GuildHall(Scene):

    def enter(self):
        print("Welcome to the Guild Hall %s." % username)
        print("I am your quest guide, Herold. What would you like to do?")
        print("1. Go on quest.")
        print("2. Visit the blacksmith.")
        print("3. Visit the armorsmith.")

        response = input("Well...? ")

        if response == "1" or "quest" or "go on quest":
            pass
        elif response == "2" or "blacksmith" or "visit the blacksmith":
            pass
        elif response == "3" or "armorsmith" or "visit the armorsmith":
            pass
        else:
            print "That's not an option."


class Caves(Scene):

    def enter(self):
        pass


class Finished(Scene):

    def enter(self):
        print("Finished so soon?")
        print("See you next time.")
        return 'finished'


class Forest(Scene):

    def enter(self):
        pass


class Maze(Scene):

    def enter(self):
        pass


class Mountain(Scene):

    def enter(self):
        pass



class Map(object):

    scenes = {
        'beginning': Beginning(),
        'caves': Caves(),
        'death': Death(),
        'demon': Demon(),
        'dragon': Dragon(),
        'finished': Finished(),
        'forest': Forest(),
        'golem': Golem(),
        'maze': Maze(),
        'minotaur': Minotaur(),
        'mountain': Mountain(),
        'wyvern': Wyvern(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)



a_map = Map('beginning')
a_game = Engine(a_map)
a_game.play()
