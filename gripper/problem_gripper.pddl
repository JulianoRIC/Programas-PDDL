(define (problem gripper_problem)

 (:domain gripper)
 
 (:objects rooma roomb - room ball1 ball2 - ball left right - gripper)
 
 (:init (at-robby rooma)
        (at ball1 rooma)
        (at ball2 rooma)
        (free left)
        (free right)
 )
 
 (:goal (and(at ball1 roomb)(at ball2 roomb)))

)