class Person:
    voting_age = 18
    can_vote = False
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.check_vote()

    def check_vote(self):
        if self.age >= self.voting_age:
            self.can_vote = True
        else:
            self.can_vote = False
    
    def info(self):
        s = f"{self.name} can't vote"
        if p.can_vote:
            s = f"{self.name} can vote"
        print(f"{self.name} is {self.age} years old. {s}")


if __name__ == '__main__':
    people = []

    people.append(Person('Alex', 32))
    people.append(Person('Charlie', 16))

    for p in people:
        p.info()

