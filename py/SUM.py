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

# Example usage
if __name__ == "__main__":
    # Define users, objects, and policies
    user1 = User("Alice", role="Manager")
    user2 = User("Bob", role="Employee")

    object1 = Object("ProjectPlan", sensitivity_level=2)
    object2 = Object("EmployeeData", sensitivity_level=3)

    policy1 = Policy("Policy1", allowed_roles=["Manager"], required_sensitivity_level=3)
    policy2 = Policy("Policy2", allowed_roles=["Employee", "Manager"], required_sensitivity_level=2)

    # Initialize the access control system and add entities
    acs = AccessControlSystem()
    acs.add_user(user1)
    acs.add_user(user2)
    acs.add_object(object1)
    acs.add_object(object2)
    acs.add_policy(policy1)
    acs.add_policy(policy2)

    # Validate access multiple times to demonstrate functionality
    for _ in range(5):
        acs.validate_access()
