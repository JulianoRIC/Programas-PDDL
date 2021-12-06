(define (problem miss_han)

 (:domain pass_boat)
 
 (:objects left right - side miss han - passenger  ba be - boat)
 
 (:init (at-emb right)
        (at han  right)
        (at miss right)
        (empty ba)
        (empty be)
 )
 
 (:goal (and(at miss left)(at han left)))

)