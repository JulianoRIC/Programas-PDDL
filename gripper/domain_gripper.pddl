(define (domain gripper)
 
 (:requirements
  :strips
  :typing 
 )
 
 ( :types room ball gripper)
 
 ( :predicates
   (at-robby ?r - room)
   (at ?b - ball ?r - room)
   (free ?g - gripper)
   (carry ?b - ball ?g - gripper)
 )
 
 (:action move
  :parameters (?r1 ?r2 - room)
  :precondition (at-robby ?r1)
  :effect (and(at-robby ?r2)(not(at-robby ?r1)))
 )
 
 (:action pick
  :parameters (?b - ball ?r - room ?g - gripper)
  :precondition (and(at ?b ?r)(at-robby ?r) (free ?g)) 
  :effect (and(carry ?b ?g) (not(at ?b ?r)) (not(free ?g))) 
 )
 
 (:action drop
  :parameters (?b - ball ?r - room ?g - gripper)
  :precondition (and(carry ?b ?g) (at-robby ?r))
  :effect (and(at ?b ?r) (free ?g) (not(carry ?b ?g)))
 )
)