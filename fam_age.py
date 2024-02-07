#1
class person:
    def __init__(self,name,country,DOB):
        self.name = name
        self.country = country
        self.DOB = int(DOB)
    def age_of_person(self):
        age=2024-self.DOB
        print(f"the age of{self.name } is {age}")

person1=person("shruti","india",'2005')
person2=person("dhruv","india",'2006')
person3=person("shubh","india",'2012')
print("person1:")
print("Name:",person1.name)
print("country:",person1.country)
print("DOB:",person1.DOB)
print(person1.age_of_person())
print("person2:")
print("Name:",person2.name)
print("country:",person2.country)
print("DOB:",person2.DOB)
print(person2.age_of_person())
print("person3:")
print("Name:",person3.name)
print("country:",person3.country)
print("DOB:",person3.DOB)
print(person3.age_of_person())
