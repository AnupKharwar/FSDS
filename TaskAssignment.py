# class
# object
# constructor
# inheritance
# private
# public
# protected
# abstraction
# encaptulations
# polymorpsim
# package
# modules
# method overrridding
#
# For all the concepts that we have discussed in our class point by point you have to write
# atleast 10 examples
#
# you have to make sure that use ineuron studnets , class , class type , number of courses
# , affiliates , blog, internship , jobs as a reference example

#  With Logging and Exception handling

import logging

class ineuron_ClassType:
    """Define the class type for Inueron cources"""
    def __init__(self , classtype, classduration, IsIntership):
        try:
            self.classtype = classtype
            self.classduration1 = classduration
            self.IsIntership = IsIntership
        except Exception as e:
            logging.exception(e)


    def classduration(self):
        print("Duration of " ,self.classtype ," course is : ", self.classduration1 )


class ineuron_student(ineuron_ClassType):
    def __init__(self,name,age,exp,classtype, classduration, IsIntership):
        try:
            ineuron_ClassType.__init__(self , classtype, classduration, IsIntership)
            self.name = name
            self.age = age
            self.exp = exp
        except Exception as e:
            logging.exception(e)


class ineuron_facility(ineuron_ClassType):
    def __init__(self,facilitator,classtype, classduration, IsIntership):
        try:
            ineuron_ClassType.__init__(self,classtype,classduration,IsIntership)
            self.facilitator = facilitator
            self.__facilitator_salary = "1 Cr"
        except Exception as e:
            logging.exception(e)

    def facilitator_info(self):
        print(self.classtype,"course has been taken by Mr. ",self.facilitator)


class ineuron_hackathon(ineuron_facility):
    def __init__(self,hackathon_name,facilitator,classtype, classduration, IsIntership):
        try:
            ineuron_facility.__init__(self,facilitator,classtype, classduration, IsIntership)
            self.hackathon_name = hackathon_name
        except Exception as e:
            logging.exception(e)

    def hackathon(self):
        print(self.hackathon_name," has been lead by Mr.",self.facilitator)

class ineuron_internship(ineuron_ClassType):
    try:

        def __init__(self,duration,classtype,classduration,IsIntership):
            ineuron_ClassType.__init__(self,classtype,classduration,IsIntership)
            self.internship_duration = duration
            self.__specialRequest = "Not available"

        def Internship_detail(self):
            if(self.IsIntership == "Yes"):
                print("Internship for course",self.classtype, " is ","for ",self.classduration1)
            else :
                print("Internship is ", self.__specialRequest ,"on special request for this course",self.classtype)

        def Internship_special_Request(self):
            if(self.classtype == "Data Analytics"):
                self.__specialRequest = "available"



    except Exception as e:
        logging.exception(e)


# Output
i = ineuron_ClassType("Data Analytics","1 year","Yes")
i.classduration()

j = ineuron_student("Anup","40","15","Data Science","1 Year","Yes")
j.classduration()

f = ineuron_facility("Sudhanshu","Data Science","1 Year","Yes")
f.facilitator_info()
print("Salary of Mr ",f.facilitator ," is ",f._ineuron_facility__facilitator_salary)

h=ineuron_hackathon("Hackathon 2.0","Sudhanshu","","","")
h.hackathon()

ii = ineuron_internship("1 Year","Data Science","1 year","Yes")
ii.Internship_detail()
ii = ineuron_internship("1 Year","Data Analytics","1 year","No")
ii.Internship_special_Request()
ii.Internship_detail()