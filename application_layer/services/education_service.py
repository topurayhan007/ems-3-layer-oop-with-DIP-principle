from application_layer.classes.education import EducationalDegree
from application_layer.interfaces.database_manager_interface import IDatabaseManager
from database_layer.storage_managers.education_db_manager import EducationDBManager
from application_layer.interfaces.education_service_interface import IEducationService

class EducationService(IEducationService):
    def __init__(self, db_manager: IDatabaseManager):
        self.db_manager = db_manager
        self.education_db_manager = EducationDBManager(db_manager)

    def add_degree(self, degree: EducationalDegree):
        result = self.education_db_manager.add_degree(degree)
        return result

    def search_degrees_of_an_employee(self, employee_id):
        degrees = self.education_db_manager.search_degrees_of_an_employee(employee_id)
        return degrees

    def delete_a_degree_of_an_employee(self, degree_id):
        result = self.education_db_manager.delete_a_degree_of_an_employee(degree_id)
        return result

    def update_a_degree_of_an_employee(self, degree: EducationalDegree):
        result = self.education_db_manager.update_a_degree_of_an_employee(degree)
        return result