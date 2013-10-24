;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname portfolio-starter) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ())))
(require 2htdp/image)

;; portfolio-starter.rkt

;; An image organizer / portfolio program

;; ================= 
;; Constants:

(define SEPARTOR "  ")
(define BLANKIMG (rectangle 0 0 "solid" "white"))
(define FONTSIZE 12)
(define FONT "indigo")
(define ALIGN "left")

;; ================= 
;; Data Definitions:                                                            

(define-struct image-node (name size data))
;; image-node is (make-image-node String Nature Image)
;; interp. The current image node name(name) and it's size(size), and it's atually image(image)
(define BLANK (make-image-node "" 20 BLANKIMG))
(define SQUARE (make-image-node "Square" 21 (rectangle 20 20 "solid" "red")))
(define RECTANGLE (make-image-node "Rectangle" 22 (rectangle 10 20 "solid" "blue")))
(define TRIANGLE (make-image-node "Triangle" 23 (triangle 20 "solid" "green")))
(define CIRCLE (make-image-node "Circle" 24 (circle 20 "solid" "green")))
#;
(define (fn-for-img img)
  (...(image-node-name img) (image-node-size img) (image-node-data img) 
      ))

(define-struct folder-node (name sub-folders images))
;; folder-node is (make-folder-node String ListOfFolderNode ListOfImageNode)
;; interp. a list of node where each node is 
;;    - empty 
;;    - a list of folder node
;;    - a list of image node
(define EMPTYFN (make-folder-node "" empty (cons BLANK empty)))
(define FOLDER1 (make-folder-node "Folder1" empty (cons SQUARE empty)))
(define FOLDER2 (make-folder-node "Folder2" empty (cons SQUARE (cons RECTANGLE empty))))
(define FOLDER3 (make-folder-node "Folder3" empty TRIANGLE))
(define FOLDER4 (make-folder-node "Folder4" empty CIRCLE))

;; ListOfFolderNode is one of:
;;  - empty
;;  - (cons FolderNode ListOfFolderNode)
;; interp. An arbitrary number of folder nodes.
(define EMPTYFNS empty)
(define FN2 (cons FOLDER1 EMPTYFNS))
(define FN3 (cons FOLDER2 FN2))
(define FN4 (cons FOLDER3 FN3))
(define FN5 (cons FOLDER4 FN4))
#;
(define (fn-for-lof lof)
  (cond [(empty? lof) (...)]
        [else
         (... (first lof)
              (fn-for-lof (rest lof)))]))

;; ListOfImageNode is one of:
;;  - empty
;;  - (cons ImageNode ListOfImageNode)
;; interp. An arbitrary number of image nodes
(define LOI1 empty)
(define LOI2 (cons SQUARE (cons RECTANGLE empty)))
(define LOI3 (cons SQUARE (cons CIRCLE (cons RECTANGLE empty))))
#;
(define (fn-for-loi loi)
  (cond [(empty? loi) (...)]
        [else
         (fn-for-fn (first loi))                              ;ImageNode
         (fn-for-loi (rest loi))]))

#;
(define (fn-for-fn fn)  
  (... (folder-node-name  fn)                   ;String
       (fn-for-fn (folder-node-sub-folders fn)) ;ListOfFolderNode
       (fn-for-loi (folder-node-images fn))     ;ListOfImage
       ))

;; ================= 
;; Functions:

;; ImageNode -> Image
;; Render a image node to image
(check-expect (render-image BLANK) (beside (text (string-append (image-node-name BLANK) SEPARTOR) FONTSIZE FONT)                                        
                                           (image-node-data BLANK)))
(check-expect (render-image SQUARE) (beside (text (string-append (image-node-name SQUARE) SEPARTOR) FONTSIZE FONT)
                                            (image-node-data SQUARE)))

(define (render-image image)
  (beside (text (string-append (image-node-name image) SEPARTOR) FONTSIZE FONT)
          (image-node-data image)))

