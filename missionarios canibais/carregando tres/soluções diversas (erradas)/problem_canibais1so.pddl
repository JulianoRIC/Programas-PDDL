(define (problem miss_han)

 (:domain pass_boat)
 
 (:objects left right - side  can can2 can3 - cannibal  b1 b2 - boat)
 
 (:init (at-emb right)
        (atC can   right)
        (atC can2  right)
        (atC can3  right)
        ;(at miss right)
        (empty b1)
        (empty b2)
 )
 
 (:goal (and(atC can left)(atC can2 left)(atC can3 left)))

)