from cat_fact import CatFact
from connector import Connector

def main():
    connector = Connector()
    for _ in range(3):
        data = connector.extract_info()
        cat_fact = CatFact(fact=data["fact"], length=data["length"])
        print(cat_fact)

if __name__ == "__main__":
    main()