;; ListOfImageNode -> Image
;; Display a list of image nodes as a image
(check-expect (render-images empty) BLANKIMG)
(check-expect (render-images LOI2) (above/align ALIGN
                                                (render-image SQUARE)
                                                (render-image RECTANGLE)
                                                BLANKIMG))
(define (render-images images)
  (cond [(empty? images) BLANKIMG]
        [else
         (above/align ALIGN
                      (render-image (first images))                           
                      (render-images (rest images)))]))

;; ListOfImageNode -> ListOfImageNode
;; Sort the image list by the size attribute
(check-expect (sort-images-by-size (cons (make-image-node "Square" 21 (rectangle 20 20 "solid" "red")) empty))
              (cons (make-image-node "Square" 21 (rectangle 20 20 "solid" "red")) empty))
(check-expect (sort-images-by-size LOI2)  (cons (make-image-node "Rectangle" 22 (rectangle 10 20 "solid" "blue")) 
                                                (cons (make-image-node "Square" 21 (rectangle 20 20 "solid" "red")) empty)))

(check-expect (sort-images-by-size empty) empty)
(define (sort-images-by-size images)
  (cond [(empty? images) empty]
        [else 
         (insert-image (first images)
                 (sort-images-by-size (rest images)))]))

(define (insert-image img loi)
  (cond [(empty? loi) (cons img empty)]
        [else 
         (if (smaller-image? img (first loi))
             (cons (first loi)
                   (insert-image img 
                           (rest loi)))
             (cons img loi))]))

(define (smaller-image? img1 img2) 
  (< (image-node-size img1) (image-node-size img2)))


;; ListOfFolderNode -> ListOfFolderNode
;; Sort the folder node by the size of images in it's sub folder recurrensively 
(check-expect (sort-folder-by-size empty) empty)
(define (sort-folder-by-size fns) 
  (cond [(empty? fns) empty]
        [else 
         (insert-fn (first fns)
                 (sort-folder-by-size (rest fns)))]))

(define (insert-fn fn fns)
  (cond [(empty? fns) (cons fn empty)]
        [else 
         (if (smaller-folder? fn (first fns))
             (cons (first fns)
                   (insert-fn fn 
                           (rest fns)))
             (cons fn fns))]))

;; FolderNode FolderNode -> Boolean
;; Whether the folder is a smaller folder?
;; !!!
(define (smaller-folder? f1 f2) 
  true)

;; FolderNode -> Image
;; Display a folder node as a image
(check-expect (render-folder-node EMPTYFN) BLANKIMG)
(check-expect (render-folder-node (make-folder-node "Folder1" 
                                                    (cons (make-folder-node "Folder2" empty (cons CIRCLE empty)) empty) (cons TRIANGLE (cons SQUARE empty))))
              (above/align ALIGN
                           (text "Folder1" FONTSIZE FONT)
                           (beside (text SEPARTOR FONTSIZE FONT)
                                   (above/align ALIGN
                                                (render-images (cons TRIANGLE (cons SQUARE empty)))
                                                (text "Folder2" FONTSIZE FONT)
                                                (beside   (text SEPARTOR FONTSIZE FONT)
                                                          (above/align ALIGN                                      
                                                                       (render-images (cons CIRCLE empty))
                                                                       BLANKIMG))
                                                BLANKIMG))))                              

(define (render-folder-node fn)
  (cond [(equal? EMPTYFN fn) BLANKIMG]
        [else (above/align ALIGN
                           (text (folder-node-name fn) FONTSIZE FONT)
                           (beside   (text SEPARTOR FONTSIZE FONT)
                                     (above/align ALIGN                                      
                                                  (render-images (sort-images-by-size (folder-node-images fn)))
                                                  (render-folder-nodes (sort-folder-by-size (folder-node-sub-folders fn))))
                                     ))]))

;; ListOfFolderNode -> Image
;; Display list of folder node as a image
(define (render-folder-nodes loi)
  (cond [(empty? loi) BLANKIMG]
        [else (above/align ALIGN
                           (render-folder-node (first loi))
                           (render-folder-nodes (rest loi)))]))
