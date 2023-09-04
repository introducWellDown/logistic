import bd_manager as bd

def show_Users():
    bd.show_pleer_bd("Users")
    
def show_Worker():
    bd.show_pleer_bd("Worker")
    
#bd.add_company_with_code("Company_2","54321")
#bd.add_company_with_code("Company_1","12345")
show_Users()
show_Worker()