(define (problem threecells)
  (:domain cells)

  ; Objects are candidates to replace free variables
  (:objects A B C - cell)

  ; The initial state describe what is currently true
  ; Everything else is considered false
  (:init (at A) (next A B) (next B C)
  )

  ; The goal state describe what we desire to achieve
  (:goal (at C))
)