;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname Assignment1) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ())))
(require 2htdp/image)

(beside (above (triangle 30 "solid" "blue")
               (ellipse 30 50 "solid" "green")
               (square 30 "solid" "red"))
        (text "Frosty" 24 "black"))

(define (foo s)
  (if (string=? (substring s 0 1) "a")
      (string-append s "a")
      s))

(foo "cat")

(define (bar s)
  (if (>= (string-length s) 5)
      (substring s 3)
      (string-append s s)))

(bar "hello")

(define (greet x)
  (string-append "hello x"))

(greet "Stephen")