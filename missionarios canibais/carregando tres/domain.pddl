(define (domain pass_boat)
 
 (:requirements
  :strips
  :typing 
 )
 
(:types missionaire hannibal boat river)

(:predicates 
 (at-r ?r - river)
 (at-h ?r - river)
 (at   ?h - hannibal    ?r - river)
 (at-m ?m - missionaire ?r - river)
 (empty ?b - boat)
 ;(full  ?b - boat)
 (carryM ?m - missionaire ?b - boat)
 (carryH ?h - hannibal ?b - boat)
)

(:action move
 :parameters(?r1 ?r2 - river)
 :precondition(at-r ?r1)
 :effect(and(at-r ?r2)(not(at-r ?r1)))
)

(:action embarkM
 :parameters(?m ?m2 - missionaire ?r - river ?b - boat)
 :precondition(and(at-m ?m ?r)(at-r ?r)(empty ?b))
 :effect(and(carryM ?m ?b)(not(at-m ?m ?r))(not(empty ?b)))
)

(:action disembarkM
 :parameters(?m - missionaire  ?r - river ?b - boat)
 :precondition(and(carryM ?m ?b)(at-r ?r))
 :effect(and(at-m ?m ?r)(empty ?b)(not(carryM ?m ?b)))
)

(:action embarkH
 :parameters(?h - hannibal ?m - missionaire ?r - river ?b - boat)
 :precondition(and(at ?h ?r)(at-r ?r)(empty ?b))
 :effect(and(carryH ?h ?b)(not(at ?h ?r))(not(empty ?b)))
)

(:action disembarkH
 :parameters(?h - hannibal ?r - river ?b - boat)
 :precondition(and(carryH ?h ?b)(at-r ?r))
 :effect(and(at ?h ?r)(empty ?b)(not(carryH ?h ?b)))
)

)