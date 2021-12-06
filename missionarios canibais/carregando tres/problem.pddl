(define (problem miss_han)

 (:domain pass_boat)
 
 (:objects left right - river miss1 miss2 miss3 - missionaire han1 han2 han3 - hannibal  stopped - boat)
 
 (:init (at-r  right)
        (at han1  right)
        (at-m miss1 right)
        (at-m miss2 right)
        (at han2  right)
        (at-m miss3 right)
        (at han3  right)
        (empty stopped)
        ;(full moving)
)
 
 ; (:goal (and(at-m miss1 left) (at-m miss2 left) (at-m miss3 left))) 
 (:goal (and(at han2 left)(at-m miss2 left)(at-m miss3 left)(at han3 left)(at-m miss1 left)(at han1 left)))

)