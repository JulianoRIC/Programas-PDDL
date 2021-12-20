(define (problem miss_han)

 (:domain pass_boat)
 
 (:objects left right - side  can can2 can3 - cannibal mis mis2 mis3 - missionary  b1 b2 - boat)
 
 (:init (at-emb right)
        (atC can   right)
        (atC can2  right)
        (atC can3  right)
        (atM mis   right)
        (atM mis2   right)
        (atM mis3   right)
        ;(at miss right)
        (empty b1)
        (empty b2)
 )
 
 (:goal (and(atC can left)(atC can2 left)(atC can3 left)(atM mis left)(atM mis2 left)(atM mis3 left)))

)