(load "C:\\euler\\78\\memoize.lisp")
(def-memoized-function pile (n)
           (cond 
             ((= n 1) 1)
             (T (+ (pile (- n 1)) (floor n 2)))))
             
(defun iterate (n)
    (cond 
        ((= 0 n) NIL)
        ( (not (null (floor (pile n) 1000000))) n)
        (T (iterate (- n 1)))
    )
)
(print (iterate 500))