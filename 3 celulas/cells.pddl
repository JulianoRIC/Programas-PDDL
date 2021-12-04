(define (domain cells) ; Domain name must match problem's

  ; Define what the planner must support to execute this domain
  ; Only domain requirements are currently supported
  (:requirements
    :strips                 ; basic preconditions and effects
    :typing                 
  )

  (:types cell)
  
  ; Define the relations
  ; Question mark prefix denotes free variables
  (:predicates
    (at ?x - cell)
    (next ?x ?y - cell)
  )

  ; Define a transition to move from one cell to another
  (:action move
   :parameters(?x ?y - cell)
   :precondition (and(at ?x) (next ?X ?y))
   :effect(and (at ?y)(not(at ?x)))
  )

)

