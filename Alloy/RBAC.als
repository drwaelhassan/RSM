// This code implements a Role-Based Access Control (RBAC) policy system
// Author: Wael Hassan ([email address removed])

module rbacSecrecyPolicy

// Define basic entities
sig User {
  roles: some Role
}

sig Role {}

sig Object {}

sig Policy {
  permittedRoles: some Role,
  targetObjects: some Object
}

// Relationships and access control
sig Access {
  user: one User,
  object: one Object,
  policy: one Policy
}

// Define a relationship to check if a user has access to an object through a policy
pred hasAccess[u: User, o: Object, p: Policy] {
  u.roles & p.permittedRoles != none
  and o in p.targetObjects
}

// Secrecy policies examples
// Policy that specifies only users with a certain role can access specific objects
fact RoleBasedAccessControl {
  all u: User, o: Object | hasAccess[u, o, Policy] implies (u.roles & o.policy.permittedRoles != none)
}

// Access validation feature
// Validate if a randomly selected user has access to a specified object
assert UserAccessValidation {
  all u: User, o: Object | hasAccess[u, o, Policy] implies some a: Access | a.user = u and a.object = o and a.policy = Policy
}

check UserAccessValidation for 4

// Visualization and examples
// Example to demonstrate how users are granted or denied access to objects based on policies
run {
  some u: User, o: Object | hasAccess[u, o, Policy]
} for 4 but 3 User, 4 Object, 2 Policy, 3 Role

