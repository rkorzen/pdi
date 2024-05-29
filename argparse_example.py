import argparse

def main():
    parser = argparse.ArgumentParser(description="przykładowy Interfejs tekstowy ")

    parser.add_argument("--waluta", help="Kod waluty")
    parser.add_argument("--kwota", type=int, help="ilość PLN przeznaczonych na zakup waluty")
    args = parser.parse_args()

    print(args.waluta, args.kwota)

main()