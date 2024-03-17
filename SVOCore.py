class Subject:
    def __init__(self, name):
        self.name = name

class Verb:
    def __init__(self, action):
        self.action = action

class Object:
    def __init__(self, item):
        self.item = item

class Relationship:
    def __init__(self, subject, verb, obj):
        self.subject = subject
        self.verb = verb
        self.obj = obj

    def is_action_permitted(self):
        # This method can be expanded based on specific rules or conditions
        # For simplicity, we'll just print the relationship for now
        print(f"Subject '{self.subject.name}' has the action '{self.verb.action}' on object '{self.obj.item}'.")

class Policy:
    def __init__(self):
        self.relationships = []

    def add_relationship(self, relationship):
        self.relationships.append(relationship)

    def evaluate_policies(self):
        for relationship in self.relationships:
            relationship.is_action_permitted()

# Example Usage
subject1 = Subject("UserA")
verb1 = Verb("read")
object1 = Object("FileX")

relationship1 = Relationship(subject1, verb1, object1)

policy = Policy()
policy.add_relationship(relationship1)

policy.evaluate_policies()
