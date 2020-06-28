import pandas as pd 


class Person(object):
    def __init__(self, firstName, lastName, age, email):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.email = email

    def print_person(self):   
        print('\nInside print_person: \n' + 'Person: ' 
            + self.firstName + ' ' 
            + self.lastName + ' ' 
            + self.age + ' ' 
            + self.email)

# def print_people_DF(df):
#     # df = pd.DataFrame(df)
#     print(df)

people = {"firstName": ["Foo", "Biz", "Bing"], 
                "lastName": ["Bar", "Baz", "Bang"], 
                "age": ["30", "45", "67"],
                "email": ["FooBar@test.com", "BizBaz@test.com", "BingBang@test.com"]}
people_df = pd.DataFrame(people)
print(people_df)

new_people_objs = [Person(**kwargs) for kwargs in people_df.to_dict(orient='records')]

for p in new_people_objs:
    p.print_person()

# print(new_people_objs[0].firstName + ' ' + new_people_objs[0].lastName)

# p2 = new_people_objs[2]

# p2.print_person()


# new_people_df = pd.DataFrame(new_people)

# print_people_DF(new_people_df)


# p1 = Person(people_df.loc[0, 'firstName'], people_df['lastName'], people_df['age'], people_df['email'])
# print(p1.firstName)
# p1 = pd.DataFrame(p1)
# p1.print_person_DF(p1)