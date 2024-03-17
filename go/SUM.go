package main

import "fmt"

// Subject represents a subject in the model
type Subject struct {
    Name string
}

// Verb represents an action or right in the model
type Verb struct {
    Action string
}

// Object represents an object or item in the model
type Object struct {
    Item string
}

// Relationship ties together a Subject, Verb, and Object
type Relationship struct {
    Subject Subject
    Verb    Verb
    Object  Object
}

// IsActionPermitted prints the relationship for simplicity
func (r *Relationship) IsActionPermitted() {
    fmt.Printf("Subject '%s' has the action '%s' on object '%s'.\n",
        r.Subject.Name, r.Verb.Action, r.Object.Item)
}

// Policy contains multiple relationships
type Policy struct {
    Relationships []Relationship
}

// AddRelationship adds a new relationship to the policy
func (p *Policy) AddRelationship(r Relationship) {
    p.Relationships = append(p.Relationships, r)
}

// EvaluatePolicies evaluates all relationships in the policy
func (p *Policy) EvaluatePolicies() {
    for _, relationship := range p.Relationships {
        relationship.IsActionPermitted()
    }
}

func main() {
    // Example usage
    subject1 := Subject{Name: "UserA"}
    verb1 := Verb{Action: "read"}
    object1 := Object{Item: "FileX"}

    relationship1 := Relationship{Subject: subject1, Verb: verb1, Object: object1}

    policy := Policy{}
    policy.AddRelationship(relationship1)

    policy.EvaluatePolicies()
}
