class person:
    def __init__(self, phone_number , email , home_addres , office_number , office_addres , neat_print):
        self.phone_number = phone_number
        self.email = email
        self.home_addres = home_addres
        self.office_number = office_number
        self.office_addres = office_addres
        self.neat_print = neat_print
        self.phone_number = input("Enter your phone number : " )
        self.email = input("Enter your email addres : " )
        self.home_addres = input("Enter your home addres : " )
        self.office_number = input("Enter your office number : " )
        self.office_addres = input("Enter your office addres : " )
        self.neat_print = (f"your phone number is {phone_number} \n your email addres is {email} \n your home addres is {home_addres} \n your office number is {office_number} 
                           \n your office addres is {office_addres}")
        print(neat_print)