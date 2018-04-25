from PersonClass import Employee
import logging
logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler=logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

class Developer(Employee):
    def __init__(self,name,ssn,age,lang):
        logger.info("Inside Dedveloper cons")
        super().__init__(name,ssn,age)
        self.prog=lang
    def getDetails(self):
        logger.info('%s %s %s',self.fname,self.lname,self.prog)
def main():
    d1=Developer("Ishan Kumr",233,29,"Scala")
    d1.getDetails()
    d1.printDetails()
    d1.age=100
    d1.getDetails()
    d1.printDetails()
if __name__=='__main__':
    main()