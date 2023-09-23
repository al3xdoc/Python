import random
class Player :
    'This is your character'
    def __init__(self, name, health, damage, mana): 
        self.name = name
        self.level = 1
        self.exp = 0  
        self.health = health
        self.damage = damage  
        self.mana = mana  
    def create_hero(name, race, ) :
        health = 0
        damage = 0
        mana = 0
        name = name
        if race.lower() == race_list[0]:
            health += 50
            damage += 30
            mana += 170
        elif race.lower() == race_list[1]:
            health += 130
            damage += 30
            mana += 130
        elif race.lower() == race_list[2]:
            health += 100
            damage += 20
            mana += 100
        elif race.lower() == race_list[3]:
            health += 30
            damage += 10
            mana += 215
        else:
            print("Please, choose from the race list!")
        return Player(name, health, damage, mana)
    def attack(self,enemy):
        enemy.hp -= self.damage
        if enemy.hp <= 0:
            print(enemy.name,"was defeated")
            self.create_weapon()
            print(f"{enemy.name} has dropped {weapon}({rarity})")
            qweapon = input("Would you like to equipt it?")
            if qweapon == "yes":
                if rarity == weapons_rarity[0]:
                    self.damage += 3
                elif rarity == weapons_rarity[1]:
                    self.damage += 6                
                elif rarity == weapons_rarity[2]:
                    self.damage += 9
                elif rarity == weapons_rarity[3]:
                    self.damage += 15
                print(f"You have picked up {weapon}({rarity})")
            else:
                print(f"You have not picked up {weapon}({rarity})")
            self.exp += 10
            if self.exp >= 100:
                self.level_up()
                enemy.level_up()
            return True
        else:
            print(enemy.name,"has",enemy.hp,"hp left!")
            return False
    def create_weapon(self):
        global weapon, rarity
        weapon = random.choice(weapons_list)
        rarity = random.choice(weapons_rarity)
        return weapon, rarity
    def level_up(self):
        self.exp = 0 
        self.level += 1 
        self.health += 5
        self.damage += 1  
        self.mana += 5  
        print(f"Congratualtion! You have leveled up to level : {self.level}. Keep going")
    def spell_ability(self ):
        qspell = input("What spell would you like to use?")
        if qspell == spells_list[0]:
            if self.mana >= 20:
                self.damage += 5
                self.mana -= 20
                print(f"Hp:{self.health}  Dmg:{self.damage}")
            else : 
                print("You don't have enough mana!")
        elif qspell == spells_list[1]:
            if self.mana >= 40:
                self.health += 15
                self.mana -= 40
                print(f"Hp:{self.health}  Dmg:{self.damage}")
            else :
                print("You don't have enough mana!")
        elif qspell == spells_list[2]:
            if self.mana >= 20:
                self.health += enemy.damage
                self.mana -= 20
                print(f"Hp:{self.health}  Dmg:{self.damage}")
            else :
                print("You don't have enough mana!")
        elif qspell == spells_list[3]:
            if self.mana >= 40:
                self.damage += 15
                self.mana -= 40
                print(f"Hp:{self.health}  Dmg:{self.damage}")
            else :
                print("You don't have enough mana!")
        elif qspell == spells_list[4]:
            if self.mana >= 30:
                enemy.hp -= 10
                self.mana -= 30
                print(f"Hp:{self.health}  Dmg:{self.damage}")
            else :
                print("You don't have enough mana!")


class Enemy :
    'This is the enemy'
    def __init__(self, name, damage, hp):
        self.name = name
        self.damage = damage
        self.hp = hp
        
    def create_enemy():
        # global min_dmg , max_dmg ,min_hp , max_hp
        # min_dmg = 5
        # max_dmg = 10
        # min_hp = 50
        # max_hp = 70
        name = random.choice(name_list)
        damage = random.randint(5,10)
        hp = random.randint (50,70)
        return Enemy(name, damage, hp)
    def attack(hero, self):
        hero.hp -= self.damage
        if hero.hp <= 0:
            print(hero.name,"was defeated")
        else:
            print(hero.name,"has",hero.hp,"hp left!")
    # def level_up(self):
    #     min_dmg += 2
    #     max_dmg += 2
    #     min_hp += 10
    #     max_hp += 10


def fight_choice():
    battle = input(f"Would you like to attack {enemy.name}?")
    if battle == "yes":
        result = my_player.attack(enemy)
        if result == False:
            enemy.attack(my_player)
            fight_choice()
    elif battle == "spell":
        my_player.spell_ability()
        fight_choice()

    else: 
        print("You have escaped")
    

name = input("What is your player's name?")

race_list = ['elf', 'dwarf', "human", "fairy"]
your_race = input("What race do you choose?")

profession_list = ['archer', 'barbarian', 'mage']
your_profession = input("What profession would you like?")

name_list = ['Azazel', 'Keres', 'Andras', 'Jafar', 'Ozul'] 

weapons_list = ['sword', 'bow', 'axe' , 'staff']
weapons_rarity = ['common', 'uncommon' , 'rare' , 'legendary']

spells_list = ['fireball' , 'healing' , 'freezing' , 'battle roar', 'meteor shower' , ] 


my_player = Player.create_hero(name, your_race)
print(f"Your player's name is: {name}")
print(f"Your race is : {your_race}")



while True:
    event = random.randint(1,2)
    if event == 1:
        enemy = Enemy.create_enemy()
        print(f"Enemy: {enemy.name} hp:{enemy.hp} dmg:{enemy.damage} ") 
        fight_choice()
    elif event == 2:
        print("There are no enemies here")

