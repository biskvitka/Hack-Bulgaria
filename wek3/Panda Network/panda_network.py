import re


class Panda:
    def __init__(self,name,email,gender):
        self.__name = name
        self.__email = email
        self.__gender = gender

    def validateEmail(self):
        if len(self.get_email()) > 7:
            if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", self.get_email()) != None:
                return True
        return False

    def __str__(self):
        return "I am {} {} panda and my email is {}".format(self.get_name(),self.get_gender(), self.get_email())

    def __eq__(self,other):
        return self.get_email() == other.get_email()

    def __hash__(self):
        return hash(self.__str__())

    def isMale(self):
        return self.get_gender() == "male"

    def isFemale(self):
        return self.get_gender() == "female"

    def get_email(self):
        return self.__email

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

class PandaSocialNetwork:
    pandas={}
    def __init__(self):
        self.network={}

    def add_panda(self,panda):
        if panda in self.network:
            raise Exception("panda already there")
        return self[panda]=()

    def has_panda(self,panda):
        return panda in self.network

    def are_friends(self,panda1,panda2):
        return panda1 in self.network[panda2] and panda2 in self.network[panda1]

    def make_friends(self,panda1,panda2):
        if not self.has_panda(panda1):
            self.add_panda(panda1)
        if not self.has_panda(panda2):
            self.add_panda(panda2)
        if self.are_friends(panda1,panda2):
            raise Exception("Pandas are already friends")

        self.network[panda1].append(panda2)
        self.network[panda2].append(panda1)

    def friends_of(self,panda):
        if panda in self.network:
            return panda in self.network
        return("This panda is not in the network")

    def connection_level(self,panda1,panda2):
        pass
