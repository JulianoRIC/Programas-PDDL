(define 
    
(domain mec)

   
(:requirements
 :typing
 :strips
 :fluents
 :equality
 :conditional-effects 
 :negative-preconditions 
 :disjunctive-preconditions)
    
    (:types
    margem
    barco
    canibal
    missionario
    
    )
    
    (:predicates 
    
    (at-boat ?m - margem)
    (atM ?mi - missionario ?m - margem)
    (atC ?c - canibal ?m - margem)
    (atMboat ?mi - missionario ?b - barco)
    (atCboat ?c - canibal ?b - barco)
    (free ?b - barco)
    ;(carryM ?mi - missionario ?b - barco)
    ;(carryC ?c - canibal ?b - barco) 
    
    )
    
    (:functions(numberM ?m - margem))
    (:functions(numberC ?m - margem))
    (:functions(numberCboat ?b - barco))
    (:functions(numberMboat ?b - barco))
    ;(number ?m - margem)
    
    (:action mudaMargem
    :parameters(?m1 ?m2 - margem ?b1 ?b2 - barco)
    :precondition (and(at-boat ?m1) (or (not(free ?b1)) (not(free ?b2))) (or (>= (numberM ?m1) (+ (numberM ?m2) (+ (numberMboat ?b1) (numberMboat ?b2))) )  (= (numberM ?m1) 0) (= (numberM ?m1) (numberC ?m1))  ) 
    (or (<= (+ (numberC ?m2) (+(numberCboat ?b1) (numberCboat ?b2))   ) (numberM ?m2) ) (= (numberM ?m2) 0 )) )
    :effect(and (not(at-boat ?m1)) (at-boat ?m2))
    )

    
     (:action embarqueUmCanibal
    :parameters(?c - canibal ?b - barco ?m - margem )
    :precondition(and(free ?b) (at-boat ?m) (atC ?c ?m) )
    :effect(and(not(free ?b))  (not(atC ?c ?m)) (decrease (numberC ?m) 1) (atCboat ?c ?b) (increase (numberCboat ?b) 1))  
    )
     (:action embarqueUmMissionario
    :parameters(?mi - missionario ?b - barco ?m - margem )
    :precondition(and(free ?b) (at-boat ?m) (atM ?mi ?m) )
    :effect(and(not(free ?b)) (not(atM ?mi ?m)) (decrease (numberM ?m) 1) (atMboat ?mi ?b) (increase (numberMboat ?b) 1))
    )
     (:action desembarqueUmCanibal
    :parameters(?c - canibal ?b - barco ?m - margem )
    :precondition(and(not(free ?b)) (at-boat ?m) (atCboat ?c ?b) )
    :effect(and (free ?b) (atC ?c ?m)  (increase (numberC ?m) 1) (not(atCboat ?c ?b)) (decrease (numberCboat ?b) 1)) 
    )
    
     (:action desembarqueUmMissionario
    :parameters(?mi - missionario ?b - barco ?m - margem )
    :precondition(and(not(free ?b)) (at-boat ?m) (atMboat ?mi ?b) )
    :effect(and (free ?b)  (atM ?mi ?m)  (increase (numberM ?m) 1) (not(atMboat ?mi ?b)) (decrease (numberMboat ?b) 1)) 
    )
   
)
    
    
  