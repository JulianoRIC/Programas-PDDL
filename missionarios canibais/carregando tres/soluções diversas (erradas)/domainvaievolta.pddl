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
 (atMboat ?m - missionary ?b - boat)
 (atCboat ?c - cannibal ?b - boat)
 (carryM ?m - missionary ?b - boat)
 (carryC ?c - cannibal ?b - boat)
)

(:functions (numberM ?s - side))
(:functions (numberC ?s - side))


;passa um canibal de um lado para outro
(:action OneCanGo  
 :parameters (?s1 ?s2 - side ?c - cannibal ?b - boat)
 :precondition(and(atC ?c ?s1) (at-emb ?s1))
 :effect(and(at-emb ?s2)(not(at-emb ?s1))(not(atC ?c ?s1))(not(empty ?b))(carryC ?c ?b)(atCboat ?c ?b))
)

;passa um missionario de um lado para outro
(:action OneMisGo  
 :parameters (?s1 ?s2 - side ?m - missionary ?b - boat)
 :precondition(and(atM ?m ?s1) (at-emb ?s1))
 :effect(and(at-emb ?s2)(not(at-emb ?s1))(not(atM ?m ?s1))(not(empty ?b))(carryM ?m ?b)(atMboat ?m ?b))
)

(:action desembarqueUmCanibal
 :parameters(?c - cannibal ?b - boat ?s - side )
 :precondition(and(not(empty ?b)) (at-emb ?s) (atCboat ?c ?b))
 :effect(and (empty ?b) (atC ?c ?s) (not(carryC ?c ?b)) (increase (numberC ?s) 1)(not(atCboat ?c ?b))) 
)

(:action desembarqueUmMissionario
 :parameters(?m - missionary ?b - boat ?s - side )
 :precondition(and(not(empty ?b)) (at-emb ?s) (atMboat ?m ?b))
 :effect(and (empty ?b)  (atM ?m ?s) (not(carryM ?m ?b)) (increase (numberM ?s) 1) (not(atMboat ?m ?b))) 
)
    
(:action BackToEmbark  
 :parameters (?s1 ?s2 - side)
 :precondition(at-emb ?s2)
 :effect(and(at-emb ?s1)(not(at-emb ?s2)))
)

)



 
 
 
 
 