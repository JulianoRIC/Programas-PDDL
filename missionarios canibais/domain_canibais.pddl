(define (domain pass_boat)
 
 (:requirements
  :strips
  :typing 
 )
 
(:types side passenger boat)

(:predicates
 (at-emb ?s - side)
 (at ?p - passenger ?s - side)
 (empty ?b - boat)
 (carry ?p - passenger ?b - boat)
)


;passa um passageiro de um lado para outro
(:action pass  
 :parameters (?s1 ?s2 - side)
 :precondition(at-emb ?s1)
 :effect(and(at-emb ?s2) (not(at-emb ?s1)))
)

(:action embark
 :parameters(?p - passenger ?s - side ?b - boat)
 :precondition(and(at ?p ?s) (at-emb ?s) (empty ?b))
 :effect(and(carry ?p ?b) (not(at ?p ?s)) (not(empty ?b)))
)

(:action disembark
 :parameters(?p - passenger ?s - side ?b - boat)
 :precondition(and(carry ?p ?b) (at-emb ?s))
 :effect(and(at ?p ?s) (empty ?b) (not(carry ?p ?b)))
)

)



 
 
 
 
 