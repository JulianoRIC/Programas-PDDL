(define (problem mec_problem)
	(:domain mec)
	
	(:objects
		 b - barco dir esq - lado
	)

	(:init	
		(barcoNo dir)
		(not(free b))
		(mL dir esq)
	    (mL esq dir)
		(busy b)
		(pA b)
		(= (can dir) 3)
		(= (can esq) 0)
		(= (mis dir) 3)
		(= (mis esq) 0)
		
	)

	(:goal (and
        (barcoNo esq)
		(= (mis esq) 3)
		(= (can esq) 3)
                (free b)
	    )
	)
)