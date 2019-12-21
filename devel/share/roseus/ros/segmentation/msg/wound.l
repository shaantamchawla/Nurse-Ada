;; Auto-generated. Do not edit!


(when (boundp 'segmentation::wound)
  (if (not (find-package "SEGMENTATION"))
    (make-package "SEGMENTATION"))
  (shadow 'wound (find-package "SEGMENTATION")))
(unless (find-package "SEGMENTATION::WOUND")
  (make-package "SEGMENTATION::WOUND"))

(in-package "ROS")
;;//! \htmlinclude wound.msg.html


(defclass segmentation::wound
  :super ros::object
  :slots (_x _y _length _width ))

(defmethod segmentation::wound
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:length __length) 0.0)
    ((:width __width) 0.0)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _length (float __length))
   (setq _width (float __width))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:length
   (&optional __length)
   (if __length (setq _length __length)) _length)
  (:width
   (&optional __width)
   (if __width (setq _width __width)) _width)
  (:serialization-length
   ()
   (+
    ;; float64 _x
    8
    ;; float64 _y
    8
    ;; float64 _length
    8
    ;; float64 _width
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _x
       (sys::poke _x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _length
       (sys::poke _length (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _width
       (sys::poke _width (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _x
     (setq _x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _length
     (setq _length (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _width
     (setq _width (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get segmentation::wound :md5sum-) "e1d56a1459316f615661d9730e39e6a7")
(setf (get segmentation::wound :datatype-) "segmentation/wound")
(setf (get segmentation::wound :definition-)
      "float64 x
float64 y
float64 length
float64 width
")



(provide :segmentation/wound "e1d56a1459316f615661d9730e39e6a7")


