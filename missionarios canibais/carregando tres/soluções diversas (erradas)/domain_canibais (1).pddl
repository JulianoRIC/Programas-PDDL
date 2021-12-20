(define (domain pass_boat)
 
 (:requirements
  :strips
  :typing 
 )
 
(:types side cannibal missionary boat)

(:predicates
 (at-emb ?s - side)
 (atC ?c - cannibal ?s - side)
 (empty ?b - boat)
 (atM ?m - missionary  ?s - side)
)


;passa um canibal de um lado para outro
(:action OneCanGo  
 :parameters (?s1 ?s2 - side ?c - cannibal ?b - boat)
 :precondition(and(atC ?c ?s1) (at-emb ?s1))
 :effect(and(at-emb ?s2)(not(at-emb ?s1))(atC ?c ?s2)(empty ?b))
)

;passa um missionario de um lado para outro
(:action OneMisGo  
 :parameters (?s1 ?s2 - side ?m - missionary ?b - boat)
 :precondition(and(atM ?m ?s1) (at-emb ?s1))
 :effect(and(at-emb ?s2)(not(at-emb ?s1))(atM ?m ?s2)(empty ?b))
)

(:action TwoCanGo  
 :parameters (?s1 ?s2 - side ?c ?c2 - cannibal ?b - boat)
 :precondition(and(atC ?c ?s1)(atC ?c2 ?s1) (at-emb ?s1))
 :effect(and(at-emb ?s2)(not(at-emb ?s1))(atC ?c ?s2)(atC ?c2 ?s2)(empty ?b))
)

(:action TwoMisGo  
 :parameters (?s1 ?s2 - side ?m ?m2 - missionary ?b - boat)
 :precondition(and(atM ?m ?s1)(atM ?m2 ?s1) (at-emb ?s1))
 :effect(and(at-emb ?s2)(not(at-emb ?s1))(atM ?m ?s2)(atM ?m2 ?s2)(empty ?b))
)

(:action OneMOneC  
 :parameters (?s1 ?s2 - side ?m - missionary ?c - cannibal ?b - boat)
 :precondition(and(atM ?m ?s1)(atC ?c ?s1) (at-emb ?s1))
 :effect(and(at-emb ?s2)(not(at-emb ?s1))(atM ?m ?s2)(atC ?c ?s2)(empty ?b))
)

(:action BackToEmbark  
 :parameters (?s1 ?s2 - side)
 :precondition(at-emb ?s2)
 :effect(and(at-emb ?s1)(not(at-emb ?s2)))
)

)



 
 
 
 
 