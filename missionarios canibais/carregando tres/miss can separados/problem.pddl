(define (problem miss_han)

 (:domain pass_boat)
 
 (:objects left right - side miss1 miss2 miss3 - missionary can1 can2 can3 - cannibal  b1 b2 - boat)
 
 (:init (at-emb right)
        (atC  can1  right)
        (atM  miss1 right)
        (atM  miss2 right)
        (atC  can2  right)
        (atM  miss3 right)
        (atC  can3  right)
        (empty b1)
        (empty b2)
 )
 
 (:goal (and(atC can2 left)(atM miss2 left)(atM miss3 left)(atC can3 left)(atM miss1 left)(atC can1 left)))

)