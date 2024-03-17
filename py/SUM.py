# Import the random module for random selection
import random

# --- Define core entities ---

# Define a class to represent a user in the system
class User:
   """
   Represents a user with a name and optional role.
   """

   def __init__(self, name, role=None):
       """
       Initializes a User object.

       Args:
           name (str): The name of the user.
           role (str, optional): The user's role in the organization. Defaults to None.
       """

       self.name = name  # Store the user's name
       self.role = role  # Store the user's role (optional)

# Define a class to represent an object with a sensitivity level
class Object:
   """
   Represents a protected object with a name and sensitivity level.
   """

   def __init__(self, name, sensitivity_level):
       """
       Initializes an Object object.

       Args:
           name (str): The name of the object.
           sensitivity_level (int): The sensitivity level of the object (higher means more sensitive).
       """

       self.name = name  # Store the object's name
       self.sensitivity_level = sensitivity_level  # Store the object's sensitivity level

# Define a class to model an access control policy
class Policy:
   """
   Represents an access control policy with allowed roles and sensitivity requirements.
   """

   def __init__(self, policy_id, allowed_roles, required_sensitivity_level):
       """
       Initializes a Policy object.

       Args:
           policy_id (str): A unique identifier for the policy.
           allowed_roles (list): A list of roles allowed to access objects under this policy.
           required_sensitivity_level (int): The maximum allowed sensitivity level for objects under this policy.
       """

       self.policy_id = policy_id  # Store the policy's identifier
       self.allowed_roles = allowed_roles  # Store the allowed roles
       self.required_sensitivity_level = required_sensitivity_level  # Store the maximum allowed sensitivity level

   def can_access(self, user, obj):
       """
       Determines if the user can access the object based on this policy.

       Args:
           user (User): The user attempting access.
           obj (Object): The object being accessed.

       Returns:
           bool: True if the user can access the object, False otherwise.
       """

       return user.role in self.allowed_roles and obj.sensitivity_level <= self.required_sensitivity_level

# --- Implement access control system ---

class AccessControlSystem:
   """
   Manages a set of policies, users, and objects to control access.
   """

   def __init__(self):
       """
       Initializes an AccessControlSystem object.
       """

       self.policies = []  # Store a list of policies
       self.users = []  # Store a list of users
       self.objects = []  # Store a list of protected objects

   def add_policy(self, policy):
       """
       Adds a policy to the access control system.

       Args:
           policy (Policy): The policy to add.
       """

       self.policies.append(policy)  # Add the policy to the list

   def add_user(self, user):
       """
       Adds a user to the access control system.

       Args:
           user (User): The user to add.
       """

       self.users.append(user)  # Add the user to the list

   def add_object(self, obj):
       """
       Adds an object to the access control system.

       Args:
           obj (Object): The object to add.
       """

       self.objects.append(obj)  # Add the object to the list

   def validate_access(self):
       """
       Validates access by randomly selecting a user and object and checking permissions against policies.
       """

       # Randomly select a user and object
       user = random.choice(self.users)  # Choose a random user
       obj = random.choice(self.objects)  # Choose a random object

       # Check policies to determine if access should be granted
       access_granted = any(policy.can_access(user, obj) for policy in self.policies)  #
