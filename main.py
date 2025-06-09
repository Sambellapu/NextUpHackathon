# Author: Samanyu Bellapu

# Theme: Vacation/Itineraries

# Intermediate Prompt: Create a vacation simulator,
# a text-based adventure program where users go on a virtual
# summer vacation and make choices that shape their journey.
# The program should present different scenarios, like going to the beach,
# hiking in the mountains, or exploring a city, and allow the user to choose
# what to do at each step. Their decisions affect outcomes such as energy level,
# fun score, or unexpected events like getting sunburned or finding a hidden spot.
# Include features like branching storylines, random events, and a final trip
# summary based on the user's experience.


options = {
    1: "Kuta Beach",
    2: "Sacred Monkey Forest Sacntuary",
    3: "Tegallalang Rice Terrace",
    4: "Exit Planner"
}

beach_options = {
    1: "Build a Sand Castle",
    2: "Scuba Dive",
    3: "Surf",
    4: "Rest & Relax ..?"
}

sand_castle_options = {
    1: "Small",
    2: "Medium",
    3: "Large",
    4: "Extra Large"
}

scuba_diving_options = {
    1: "50ft",
    2: "100ft",
    3: "150ft",
    4: "200ft"
}

surfing_options = {
    1: "30 mintues",
    2: "1 hour",
    3: "1 hour and a half",
    4: "2 hours"
}

resting_options = {
    1: "30 mintues",
    2: "1 hour",
    3: "1 hour and a half",
    4: "2 hours"
}

lunch_options = {
    1: "Barbecue",
    2: "Pre made",
    3: "Take out"
}

monkey_forest = {
    1: "Play with the monkeys",
    2: "Walk around the trails",
    3: "Watch the monkeys play"
}

games_with_monkeys = {
    1: "Catch",
    2: "Tag",
    3: "Build puzzles"
}

trail_time = {
    1: "1 hour",
    2: "1 hour and a half",
    3: "2 hour"
}

watch_time = {
    1: "1 hour",
    2: "2 hours",
    3: "3 hours"
}

rice_terrace = {
    1: "Look at the scenic view",
    2: "Go on the famous swing",
    3: "Walk the trail"
}

how_long_view = {
    1: "30 mintuets",
    2: "1 hour",
    3: "1 hour and a half"
}

choose_push = {
    1: "Weak",
    2: "Medium",
    3: "Hard"
}

how_long_hike = {
    1: "1 hour",
    2: "1 hour and half",
    3: "2 hours"
}


def kuta_beach():
    energy = 0
    fun = 0
    surprises = []
    print("\nGreat choice! At the Kuta beach, what would you like to do ?")
    for number, description in beach_options.items():
        print(f"{number}. {description}")

    kuta_beach_user_Options = int(input(f"\n:_ "))

    if kuta_beach_user_Options == 1:
        # sand_castle_options 1:"Small", 2:"Medium", 3:"Large",4:"Extra Large"
        print("Wow! Sand Castle that's fun, how big you are planning ?")
        for number, description in sand_castle_options.items():
            print(f"{number}. {description}")

        sand_castle_user_Options = int(input(f"\n:_"))
        print("Thats cool, you will be hungry, any plans for lunch ?")

        for number, description in lunch_options.items():
            print(f"{number}. {description}")

        if sand_castle_user_Options == 1:
            energy -= 1
            fun += 1
        elif sand_castle_user_Options == 2:
            energy -= 2
            fun += 2
            surprises.append("You find a rare seashell!!")
        elif sand_castle_user_Options == 3:
            energy -= 3
            fun += 3
        elif sand_castle_user_Options == 4:
            energy -= 3
            fun += 4
            surprises.append("You win a sandcastle contest and get a golden shovel!")

    elif kuta_beach_user_Options == 2:
        # scuba dive
        print("Wow Adventures! How deep you like to dive ?")
        for number, description in scuba_diving_options.items():
            print(f"{number}. {description}")

        scuba_diving_user_Options = int(input(f"\n:_"))
        print("Thats cool, you will be hungry, any plans for lunch ?")

        if scuba_diving_user_Options == 1:
            energy += 1
            fun += 3
        elif scuba_diving_user_Options == 2:
            energy += 0
            fun += 4
        elif scuba_diving_user_Options == 3:
            energy -= 2
            fun += 5
            surprises.append("A find a message in a bottle. What does it say?")
        elif scuba_diving_user_Options == 4:
            energy -= 5
            fun += 6

    elif kuta_beach_user_Options == 3:
        # surfing
        print("Wow Adventures! How long would you surf ?")
        for number, description in surfing_options.items():
            print(f"{number}. {description}")

        surfing_user_Options = int(input(f"\n:_"))
        print("Thats cool, you will be hungry, any plans for lunch ?")

        # surfing_user_Options = int(input(f"How long would you surf {surfing_options} choose on of the numbers "))

        if surfing_user_Options == 1:
            energy -= 0
            fun += 3
            surprises.append("A friendly dolphin swims by and jump out of the water!")
        elif surfing_user_Options == 2:
            energy -= 3
            fun += 5
            surprises.append("You get caught in a surprise splash from a big wave!")
        elif surfing_user_Options == 3:
            energy -= 4
            fun = 3
        elif surfing_user_Options == 4:
            energy -= 5
            fun = 2
            surprises.append("You spot a pod of dolphins in the distance.")
    elif kuta_beach_user_Options == 4:
        # sun bathing
        print("Wow its so relaxing! How long would you rest ?")
        for number, description in resting_options.items():
            print(f"{number}. {description}")

        resting_user_Options = int(input(f"\n:_"))
        print("Thats cool, you will be hungry, any plans for lunch ?")

        if resting_user_Options == 1:
            energy += 2
            fun += 2
            surprises.append("You seagul tries to steal your snack!.")
        elif resting_user_Options == 2:
            energy += 3
            fun += 1
            surprises.append("A kite lands near you, and the owner gives you a turn flying it.")
        elif resting_user_Options == 3:
            energy += 4
            fun -= 1
        elif resting_user_Options == 4:
            energy += 5
            fun -= 3
            surprises.append("You get a little sunburned -- time for a sunscreen!.")
    return energy, fun, surprises


