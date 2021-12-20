(define (domain mec)
    
(:requirements
 :typing
 :fluents
)    
(:types
 lado
 barco     
)

(:predicates
 (mL ?dir ?esq - lado)          ;mL = muda lado  
 (free ?b      - barco)   ;lugar no barco vazio
 (busy ?b      - barco)   ;lugar no barco ocupado
 (PA ?b        - barco)  ;pode atravessar
 (NPA ?b       - barco)   ;nao pode atravessar
 (barcoNo ?m   - lado)    ;barco na margem
)

(:functions
 (mis ?m - lado) ;conta missionarios de um lado do rio
 (can ?m - lado) ;conta canibais de um lado do rio	
)
	
(:action permiteEmbarque
 :parameters (?b - barco)
 :precondition (and(busy ?b)(pA ?b)) 
 :effect (and(free ?b)(not(busy ?b)))
)
    
(:action atravessaRio_E_Desembarca
 :parameters(?b - barco)
 :precondition(NPA ?b)
 :effect (and (not(NPA ?b))(PA ?b))
)
    
    ;ol --> outro lado do rio
    ;la  --> lado atual do rio
    
(:action EmbarcaUmMissionarioUmCanibal
:parameters(?b - barco ?lA ?oL - lado)
:precondition(and(mL ?lA ?oL)(PA ?b)(barcoNo ?lA)(free ?b)(>=(mis ?lA)1)(>=(can ?lA)1)(>=(-(mis ?la)1)(-(can ?la)1)) (>=(+(mis ?ol)1)(+(can ?ol)1)))
:effect(and(not(barcoNo ?lA))(barcoNo ?oL)(not(PA ?b))(NPA ?b)(not(free ?b))(busy ?b)(increase(can ?oL)1)(increase (mis ?oL)1)(decrease(can ?lA) 1)(decrease (mis ?lA)1))
)

(:action EmbarcaUmMissionario
:parameters (?b - barco ?lA ?oL - lado)
:precondition (and(mL ?lA ?oL)(PA ?b)(barcoNo ?lA)(free ?b)(>=(mis ?la)1)(>= (-(mis ?lA) 1)(can ?lA))(>= (+ (mis ?oL) 1)(can ?oL)))
:effect (and(not(barcoNo ?lA))(barcoNo  ?oL)(not(PA ?b))(NPA ?b)(not(free ?b))(busy ?b) (increase (mis ?oL) 1)(decrease (mis ?lA)1))
)

(:action EmbarcaUmMissionarioSozinho
:parameters (?b - barco ?lA ?oL - lado )
:precondition (and(mL ?lA ?oL)(pA ?b)(barcoNo ?lA)(free ?b) (= (mis ?lA) 1) (= (- (mis ?lA) 1) 0) (>= (+ (mis ?oL) 1) (can ?oL)) )
:effect (and (not (barcoNo ?lA)) (barcoNo ?oL)  (not(PA ?b))  (NPA ?b) (not(free ?b)) (busy ?b)(increase (mis ?oL) 1) (decrease (mis ?lA) 1) )
)
	

(:action EmbarcamDoisMissionarios
:parameters (?b - barco ?lA ?oL - lado )
:precondition (and(mL ?lA ?oL)(pA ?b)(barcoNo ?lA) (free ?b) (>= (mis ?lA) 2)(>=(+(mis ?ol)2)(can ?ol))(>=(-(mis ?la)2)(can ?la)))
:effect (and(not (barcoNo  ?lA)) (barcoNo  ?oL)  (not(PA ?b))  (NPA ?b) (not(free ?b)) (busy ?b)(increase (mis ?oL) 2)(decrease (mis ?lA) 2))
)

(:action EmbarcamDoisMissionariosSozinhos
:parameters (?b - barco ?lA ?oL - lado)
:precondition (and(mL ?lA ?oL)(pA ?b) (barcoNo  ?lA) (free ?b)(=(mis ?lA) 2)(=(- (mis ?lA) 2) 0)(>= (+(mis ?oL) 2) (can ?oL)))
:effect (and (not(barcoNo ?lA))(barcoNo ?oL) (not(PA ?b))(NPA ?b)(not(free ?b))(busy ?b)(increase (mis ?oL) 2)(decrease (mis ?lA)2))
)

(:action EmbarcaUmCanibal
:parameters (?b - barco ?lA ?oL - lado)
:precondition (and(mL ?lA ?oL)(pA ?b)(barcoNo ?lA)(free ?b)(>=(can ?la)1)(>= (mis ?oL) (+ (can ?oL) 1)) )
:effect (and(not(barcoNo ?lA))(barcoNo  ?oL)(not(PA ?b))(NPA ?b)(not(free ?b))(busy ?b) (increase (can ?oL) 1)(decrease (can ?lA)1))
)

(:action EmbarcaUmCanibalSozinho
:parameters (?b - barco ?lA ?oL - lado)
:precondition (and(mL ?lA ?oL)(pA ?b)(barcoNo ?lA)(free ?b)(>= (can ?lA) 1)(= (mis ?oL) 0))
:effect (and (not (barcoNo  ?lA))(barcoNo ?oL)(not(PA ?b))(NPA ?b)(not(free ?b))(busy ?b)(increase (can ?oL) 1)(decrease (can ?lA) 1) )
)

(:action EmbarcamDoisCanibais
:parameters (?b - barco ?lA ?oL - lado)
:precondition (and (mL ?lA ?oL) (pA ?b)(barcoNo ?lA) (free ?b)(>= (can ?lA) 2)(<=(+(can ?ol)2)(mis ?ol)))
:effect (and (not (barcoNo ?lA))(barcoNo ?oL)(not(PA ?b))(NPA ?b) (not(free ?b)) (busy ?b) (increase (can ?oL) 2) (decrease (can ?lA) 2) )
)

(:action EmbarcamDoisCanibaisSozinhos
:parameters (?b - barco ?lA ?oL - lado)
:precondition (and (mL ?lA ?oL) (pA ?b)(barcoNo ?lA) (free ?b) (>= (can ?lA) 2) (= (mis ?oL) 0) )
:effect (and (not (barcoNo  ?lA)) (barcoNo  ?oL)  (not(PA ?b))  (NPA ?b) (not(free ?b)) (busy ?b) (increase (can ?oL) 2) (decrease (can ?lA) 2) )
)
	
)