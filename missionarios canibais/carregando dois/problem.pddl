(define (problem miss_han)

 (:domain pass_boat)
 
 (:objects left right - side miss han han2 miss2 - passenger  transport - boat)
 
 (:init (at-emb right)
        (at han  right)
        (at han2 right)
        (at miss2 right)
        (at miss right)
        (empty transport)
 )
 
 (:goal (and(at miss left)(at han left) (at han2 left) (at miss2 left)))

)