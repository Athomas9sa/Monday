class Person:
    def __init__(self, name, email, phone):
         self.name = name
         self.email = email
         self.phone = phone

    def greet(self, other_person):
        print('Hello %s, I am %s!' % (other_person.name, self.name))

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jardan@aol.com", "495-586-3456")

sonny.greet(jordan)
jordan.greet(sonny)

print("Sonny's contact info:" + sonny.email, sonny.phone)
print("Sonny's contact info:" + sonny.email, sonny.phone)

