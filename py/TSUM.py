# Author: Wael Hassan

# Basic entities for RBAC (Role-Based Access Control)

class User:
  """
  Represents a user in the RBAC system.

  Attributes:
      user_id (str): Unique identifier for the user.
      name (str): Name of the user.
  """
  def __init__(self, user_id, name):
    self.user_id = user_id
    self.name = name

class Role:
  """
  Represents a role within the RBAC system.

  Attributes:
      role_id (str): Unique identifier for the role.
      name (str): Name of the role.
  """
  def __init__(self, role_id, name):
    self.role_id = role_id
    self.name = name

class Permission:
  """
  Represents a permission granted within the RBAC system.

  Attributes:
      permission_id (str): Unique identifier for the permission.
      description (str): Description of the permission.
  """
  def __init__(self, permission_id, description):
    self.permission_id = permission_id
    self.description = description

class Operation:
  """
  Represents an operation that can be performed within the RBAC system.

  Attributes:
      operation_id (str): Unique identifier for the operation.
      name (str): Name of the operation.
  """
  def __init__(self, operation_id, name):
    self.operation_id = operation_id
    self.name = name

class RBAC_Object:
  """
  Represents an object that can be accessed within the RBAC system.

  Attributes:
      object_id (str): Unique identifier for the object.
      name (str): Name of the object.
  """
  def __init__(self, object_id, name):
    self.object_id = object_id
    self.name = name


def transform_subjects_to_roles_users(subjects):
  """
  Transforms a dictionary of subjects with their roles and optional user mappings
  into separate dictionaries for roles and users.

  Args:
      subjects (dict): Dictionary where keys are subjects and values are dictionaries
          containing 'roles' (list of roles) and optionally 'user' (username).

  Returns:
      tuple: A tuple containing two dictionaries, the first with roles and the second with users.
  """
  roles = {subject: details.get('roles', []) for subject, details in subjects.items()}
  users = {subject: details.get('user') for subject, details in subjects.items() if 'user' in details}
  return roles, users

def transform_verbs_to_operations_permissions(verbs):
  """
  Transforms a dictionary of verbs with their corresponding operations and permissions
  into a single dictionary with operations as keys and permission details as values.

  Args:
      verbs (dict): Dictionary where keys are verbs and values are lists of tuples.
          Each tuple represents an operation applied to an object with its corresponding permission.

  Returns:
      dict: Dictionary with operations as keys and permission details as values.
  """
  operations_permissions = {verb: details for verb, details in verbs.items()}
  return operations_permissions

def transform_objects_to_rbac_objects(objects):
  """
  Transforms a dictionary of SVO (Subject-Verb-Object) objects into RBAC objects.

  Args:
      objects (dict): Dictionary where keys are objects and values are lists containing
          additional details (implementation specific).

  Returns:
      dict: Dictionary with RBAC objects as keys and their details as values.
  """
  rbac_objects = {obj: details for obj, details in objects.items()}
  return rbac_objects


# Example SVO to RBAC transformation
subjects = {
  's1': {'roles': ['r1', 'r2'], 'user': 'u1'}
}

verbs = {
  'v1': [('o1', 'p1'), ('o2', 'p2')]
}

objects = {
  'o1': ['obj1', 'obj2']
}

# Transformation
roles, users = transform_subjects_to_roles_users(subjects)
operations_permissions = transform_verbs_to_operations_permissions(verbs)
rbac_objects = transform_objects_to_rbac_objects(objects)

# Printing transformed entities
