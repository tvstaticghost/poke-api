from data import PokeLineup

def main():
    test = PokeLineup('firered', 'bulbasaur'.lower(), True, 'balanced')
    print(test.balanced())


if __name__ == '__main__':
    main()