from sqlalchemy import create_engine
from sqlalchemy.sql import text


class EmployeeTable:
    __scripts = {
        "create company": text("insert into company( name, description) values(:name, :description)"),
        "get max id company": text("select MAX(\"id\") from company"),
        "delete company": text("delete from company where id =:id_to_delete"),
        "list SELECT": text("select * from employee where id =:company_id"),
        "item SELECT": text("select * from employee where company_id =:company_id и id =:employee_id"),
        "maxID SELECT": text("select MAX(id) from employee where company_id = company_id"),
        "item DELETE": text("delete from employee where id =:id_to_delete"),
        "item UPDATE": text("update employee set first_name =:new_name where id =:employee_id"),
        "item INSERT": text("insert into employee(company_id, first_name, last_name, phone) values(:id, :name, :surname,:phone_num)")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def create_company(self, company_name: str, descr: str):
        return self.__db.execute(self.__scripts["create company"], name=company_name, description=descr)

    def get_max_id_company(self):
        return self.__db.execute(self.__scripts["get max id company"]).fetchall()[0][0]
    
    def delete(self, id: int):
        self.__db.execute(self.__scripts["delete company"], id_to_delete=id)

    def get_employee_list(self, id: int):
        return self.__db.execute(self.__scripts["list SELECT"], company_id=id).fetchall()
    
    def get_employee_by_id(self, company_id: int, id: int):
        return self.__db.execute(self.__scripts["item SELECT"], company_id=company_id, employee_id=id).fetchall()

    def get_max_id_employee(self, company_id: int):
        return self.__db.execute(self.__scripts["maxID SELECT"], company_id=company_id).fetchall()[0][0]

    def delete_employee(self, id: int):
        self.__db.execute(self.__scripts["item DELETE"], id_to_delete=id)

    def create_new_employee(self, company_id: int, first_name: str, last_name: str, phone: str):
        return self.__db.execute(self.__scripts["item INSERT"], id=company_id, name=first_name, surname=last_name, phone_num=phone)

    def update_employee(self, new_name: str, id: int):
        return self.__db.execute(self.__scripts["item UPDATE"], new_name=new_name, employee_id=id)