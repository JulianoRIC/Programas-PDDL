( define (problem mec_problem)


(:domain mec)
(:objects m1 m2 - margem mi1 mi2 mi3 - missionario c1 c2 c3 - canibal b1 b2 - barco e - embarcacao)
(:init  (at-boat m1)
        (atM mi1 m1)
        (atM mi2 m1)
        (atM mi3 m1)
        (atC c1 m1)
        (atC c2 m1)
        (atC c3 m1)
        (free b1)
        (free b2)
        (= (numberM m1) 3)
        (= (numberC m1) 3)
        (= (numberM m2 ) 0)
        (= (numberC m2 ) 0)
        (= (numberMboat e ) 0)
        (= (numberCboat e ) 0)
        
)

(:goal (and (at-boat m2) (atM mi1 m2) (atM mi2 m2) (atM mi3 m2)
        (atC c1 m2) (atC c2 m2) (atC c3 m2) (free b1) (free b2)
        (= (numberM m1 ) 0)
        (= (numberC m1 ) 0)
        (= (numberM m2 ) 3)
        (= (numberC m2 ) 3)
        )
) 


)