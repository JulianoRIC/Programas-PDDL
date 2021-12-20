(define (domain mec)
    (:requirements
    :typing
    :strips
    :fluents
    :equality
    :conditional-effects)
    
    (:types
    margem
    barco
    canibal
    missionario
    embarcacao
    )
    
    (:predicates 
    
    (at-boat ?m - margem)
    (atM ?mi - missionario ?m - margem)
    (atC ?c - canibal ?m - margem)
    (atMboat ?mi - missionario ?b - barco)
    (atCboat ?c - canibal ?b - barco)
    (free ?b - barco)
    (carryM ?mi - missionario ?b - barco)
    (carryC ?c - canibal ?b - barco) 
    
    )
    
    (:functions (numberM ?m - margem))
    (:functions (numberC ?m - margem))
    (:functions (numberCboat ?e - embarcacao))
    (:functions (numberMboat ?e - embarcacao))
    ;(:functions (number ?m - margem))
    
    
    (:action mudaMargem
    :parameters(?m1 ?m2 - margem ?b1 ?b2 - barco ?e - embarcacao)
    :precondition(and(at-boat ?m1)(or (not(free ?b1)) (not(free ?b2))) (>(numberM ?m1)(numberC ?m2)) (>= (+ (numberMboat ?e) (numberM ?m2)) (+ (numberCboat ?e) (numberC ?m2)))) 
    :effect(and (not(at-boat ?m1)) (at-boat ?m2))
    )

    
     (:action embarqueUmCanibal
    :parameters(?c - canibal ?b - barco ?m - margem ?m1 ?m2 - margem ?e - embarcacao)
    :precondition(and(free ?b) (at-boat ?m) (atC ?c ?m))
    :effect(and(not(free ?b)) (not(atC ?c ?m)) (increase (numberCboat ?e) 1) (decrease (numberC ?m) 1) (atCboat ?c ?b))  
    )
     (:action embarqueUmMissionario
    :parameters(?mi - missionario ?b - barco ?m - margem ?m1 ?m2 - margem ?e - embarcacao)
    :precondition(and(free ?b) (at-boat ?m) (atM ?mi ?m)(>(numberM ?m2)(numberC ?m2)))  ;condicao m > c
    :effect(and(not(free ?b))  (not(atM ?mi ?m)) (increase (numberMboat ?e) 1) (decrease (numberM ?m) 1) (atMboat ?mi ?b))
    )
    
    (:action desembarqueUmCanibal
    :parameters(?c - canibal ?b - barco ?m ?m2 - margem ?e - embarcacao)
    :precondition(and(not(free ?b)) (at-boat ?m) (atCboat ?c ?b) (>(numberM ?m2)(numberC ?m2)))
    :effect(and (free ?b) (atC ?c ?m)  (decrease (numberCboat ?e) 1) (increase (numberC ?m) 1) (not(atCboat ?c ?b))) 
    )
    
    (:action desembarqueUmMissionario
    :parameters(?mi - missionario ?b - barco ?m - margem ?e - embarcacao)
    :precondition(and(not(free ?b)) (at-boat ?m) (atMboat ?mi ?b) )
    :effect(and (free ?b)  (atM ?mi ?m)  (decrease (numberMboat ?e) 1) (increase (numberM ?m) 1) (not(atMboat ?mi ?b))) 
    )
   
    
    )