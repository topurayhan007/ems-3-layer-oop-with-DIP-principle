from application_layer.interfaces.repository_interface import IRepository
from abc import abstractmethod
from typing import List, Dict

class IEmployeeRepository(IRepository):
    @abstractmethod
    def search(self, input_text):
        pass

    @abstractmethod
    def get_all(self) -> List[Dict]:
        pass