(define (problem miss_han)

 (:domain pass_boat)
 
 (:objects left right - side  CAN1 - can1 CAN2 - can2 CAN3 - can3 MIS1 - mis1 MIS2 - mis2 MIS3 - mis3   b1 b2 - boat)
 
 (:init (at-emb right)
        (atC1 CAN1   right)
        (atC2 CAN2   right)
        (atC3 CAN3   right)
        (atM1 MIS1   right)
        (atM2 MIS2   right)
        (atM3 MIS3   right)
        (empty b1)
        (empty b2)
 )
 
 (:goal (and(atC1 CAN1 left)(atC2 CAN2 left)(atC3 CAN3 left)(atM1 MIS1 left)(atM2 MIS2 left)(atM3 MIS3 left)))

)