import json
import random

# Define basic entities
class User:
    def __init__(self, name, role=None):
        self.name = name
        self.role = role  # User's role in the organization

class Object:
    def __init__(self, name, sensitivity_level):
        self.name = name
        self.sensitivity_level = sensitivity_level  # Sensitivity level of the object

class Policy:
    def __init__(self, policy_id, allowed_roles, required_sensitivity_level):
        self.policy_id = policy_id
        self.allowed_roles = allowed_roles  # Roles allowed by this policy
        self.required_sensitivity_level = required_sensitivity_level  # Required sensitivity level for access

    def can_access(self, user, obj):
        # Determine if the user can access the object based on this policy
        return user.role in self.allowed_roles and obj.sensitivity_level <= self.required_sensitivity_level

class AccessControlSystem:
    def __init__(self):
        self.policies = []
        self.users = []
        self.objects = []

    def add_policy(self, policy):
        self.policies.append(policy)

    def add_user(self, user):
        self.users.append(user)

    def add_object(self, obj):
        self.objects.append(obj)

    def validate_access(self):
        # Randomly select a user and an object
        user = random.choice(self.users)
        obj = random.choice(self.objects)

        # Check policies to determine if access should be granted
        access_granted = any(policy.can_access(user, obj) for policy in self.policies)
        
        print(f"User '{user.name}' with role '{user.role}' attempting to access '{obj.name}' (Sensitivity: {obj.sensitivity_level}): {'Access Granted' if access_granted else 'Access Denied'}")

# Load JSON data from file
file_path = "Input/LLMOpsPolicies.json"
with open(file_path, "r") as file:
    json_data = json.load(file)

# Extract policy data and create Policy objects
policy_data = json_data["policies"]
policies = []
for policy_info in policy_data:
    subject = policy_info["subject"]["name"]
    allowed_roles = policy_info["allowable_purposes"]
    required_sensitivity_level = len(policy_info["processing_types"]) # Just a placeholder value
    policy = Policy(subject, allowed_roles, required_sensitivity_level)
    policies.append(policy)

# Example usage
if __name__ == "__main__":
    # Initialize the access control system and add entities
    acs = AccessControlSystem()

    # Define users and objects
    user1 = User("Alice", role="Manager")
    user2 = User("Bob", role="Employee")
    acs.add_user(user1)
    acs.add_user(user2)

    object1 = Object("ProjectPlan", sensitivity_level=2)
    object2 = Object("EmployeeData", sensitivity_level=3)
    acs.add_object(object1)
    acs.add_object(object2)

    # Add policies to the access control system
    for policy in policies:
        acs.add_policy(policy)

    # Validate access multiple times to demonstrate functionality
    for _ in range(5):
        acs.validate_access()
