(define (domain pass_boat)
 
 (:requirements
  :strips
  :typing 
 )
 
(:types side cannibal boat)

(:predicates
 (at-emb ?s - side)
 (atC ?c - cannibal ?s - side)
 (empty ?b - boat)
 (carry ?p - passenger ?b - boat)
)


;passa um canibal de um lado para outro
(:action vai  
 :parameters (?s1 ?s2 - side ?c - cannibal ?b - boat)
 :precondition(and(atC ?c ?s1) (at-emb ?s1))
 :effect(and(at-emb ?s2)(not(at-emb ?s1))(atC ?c ?s2)(empty ?b))
)

(:action volta  
 :parameters (?s1 ?s2 - side)
 :precondition(at-emb ?s2)
 :effect(and(at-emb ?s1)(not(at-emb ?s2)))
)

)



 
 
 
 
 