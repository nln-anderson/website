from sqlalchemy.engine import create_engine
from sqlalchemy import select, text

file_path = "C:/Users/NAN9/Downloads/book.csv"

def date_handler(date: str) -> str:
    """This function reformats the date for PostgreSQL"""
    date_components = date.split("/")
    if len(date_components[2])==2:
        new_date = f"20{date_components[2]}/{date_components[0]}/{date_components[1]}"
    else:
        new_date = f"{date_components[2]}/{date_components[0]}/{date_components[1]}"
    return new_date

def rate_handler(name: str, first: str) -> int:
    if name == "Kerekes" or name == "Woz" or name == "Boxer" or name=="Ramirez":
        return 35
    elif name == "Anastasi"or name == "McLeod" or name == "Eastepp":
        return 40
    elif name == "Quartararo":
        return 45
    elif name == "Perez" or name == "Johnson" or name == "Clarke" or name=="Pasquini":
        return 60
    
def content_handler(last_name: str, first_name: str) -> str:
    if first_name == "Joseph" or first_name == "Ryan":
        return "Algebra 2"
    elif first_name in ("Sasha", "Ali", "Katheryn", "Sophie", "Tallulah"):
        return "Calculus 1"
    elif first_name in ("Aubrey", "Isabella", "Carly"):
        return "College Algebra"
    elif first_name in ("Nathan", "Kyla"):
        return "Geometry"

def main():
    with open(file_path, "r") as file:
        lines = file.readlines()
        for n in range(3, len(lines)):
            components = lines[n].split(",")
            first_name = components[0].split()[0]
            last_name = components[0].split()[1]
            date = date_handler(components[1])
            rate = rate_handler(last_name, first_name)
            paid = True
            

if __name__ == "__main__":
    main()

