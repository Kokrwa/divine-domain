import random
import time
import os
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def animated_intro():
    clear()
    title_lines = [
        "                                       ",
        "                ,----..                 ",
        "  ,----..      /   /   \\      ,---,     ",
        " /   /   \\    /   .     :   .'  .' `\\   ",
        "|   :     :  .   /   ;.  \\,---.'     \\  ",
        ".   |  ;. / .   ;   /  ` ;|   |  .`\\  | ",
        ".   ; /--`  ;   |  ; \\ ; '|   ' '  ;  : ",
        ";   | ;  __ |   :  | ; | '|   ' '  ;  : ",
        "|   : |.' .'.   |  ' ' ' :'   | ;  .  | ",
        ".   | '_.' :'   ;  \\; /  ||   | :  |  ' ",
        "'   ; : \\  | \\   \\  ',  / '   : | /  ;  ",
        "'   | '/  .'  ;   :    /  |   | '` ,/   ",
        "|   :    /     \\   \\ .'   ;   :  .'     ",
        " \\   \\ .'       `---`     |   ,.'       ",
        "  `---`                   '---'         ",
        "                                          ",
        "            🌍 DIVINE DOMAIN 🌍"
    ]

    for i in range(1, len(title_lines)+1):
        clear()
        for line in title_lines[:i]:
            print(line)
        time.sleep(0.15)
    time.sleep(1.5)

def ascii_title():
    print(r"""
                                       
                ,----..                 
  ,----..      /   /   \      ,---,     
 /   /   \    /   .     :   .'  .' `\   
|   :     :  .   /   ;.  \,---.'     \  
.   |  ;. / .   ;   /  ` ;|   |  .`\  | 
.   ; /--`  ;   |  ; \ ; '|   ' '  ;  : 
;   | ;  __ |   :  | ; | '|   ' '  ;  : 
|   : |.' .'.   |  ' ' ' :'   | ;  .  | 
.   | '_.' :'   ;  \; /  ||   | :  |  ' 
'   ; : \  | \   \  ',  / '   : | /  ;  
'   | '/  .'  ;   :    /  |   | '` ,/   
|   :    /     \   \ .'   ;   :  .'     
 \   \ .'       `---`     |   ,.'       
  `---`                   '---'         
                                                                                  
            🌍 DIVINE DOMAIN 🌍
""")

def show_lore():
    clear()
    print("\n📖 LORE OF DIVINE DOMAIN\n")
    print("In the beginning, there was only void. Then you awoke.")
    print("The mortals now crawl across your creation. They beg, they defy, they evolve.")
    print("You are the divine architect, the unseen hand, the wrath in the sky.")
    print("\nRule them wisely. Or don’t. Let the world burn.")
    input("\nPress Enter to return to menu...")

def show_controls():
    clear()
    print("\n🎮 CONTROLS & INFO\n")
    print("• Choose actions every turn to shape civilizations.")
    print("• Build faith to earn Divine Points (DP).")
    print("• Use DP to cast world-altering Divine Powers.")
    print("• Rebellion builds if faith drops. Keep them loyal... or punish them.")
    print("• Respond to prayers from civilizations: help or ignore.")
    input("\nPress Enter to return to menu...")

def bar(stat):
    total_blocks = 20
    filled = int((stat / 100) * total_blocks)
    empty = total_blocks - filled
    if stat >= 70:
        color = "🟩"
    elif stat >= 30:
        color = "🟨"
    else:
        color = "🔴"
    return f"{color} [" + "█" * filled + "░" * empty + f"] {stat}%"

