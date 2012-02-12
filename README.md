=Spoon
There is no spoon. A Python properties system.

== Important Concepts
* make no assumption of framework or persistance layer

== Objective
Given some system, there exists a set of domain behaviors that are required and
a set of behaviors unknown at the present time. This is an invariant of
software development.

Construct a system that is flexable enough to accomodate for unknown
requirements at development time and simple enough to quickly add new
components when needed.

== Properties and DCI
Data, context and Interaction is a design pattern that is similar to what this
system does.

DCI is composed of:
* Context: Responsible for extending Actors and invoking Role behavior.
* Role: Extends Actors to provide use case functionality.
* Actor: Data objects that are extended and provide data for Roles.

In comparison:
* ObjectTemplate's are the Context as the extend Object's with some set of
  properties.
* Properties are Roles, the provide functionality to Objects.
* Object's are Actors. They are collections of Roles/Properties that can
  handle the call of duty.

Important Distictions
It is my goal to separate the system from any framework or presistance
mechanism:

* Actors must not be Models in the MVC sense - they cannot
be tied to a persistance layer or framework. They are object instances that
responde to events, wether in the form of method calls or triggered events.

* Context/ObjectTemplate should not assume persistance layers, e.g.:
    
    class SomeContext:
        def init(thing1_uid):
            # Don't do this, it assumes too much.
            thing1 = Thing.find(uid=thing1_uid)

            # instead, pass instances to contexts; it is the callers
            responsiblity to fetch their state.

* Properties: These simply perform duties on the objects the extend given the
  objects they are passed. Pretty simple.

=== System Naming Storm
Object/Property may be too vague; using Context/Role might ruffle feathers of
Pattern nazi's if I don't perfactly subscribe to some preconcieved notion
of the patterns implementation.

Context or Objects
* Object
* Context
* Entity
* Template
* Factory


== Quick Example
There is no bird: Develop a system to simulate birds.

? code in markdown ?

