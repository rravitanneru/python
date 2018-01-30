# abstract class is a class but can't be intiated like normal case but sub-classess of an abstract class can be intiated

from abc import ABC, abstractmethod
class employee(ABC):
    @abstractmethod
    def cal_sali(self,sal):
        pass

class ravi(employee):
    def cal_sali(self,sal):
        finalsalary = sal * 1.05
        return  finalsalary


std_1 = ravi()
print(std_1.cal_sali(10000))


        


