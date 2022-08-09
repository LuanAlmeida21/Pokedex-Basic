import os
import json

class Pokedex_pro:

    def __init__(self):

        self.list_empty = []
        self.pokedex = {
            '001': {
                'status': {
                    'name': 'Bulbasaur',
                    'attack': 49,
                    'hp': 45,
                    'type one': 'Grass',
                    'type two': 'Poison'
                },
            },

            '002': {
                'status': {
                    'name': 'Charmander',
                    'attack': 52,
                    'hp': 39,
                    'type one': 'Fire',
                    'type two': ''
                },
            },

            '003': {
                'status': {
                    'name': 'Squirtle',
                    'attack': 48,
                    'hp': 44,
                    'type one': 'Water',
                    'type two': ''
                },
            },

            '004': {
                'status': {
                    'name': 'Alolan Ninetales',
                    'attack': 67,
                    'hp': 73,
                    'type one': 'Ice',
                    'type two': 'Fairy'
                },
            },
        }

    def add_dict_into_file_json(self, arquivo, dictionary):
        # And then I tried to write the second one, adding in the existing JSON
        with open(arquivo, 'a+') as file:

            # return the point to the top of the file
            file.seek(0, 0)

            # get dados current
            json_current = file.read()

            # if the file is empty, it may give error
            if json_current:
                # load json current how dict
                dictionary_current = json.loads(json_current)

                # add new dict in current dict
                dictionary_current.update(dictionary)
            else:
                dictionary_current = dictionary

            # clear file
            file.seek(0, 0)
            file.truncate()

            # Write the new dados
            file.write(json.dumps(dictionary_current, indent=True))

            return dictionary_current

    def search_poke_id(self, id):
        search_id = str(id)
        if search_id in self.new_poke:
            print(f'{"Pokemon Found":-^36}')
            for key, value in self.new_poke.items():
                for key_1, value_1 in value.items():
                    if '' in value_1.values():
                        del value_1['type two']
            for key_2, value_2 in self.new_poke[search_id].items():
                for key_3, value_3 in value_2.items():
                    print(f'\t{key_3.title()}: {value_3}')
            return True
            print()
        else:
            print(f"{'Does not exist':-^36}")

    def verify_name(self, name1):
        for key, value in self.new_poke.items():
            for key_1, value_1 in value.items():
                if name1.title() in value_1.values():
                    return True
        else:
            return False

    def search_name(self, name1):
        verify = 0
        for key, value in self.new_poke.items():
            for key_1, value_2 in value.items():
                if '' in value_2.values():
                    del value_2['type two']
                if name1.title() in value_2.values():
                    print(f'{"Pokemon Found":-^36}')
                    for key_3, value_3 in value_2.items():
                        print(f'\t{key_3.title()}: {value_3}')
                else:
                    verify += 1
        if verify == len(self.new_poke):
            return print(f"{'Does not exist':-^36}")

    def list_hp(self, hp_1):
        for key, value in self.new_poke.items():
            for key_1, value_1 in value.items():
                self.list_empty.append(value_1)
                pokedex_class.clear_window()
        if hp_1 == '>':
            for sort in sorted(self.list_empty, key=lambda key: key['hp'], reverse=True):
                if '' in sort.values():
                    del sort['type two']
                for key_2, value_2 in sort.items():
                    print(f'\t {key_2.title()}: {value_2}')
                print()
        else:
            for sort in sorted(self.list_empty, key=lambda key: key['hp']):
                if '' in sort.values():
                    del sort['type two']
                for key_2, value_2 in sort.items():
                    print(f'\t {key_2.title()}: {value_2}')
                print()
    def list_attack(self, attack_1):

        for key, value in self.new_poke.items():
            for key_1, value_1 in value.items():
                self.list_empty.append(value_1)
        if attack_1 == '>':
            for sort in sorted(self.list_empty, key=lambda key: key['attack'], reverse=True):
                if '' in sort.values():
                    del sort['type two']
                for key_2, value_2 in sort.items():
                    print(f'\t {key_2.title()}: {value_2}')
                print()
        else:
            for sort in sorted(self.list_empty, key=lambda key: key['attack']):
                if '' in sort.values():
                    del sort['type two']
                for key_2, value_2 in sort.items():
                    print(f'\t {key_2.title()}: {value_2}')
                print()

    def list_pokedex(self):
        for key, value in self.new_poke.items():
            print(f'Poke ID - {key}')
            for key_1, value_1 in value.items():
                if '' in value_1.values():
                    del value_1['type two']
                for key_2, value_2 in value['status'].items():
                    print(f'{key_2.title()}: {value_2}')
            print()

    def list_type(self, tipo):
        reference = 0
        print(f'Chosen type:  {tipo.upper():-^36}')
        for key, value in self.new_poke.items():
            for key_1, value_2 in value.items():
                if tipo not in value_2.values():
                    reference += 1
                else:
                    if '' in value_2.values():
                        del value_2['type two']
                    for key_3, value_3 in value_2.items():
                        print(f'\t{key_3.title()}: {value_3}')
                    print()
        if reference == len(self.new_poke):
            print(f"Chosen Type '{tipo}' Not Exist")
            print()

    def add_edit(self, chose):
        if chose == 1:
            for i in self.new_poke:
                i = int(i)
            prox_id = i + 1
            prox_id = str(f'00{prox_id}')

            name = input('Name: ')
            while pokedex_class.verify_name(name) == True:
                name = input('Type Another Name: ')

            attack = int(input('Attack: '))
            hp = int(input('HP: '))

            type_one = input('Type One: ')
            while pokedex_class.types(type_one) == False:
                type_one = input('Type One: ')

            type_two = input('Type Two: ')
            while pokedex_class.types(type_two) == False:
                type_two = input('Type Two: ')

            self.pokedex[prox_id] = {str(prox_id): {
                'status':
                {'name': name,
                 'attack': attack,
                 'hp': hp,
                 'type one': type_one,
                 'type two': type_two}
            },
            }
            pokedex_class.clear_window()
            self.new_poke = pokedex_class.add_dict_into_file_json(
                'pokedex_teste.json', self.pokedex[prox_id])
            pokedex_class.list_pokedex()

        else:
            pokedex_class.list_pokedex()
            id = input('Type ID you wish change (EX: 001): ')
            if pokedex_class.search_poke_id(id) == True:
                name = input('Name: ')
                while pokedex_class.verify_name(name) == True:
                    name = input('Type Another Name: ')

                attack = int(input('Attack: '))
                hp = int(input('HP: '))

                type_one = input('Type One: ')
                while pokedex_class.types(type_one) == False:
                    type_one = input('Type One: ')

                type_two = input('Type Two: ')
                while pokedex_class.types(type_two) == False:
                    type_two = input('Type Two: ')

                self.new_poke[id] = {str(id): {
                    'status':
                    {'name': name,
                     'attack': attack,
                     'hp': hp,
                     'type one': type_one,
                     'type two': type_two}
                },
                }
                pokedex_class.clear_window()
                self.new_poke = pokedex_class.add_dict_into_file_json(
                    'pokedex_teste.json', self.new_poke[id])
                pokedex_class.list_pokedex()

    def menu(self):
        pokedex_class.clear_window()
        print(f'Search by Poke ID {"": ^10} (1)')
        print(f'Search by Name {"": ^13} (2)')
        print(f'List by HP {"": ^17} (3)')
        print(f'List by Attack {"": ^13} (4)')
        print(f'List by Type {"": ^15} (5)')
        print(f'List Pokedex {"": ^15} (6)')
        print(f'Add/Edit Pokedex {"": ^4} (7)')

    def clear_window(self):
        return os.system('cls')

    def types(self, verify_type):
        types = ('Normal', 'Fire', 'Water', 'Electric', 'Grass', 'Ice',
                 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock',
                 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy', '')

        if verify_type in types:
            return True
        else:
            return False

    def start_pokedex(self):
        self.new_poke = pokedex_class.add_dict_into_file_json(
            'pokedex_teste.json', self.pokedex)

        while True:
            pokedex_class.menu()
            option = int(input('Choose an option -> '))
            pokedex_class.clear_window()

            while option > 7 or option < 0:
                option = int(input('Choose an option again: '))
            if option == 1:
                pokedex_class.clear_window()
                id = input('Type the ID (EX: 001): ')
                pokedex_class.search_poke_id(id)

            if option == 2:
                pokedex_class.clear_window()
                name = input('Type the name pokemon: ')
                pokedex_class.search_name(name)

            if option == 3:
                pokedex_class.clear_window()
                hp = input(str(
                    'What order you wish?\nFrom Highest to Lowest type (>) \nFrom Lowest to Highest (<)\n'))
                while hp != '>' and hp != '<':
                    hp = input('Type again: ')
                pokedex_class.list_hp(hp)

            if option == 4:
                pokedex_class.clear_window()
                attack = input(str(
                    'What order you wish?\nFrom Highest to Lowest type (>) \nFrom Lowest to Highest (<)\n'))
                while attack != '>' and attack != '<':
                    attack = input('Type again: ')
                pokedex_class.clear_window()
                pokedex_class.list_attack(attack)

            if option == 5:
                tipo = input('Type: ')
                pokedex_class.clear_window()
                pokedex_class.list_type(tipo)

            if option == 6:
                pokedex_class.clear_window()
                pokedex_class.list_pokedex()

            if option == 7:
                pokedex_class.clear_window()
                add_or_edit = int(
                    input('What you wish to do? (1) Add or (2) Edit: '))
                pokedex_class.add_edit(add_or_edit)

            answer = input('Continue? (Y) Yes or (N) No: ')
            if answer.title() == 'Y':
                pokedex_class.clear_window()
            else:
                pokedex_class.clear_window()
                break

pokedex_class = Pokedex_pro()
pokedex_class.start_pokedex()
