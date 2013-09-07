;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname |Lecture 1|) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ())))
;(+ 3 4)

;(+ 3 (* 2 3))

(round (/ 12 (* 2 3)))

;(sqr 3)

;(sqrt 16)

;(sqrt (+ (sqr 3) (sqr 4)))

;(+ 2 (* 3 4) (- (+ 1 2)))

"apple"

"Ada"

;;; String primitives.
(string-append "Ada" " " "Lovelace")
(string-length "apple")
(substring "Caribou" 2 4)
(substring "0123456789" 2 4)
(substring "Caribou" 0 3)