def sacred_monkey_forest():
    energy = 0
    fun = 0
    surprises = []

    print(
        "\nGreat choice! Sacred monkey forest is one of the best location to see in Bali, what would you like to do ?")
    for number, description in monkey_forest.items():
        print(f"{number}. {description}")

    sacred_monkey_forest_user_Options = int(input(f"\n:_ "))

    if sacred_monkey_forest_user_Options == 1:
        print("Pick which game you want to play with the monkeys ?")
        for number, description in games_with_monkeys.items():
            print(f"{number}. {description}")

        play_with_the_monkeys_user_Options = int(input(f"\n:_"))
        print("Thats cool, you will be hungry, any plans for lunch ?")

        if play_with_the_monkeys_user_Options == 1:
            energy -= 1
            fun += 3
            surprises.append("A monkey gently tugs at your backpack, curious about whats inside.")
        elif play_with_the_monkeys_user_Options == 2:
            energy -= 4
            fun += 2
        elif play_with_the_monkeys_user_Options == 3:
            energy -= 1
            fun += 3
            surprises.append("A local guide shares a legend about the forest's magical spirits.")
    elif sacred_monkey_forest_user_Options == 2:
        print("Pick how long you want to walk on the trails ?")

        for number, description in trail_time.items():
            print(f"{number}. {description}")

        trails_monkey_forest = int(input(f"\n:_"))
        print("Thats cool, you will be hungry, any plans for lunch ?")

        if trails_monkey_forest == 1:
            energy -= 1
            fun += 3
            surprises.append("You witness a baby monkey hugging its mother-- such a tender moment!.")
        elif trails_monkey_forest == 2:
            energy -= 2
            fun += 2
            surprises.append("A playful monkey jump onto your sholder for a quick ride!.")
        elif trails_monkey_forest == 3:
            energy -= 4
            fun += 1
            surprises.append("You monkey tires to snatch your sunglasses.")
    elif sacred_monkey_forest_user_Options == 3:
        print("How long do you want to wacth them ?")

        for number, description in watch_time.items():
            print(f"{number}. {description}")

        puzzles_with_the_monkey = int(input(f"\n:_"))
        print("Thats cool, you will be hungry, any plans for lunch ?")

        if puzzles_with_the_monkey == 1:
            energy -= 1
            fun += 3
            surprises.append("You see a monkey family playing together near a temple statues.")
        elif puzzles_with_the_monkey == 2:
            energy -= 2
            fun += 2
            surprises.append("You find a beautiful flower offering left at a temple.")
        elif puzzles_with_the_monkey == 3:
            energy -= 3
            fun += 3
            surprises.append("You quietly watch a purification ritual at the Baji temple.")
    return energy, fun, surprises


