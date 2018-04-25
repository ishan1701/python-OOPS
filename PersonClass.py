import logging
logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler=logging.StreamHandler()

formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

class Employee:
    def splitName(self,name):
        try:
            fname=name.split(" ")[0]
            lname=name.split(" ")[1]
        except Exception as e:
            logger.error(e)
            exit(1)
        return (fname,lname)
    def __init__(self,name,ssn,age):
        logger.info("Indside Person Class")
        self.fname,self.lname=self.splitName(name)
        self.__aadhar=ssn
        self._age=age
    @property
    def age(self):
        logger.info(self._age)
    @age.setter
    def age(self,newage):
        self._age=newage
    def printDetails(self):
        print(self.fname,self.lname,self.__aadhar,self._age)
