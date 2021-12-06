(define (problem miss_han)

 (:domain pass_boat)
 
 (:objects left right - side miss1 miss2 miss3 han1 han2 han3 - passenger  stopped - boat)
 
 (:init (at-emb right)
        (at han1  right)
        (at miss1 right)
        (at miss2 right)
        (at han2  right)
        (at miss3 right)
        (at han3  right)
        (empty stopped)
 )
 
 (:goal (and(at han2 left)(at miss2 left)(at miss3 left)(at han3 left)(at miss1 left)(at han1 left)))

)