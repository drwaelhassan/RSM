package main

import "fmt"

type User struct {
    ID   string
    Role string
}

type Object struct {
    ID         string
    SecrecyLevel string
}

type Policy struct {
    Role        string
    SecrecyLevel string
    AllowAccess bool
}

var policies []Policy
var users []User
var objects []Object
func init() {
    policies = []Policy{
        {Role: "Admin", SecrecyLevel: "High", AllowAccess: true},
        {Role: "User", SecrecyLevel: "Low", AllowAccess: true},
        {Role: "Guest", SecrecyLevel: "Low", AllowAccess: false},
        // Add more policies as needed
    }

    users = []User{
        {ID: "user1", Role: "Admin"},
        {ID: "user2", Role: "User"},
        // Add more users as needed
    }

    objects = []Object{
        {ID: "object1", SecrecyLevel: "High"},
        {ID: "object2", SecrecyLevel: "Low"},
        // Add more objects as needed
    }
}
func canAccess(userID, objectID string) bool {
    var userRole, objectSecrecyLevel string

    // Find user role
    for _, u := range users {
        if u.ID == userID {
            userRole = u.Role
            break
        }
    }

    // Find object secrecy level
    for _, obj := range objects {
        if obj.ID == objectID {
            objectSecrecyLevel = obj.SecrecyLevel
            break
        }
    }

    // Check policies
    for _, policy := range policies {
        if policy.Role == userRole && policy.SecrecyLevel == objectSecrecyLevel {
            return policy.AllowAccess
        }
    }

    return false
}
func main() {
    fmt.Println("Access Check 1 (Admin to High):", canAccess("user1", "object1"))
    fmt.Println("Access Check 2 (User to Low):", canAccess("user2", "object2"))
    fmt.Println("Access Check 3 (User to High):", canAccess("user2", "object1"))
}
