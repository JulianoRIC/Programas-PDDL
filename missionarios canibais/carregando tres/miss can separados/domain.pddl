(define (domain pass_boat)
 
 (:requirements
  :strips
  :typing 
  :conditional-effects
  :equality 
 )
 
(:types side missionary cannibal boat)

(:predicates
 (at-emb ?s - side)
 (atC ?c - cannibal   ?s - side)
 (atM ?m - missionary ?s - side)
 (empty  ?b - boat)
 (carryC ?c - cannibal   ?b - boat)
 (carryM ?m - missionary ?b - boat)
)


;passa um passageiro de um lado para outro
(:action pass  
 :parameters (?s1 ?s2 - side ?b ?b2 - boat)
 :precondition(and(at-emb ?s1)(or (not(empty ?b)) (not(empty ?b2)))) 
 :effect(and(at-emb ?s2) (not(at-emb ?s1)))
)

(:action embarkC 
 :parameters(?c - cannibal ?s - side ?b - boat)
 :precondition(and(atC ?c ?s) (at-emb ?s) (empty ?b) );(not(atC ?c ?s))) ;(not(= ?c ?c2)))
 :effect(and(carryC ?c ?b) (not(atC ?c ?s)) (not(empty ?b)))
)

(:action disembarkC
 :parameters(?c - cannibal ?s - side ?b - boat)
 :precondition(and(carryC ?c ?b) (at-emb ?s))
 :effect(and(atC ?c ?s) (empty ?b) (not(carryC ?c ?b)))
)

(:action embarkM 
 :parameters(?m - missionary ?s - side ?b - boat)
 :precondition(and(atM ?m ?s) (at-emb ?s) (empty ?b)) ;(not(= ?m ?m2)))
 :effect(and(carryM ?m ?b) (not(atM ?m ?s)) (not(empty ?b)))
)

(:action disembarkM
 :parameters(?m - missionary ?s - side ?b - boat)
 :precondition(and(carryM ?m ?b) (at-emb ?s))
 :effect(and(atM ?m ?s) (empty ?b) (not(carryM ?m ?b)))
)

)




 
 
 
 
 