def Tegallalan_Rice_Terrace():
    energy = 0
    fun = 0
    surprises = []

    print("\nGreat choice! The Tegallalan rice terrace is a great pick out of these three, what would you like to do ?")
    for number, description in rice_terrace.items():
        print(f"{number}. {description}")

    Tegallalan_rice_terrace_user_Options = int(input(f"\n:_ "))

    if Tegallalan_rice_terrace_user_Options == 1:
        print("How long will you view the scenic vally ?")

        for number, description in how_long_view.items():
            print(f"{number}. {description}")

        how_long_will_you_view = int(input(f"\n:_"))
        print("Thats cool, you will be hungry, any plans for lunch ?")

        if how_long_will_you_view == 1:
            energy -= 1
            fun += 2
            surprises.append("You meet a local artist scketching the landscape.")
        elif how_long_will_you_view == 2:
            energy -= 2
            fun += 1
        elif how_long_will_you_view == 3:
            energy -= 3
            fun += 3
            surprises.append("A friendly dog joins you for part of your walk.")
    elif Tegallalan_rice_terrace_user_Options == 2:
        print("Go on the famous swing ?")

        for number, description in choose_push.items():
            print(f"{number}. {description}")

        how_push = int(input(f"\n:_"))
        print("Thats cool, you will be hungry, any plans for lunch ?")

        if how_push == 1:
            energy -= 0
            fun += 1
            surprises.append("A light rain starts, and you see a rainbow arching over the fields.")
        elif how_push == 2:
            energy -= 0
            fun += 3
        elif how_push == 3:
            energy -= 0
            fun += 5
            surprises.append("A butterfly lands on your hand as you admire the view.")
    elif Tegallalan_rice_terrace_user_Options == 3:
        print("Hiking thats great chose!! how long will you hike ?")

        for number, description in how_long_hike.items():
            print(f"{number}. {description}")

        how_long_hike1 = int(input(f"\n:_"))
        print("Thats cool, you will be hungry, any plans for lunch ?")

        if how_long_hike1 == 1:
            energy -= 2
            fun += 3
            surprises.append("You spot a farmer planting rice and get invited to help.")
        elif how_long_hike1 == 2:
            energy -= 3
            fun += 2
        elif how_long_hike1 == 3:
            energy -= 4
            fun += 1
            surprises.append(
                "You discover a hidden path that leads to a quite, scenic viewpoint-- perfect for photos!.")
    return energy, fun, surprises


def printSummary(e, f, sup):
    e = 1 if e <= 0 else e
    f = 1 if f <= 0 else f
    print("##########################################################")
    if sup:
        print("\nYour Surprises \U0001F603:")
        for s in sup:
            print(f" '{s}' ")
    else:
        print("\nSorry No Surprises: \U0001F641 ")

    if e == 1:
        print("Your Energy Level: \U00002B50")
    elif e == 2:
        print("Your Energy Level: \U00002B50 \U00002B50")
    elif e == 3:
        print("Your Energy Level: \U00002B50 \U00002B50 \U00002B50")
    elif e == 4:
        print("Your Energy Level: \U00002B50 \U00002B50 \U00002B50 \U00002B50")
    elif e == 5:
        print("Your Energy Level: \U00002B50 \U00002B50 \U00002B50 \U00002B50 \U00002B50")

    if f == 1:
        print("Fun Factor: \U0001F60D")
    elif f == 2:
        print("Fun Factor: \U0001F60D \U0001F60D")
    elif f == 3:
        print("Fun Factor: \U0001F60D \U0001F60D \U0001F60D")
    elif f == 4:
        print("Fun Factor: \U0001F60D \U0001F60D \U0001F60D \U0001F60D")
    elif f == 5:
        print("Fun Factor: \U0001F60D \U0001F60D \U0001F60D \U0001F60D \U0001F60D")

    print("##########################################################")


def plannerOutput(lv):
    if lv == 1:
        en, fu, surp = kuta_beach()
        printSummary(en, fu, surp)
    elif lv == 2:
        en, fu, surp = sacred_monkey_forest()
        printSummary(en, fu, surp)
    elif lv == 3:
        en, fu, surp = Tegallalan_Rice_Terrace()
        printSummary(en, fu, surp)
    else:
        print("Bye Bye Nice using the planner..!")


def main():
    level1 = 0
    while level1 != 4:
        print("\nWhere would you like to go ? \n")
        for number, description in options.items():
            print(f"{number}. {description}")

        level1 = int(input(f"\nChose one of the numbers: "))
        plannerOutput(level1)


# Beach \U0001F3D6
# Bali print("\U0001F1EE\U0001F1E9")

if __name__ == "__main__":
    print("Welcome to Samanyu Bellapu's Summer Adventure Virtual Planner for Bali \u2708 \u2708 !.. \n")
    main()