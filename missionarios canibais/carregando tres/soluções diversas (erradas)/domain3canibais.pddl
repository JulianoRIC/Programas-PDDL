(define (domain pass_boat)
 
 (:requirements
  :strips
  :typing 
 )
 
(:types side can1 can2 can3 mis1 mis2 mis3 boat)

(:predicates
 (at-emb ?s - side)
 (atC1 ?c   - can1 ?s - side)
 (atC2 ?c2  - can2 ?s - side)
 (atC3 ?c3  - can3 ?s - side)
 (atM1 ?m   - mis1 ?s - side)
 (atM2 ?m2  - mis2 ?s - side)
 (atM3 ?m3  - mis3 ?s - side)
 (empty ?b - boat)
 ;(carry ?p - passenger ?b - boat)
)


;passa um canibal de um lado para outro
(:action GOC1  
 :parameters (?s1 ?s2 - side ?c - can1 ?b - boat)
 :precondition(and(atC1 ?c ?s1) (at-emb ?s1))
 :effect(and(at-emb ?s2)(not(at-emb ?s1))(atC1 ?c ?s2)(empty ?b))
)

(:action GOC2 
 :parameters (?s1 ?s2 - side ?c2 - can2 ?b - boat)
 :precondition(and(atC2 ?c2 ?s1) (at-emb ?s1))
 :effect(and(at-emb ?s2)(not(at-emb ?s1))(atC2 ?c2 ?s2)(empty ?b))
)

(:action GOC3 
 :parameters (?s1 ?s2 - side ?c3 - can3 ?b - boat)
 :precondition(and(atC3 ?c3 ?s1) (at-emb ?s1))
 :effect(and(at-emb ?s2)(not(at-emb ?s1))(atC3 ?c3 ?s2)(empty ?b))
)

(:action GOC1C2 
 :parameters (?s1 ?s2 - side ?c1 - can1 ?c2 - can2 ?b - boat)
 :precondition(and(at-emb ?s1)(atC1 ?c1 ?s1)(atC2 ?c2 ?s1))
 :effect(and(at-emb ?s2)(not(at-emb ?s1))(atC1 ?c1 ?s2)(atC2 ?c2 ?s2)(empty ?b))
)

(:action GOM1  
 :parameters (?s1 ?s2 - side ?m - mis1 ?b - boat)
 :precondition(and(atM1 ?m ?s1) (at-emb ?s1))
 :effect(and(at-emb ?s2)(not(at-emb ?s1))(atM1 ?m ?s2)(empty ?b))
)

(:action GOM2  
 :parameters (?s1 ?s2 - side ?m2 - mis2 ?b - boat)
 :precondition(and(atM2 ?m2 ?s1) (at-emb ?s1))
 :effect(and(at-emb ?s2)(not(at-emb ?s1))(atM2 ?m2 ?s2)(empty ?b))
)

(:action GOM3  
 :parameters (?s1 ?s2 - side ?m3 - mis3 ?b - boat)
 :precondition(and(atM3 ?m3 ?s1) (at-emb ?s1))
 :effect(and(at-emb ?s2)(not(at-emb ?s1))(atM3 ?m3 ?s2)(empty ?b))
)

(:action GOM1M2 
 :parameters (?s1 ?s2 - side ?m - mis1 ?m2 - mis2 ?b - boat)
 :precondition(and(at-emb ?s1)(atM1 ?m ?s1)(atM2 ?m2 ?s1))
 :effect(and(at-emb ?s2)(not(at-emb ?s1))(atM1 ?m ?s2)(atM2 ?m2 ?s2)(empty ?b))
)


(:action GOM1C1 
 :parameters (?s1 ?s2 - side ?m - mis1 ?c - can1 ?b - boat)
 :precondition(and(at-emb ?s1)(atM1 ?m ?s1)(atC1 ?c ?s1))
 :effect(and(at-emb ?s2)(not(at-emb ?s1))(atM1 ?m ?s2)(atC1 ?c ?s2)(empty ?b))
)

(:action GOM2C2 
 :parameters (?s1 ?s2 - side ?m2 - mis2 ?c2 - can2 ?b - boat)
 :precondition(and(at-emb ?s1)(atM2 ?m2 ?s1)(atC2 ?c2 ?s1))
 :effect(and(at-emb ?s2)(not(at-emb ?s1))(atM2 ?m2 ?s2)(atC2 ?c2 ?s2)(empty ?b))
)


(:action BACK  
 :parameters (?s1 ?s2 - side)
 :precondition(at-emb ?s2)
 :effect(and(at-emb ?s1)(not(at-emb ?s2)))
)

)



 
 
 
 
 