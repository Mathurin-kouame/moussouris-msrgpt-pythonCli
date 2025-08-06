# import requests
# import argparse

# parser = argparse.ArgumentParser(description="Récupération des en-têtes HTTP d'une url")
# parser.add_argument("-u", "--url", help="L'URL cible; ex: www.exemple.com")

# args = parser.parse_args()

# try:
#     response = requests.get(args.url)
#     print("Entêtes reçu")
#     #print("{}").format(response.headers))
    
#     for key, value in response.headers.items():
#         print(f"{key}: {value}")

# except Exception  as e:
#     print(f"Erreur : {e}")

import argparse

def main():
    parser = argparse.ArgumentParser(description="Fais des calculs simples entre deux nombres.")
    parser.add_argument("x", type=int, help="Premier nombre")
    parser.add_argument("y", type=int, help="Deuxième nombre")
    parser.add_argument("operation", choices=["add", "sub", "mul", "div"], help="Opération à effectuer")

    args = parser.parse_args()

    if args.operation == "add":
        result = args.x + args.y
        symbole = "+"
    elif args.operation == "sub":
        result = args.x - args.y
        symbole = "-"
    elif args.operation == "mul":
        result = args.x * args.y
        symbole = "*"
    elif args.operation == "div":
        if args.y == 0:
            print("Erreur : division par zéro.")
            return
        result = args.x / args.y
        symbole = "/"

    print(f"{args.x} {symbole} {args.y} = {result}")

if __name__ == "__main__":
    main()
