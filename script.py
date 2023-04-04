#pandas
#edited
import pandas
#FFWF


def main():
    Employe_name = input("Enter Employe details: ")
    Employe_Id = int(input("Enter Employe Id : "))
    Employe_salary = float(input("Enter salary details : "))
    Data = pandas.DataFrame({
        "Employe Name":[Employe_name],
        "Employe Id":[Employe_Id],
        "Employe salary":[Employe_salary]
    })

    print(Data)
