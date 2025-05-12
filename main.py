import os
from dotenv import load_dotenv
from database_layer.db_setup import DatabaseManager
from application_layer.services.employee_service import EmployeeService
from application_layer.services.education_service import EducationService
from application_layer.services.experience_service import ExperienceService
from presentation_layer.cli_controllers.employee_cli_controller import EmployeeCliController
from presentation_layer.cli_controllers.education_cli_controller import EducationCliController
from presentation_layer.cli_controllers.experience_cli_controller import ExperienceCliController
from presentation_layer.cli_ui import CLI
from application_layer.interfaces.database_manager_interface import IDatabaseManager
from application_layer.interfaces.employee_service_interface import IEmployeeService
from application_layer.interfaces.education_service_interface import IEducationService
from application_layer.interfaces.experience_service_interface import IExperienceService

load_dotenv()

config = {
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'host': os.getenv("DB_HOST"),
    'database': os.getenv("DB_NAME"),
    'raise_on_warnings': True
}

def main(employee_service: IEmployeeService, education_service: IEducationService, experience_service: IExperienceService):

    # Cli Controller objects
    education_cli_controller = EducationCliController(education_service)
    experience_cli_controller = ExperienceCliController(experience_service)
    employee_cli_controller = EmployeeCliController(employee_service, education_cli_controller, experience_cli_controller)

    # Start the CLI
    cli = CLI(employee_cli_controller, education_cli_controller, experience_cli_controller)
    cli.run()


if __name__ == "__main__":
    db_manager = DatabaseManager(config)
    try:
        db_manager.initialize_database()
    except Exception as e:
        print(f"Database initialization failed: {e}")
        exit(1)

    # Services objects
    employee_service = EmployeeService(db_manager)
    education_service = EducationService(db_manager)
    experience_service = ExperienceService(db_manager)

    main(employee_service, education_service, experience_service)