def start_game():
    civilizations = {
        "Zarathians": {"faith": 50, "war": 30, "tech": 40, "culture": 45, "science": 25, "rebellion": 0, "religion": "Worships You"},
        "Myrrdin": {"faith": 80, "war": 20, "tech": 30, "culture": 75, "science": 35, "rebellion": 0, "religion": "Worships You"},
        "Drakor": {"faith": 20, "war": 70, "tech": 50, "culture": 15, "science": 60, "rebellion": 0, "religion": "Worships You"}
    }

    divine_points = 0

    powers = {
        "Holy Fire": {"cost": 20, "desc": "🔥 Wipe a civ’s war + rebellion"},
        "Brainwash": {"cost": 25, "desc": "🧠 Set faith to 100, rebellion to 0"},
        "Flood the World": {"cost": 40, "desc": "🌊 Reset all stats to 50"},
        "Create Godspawn": {"cost": 30, "desc": "👶 Boost all stats by 10"},
        "Ascension": {"cost": 100, "desc": "👁 End the game instantly"}
    }

    actions = [
        "Create Life", "Smite Civilization", "Grant Miracle", 
        "Send Plague", "Inspire Prophet", "Advance Science", 
        "Corrupt Culture", "Do Nothing"
    ]

    def pick_civ():
        civ_names = list(civilizations.keys())
        print("\n🌍 Choose a civilization:")
        for i, name in enumerate(civ_names):
            print(f"{i + 1}. {name}")
        while True:
            try:
                choice = int(input("→ Select (1-3): "))
                if 1 <= choice <= len(civ_names):
                    return civ_names[choice - 1]
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Enter a number.")

    def cast_power():
        nonlocal divine_points
        print(f"\n✨ Divine Points: {divine_points}")
        for i, (name, info) in enumerate(powers.items()):
            print(f"{i + 1}. {name} ({info['cost']} DP) - {info['desc']}")
        while True:
            try:
                choice = int(input("Choose a power to cast (or 0 to cancel): "))
                if choice == 0:
                    return
                if 1 <= choice <= len(powers):
                    break
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Enter a number.")

        power = list(powers.keys())[choice - 1]
        cost = powers[power]["cost"]

        if divine_points < cost:
            print("⛔ Not enough divine points!")
            return

        divine_points -= cost

        if power == "Holy Fire":
            target = pick_civ()
            civ = civilizations[target]
            civ["war"] = 0
            civ["rebellion"] = 0
            print(f"🔥 {target} has been purged of violence and treason.")
        elif power == "Brainwash":
            target = pick_civ()
            civ = civilizations[target]
            civ["faith"] = 100
            civ["rebellion"] = 0
            print(f"🧠 {target} now worships you completely.")
        elif power == "Flood the World":
            for civ in civilizations.values():
                for key in ["faith", "war", "tech", "culture", "science", "rebellion"]:
                    civ[key] = 50
            print("🌊 The world resets in a divine flood.")
        elif power == "Create Godspawn":
            for civ in civilizations.values():
                for key in ["faith", "war", "tech", "culture", "science"]:
                    civ[key] = min(100, civ[key] + 10)
            print("👶 A divine child walks the lands, blessing all.")
        elif power == "Ascension":
            print("👁 You ascend beyond this reality. The game ends.")
            show_stats()
            sys.exit()

    def resolve_action(action):
        nonlocal divine_points
        if action is None:
            return

        target = random.choice(list(civilizations.keys()))
        print(f"\n🌐 Action: {action} on {target}")
        civ = civilizations[target]

        if action == "Create Life":
            civ["faith"] += 10
            civ["culture"] += 5
        elif action == "Smite Civilization":
            civ["war"] -= 20
            civ["faith"] += 15
            civ["tech"] -= 10
            civ["rebellion"] += 10
        elif action == "Grant Miracle":
            civ["faith"] += 20
            civ["rebellion"] -= 10
        elif action == "Send Plague":
            civ["tech"] -= 15
            civ["faith"] += 5
            civ["science"] -= 10
            civ["rebellion"] += 15
        elif action == "Inspire Prophet":
            civ["faith"] += 25
            civ["culture"] += 10
            civ["rebellion"] -= 5
        elif action == "Advance Science":
            civ["science"] += 20
            civ["faith"] -= 10
            civ["rebellion"] += 10
        elif action == "Corrupt Culture":
            civ["culture"] -= 25
            civ["war"] += 10
            civ["rebellion"] += 15
        elif action == "Do Nothing":
            for civ in civilizations.values():
                civ["faith"] -= 5
                civ["rebellion"] += 5

        for key in ["faith", "war", "tech", "culture", "science"]:
            civ[key] = max(0, min(100, civ[key]))
        civ["rebellion"] = max(0, min(100, civ["rebellion"]))

        divine_points += civ["faith"] // 20
        divine_points += civ["rebellion"] // 25

        religion_check(target)

    def religion_check(civ_name):
        civ = civilizations[civ_name]
        if civ["rebellion"] >= 100:
            civ["religion"] = "Rebels / False Gods"
            civ["faith"] = 0
        elif civ["faith"] < 20 and civ["science"] > 60:
            civ["religion"] = "Atheist"
        elif civ["faith"] > 60:
            civ["religion"] = "Worships You"

    def show_stats():
        print("\n📊 Civilization Status:")
        for civ, stats in civilizations.items():
            print(f"\n🔹 {civ} ({stats['religion']})")
            for key in ["faith", "war", "tech", "culture", "science", "rebellion"]:
                print(f"{key.capitalize():<10}: {bar(stats[key])}")
        print(f"\n✨ Divine Points: {divine_points}")

    def handle_prayers():
        nonlocal divine_points
        # Randomly decide if prayers come in this turn (0-2 prayers)
        num_prayers = random.randint(0, 2)
        if num_prayers == 0:
            return

        civ_names = list(civilizations.keys())
        prayers = random.sample(civ_names, k=num_prayers)

        print("\n🙏 You receive prayers from:")
        for i, civ in enumerate(prayers, 1):
            print(f"{i}. {civ} - They ask for divine help!")

        print(f"{len(prayers)+1}. Ignore all prayers")

        while True:
            try:
                choice = int(input(f"Choose a prayer to answer (1-{len(prayers)+1}): "))
                if 1 <= choice <= len(prayers):
                    selected = prayers[choice - 1]
                    civ = civilizations[selected]
                    # Helping increases faith & DP, reduces rebellion
                    civ["faith"] = min(100, civ["faith"] + 20)
                    civ["rebellion"] = max(0, civ["rebellion"] - 15)
                    divine_points += 10
                    print(f"✨ You answered {selected}'s prayer. Faith rises and rebellion falls.")
                    break
                elif choice == len(prayers) + 1:
                    # Ignoring causes rebellion +10 to all praying civs
                    for civ in prayers:
                        civilizations[civ]["rebellion"] = min(100, civilizations[civ]["rebellion"] + 10)
                    print("😔 You ignored the prayers. Rebellion grows in their hearts.")
                    break
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Enter a number.")

    for turn in range(999):
        print(f"\n🕛 Turn {turn + 1}")
        show_stats()

        # Handle prayers before actions
        handle_prayers()

        print("\n🛠 Choose your divine action:")
        for i, act in enumerate(actions):
            print(f"{i + 1}. {act}")
        print("9. Cast Divine Power ✨")

        while True:
            try:
                choice = int(input("→ Choose (1-9): "))
                if 1 <= choice <= 9:
                    break
                else:
                    print("Choose a number between 1 and 9.")
            except ValueError:
                print("Enter a valid number.")

        if choice == 9:
            cast_power()
            continue

        action = actions[choice - 1]
        resolve_action(action)
        time.sleep(1)

    print("\n🌟 FINAL JUDGMENT 🌟")
    show_stats()

def show_menu():
    while True:
        clear()
        ascii_title()
        print("1. Start Game")
        print("2. Lore")
        print("3. Controls")
        print("4. Exit")
        choice = input("\nChoose an option: ")

        if choice == "1":
            start_game()
            break
        elif choice == "2":
            show_lore()
        elif choice == "3":
            show_controls()
        elif choice == "4":
            print("Farewell, Divine One.")
            sys.exit()
        else:
            input("Invalid. Press Enter to continue.")

# Run the intro animation, then show the menu
animated_intro()
show_menu()
