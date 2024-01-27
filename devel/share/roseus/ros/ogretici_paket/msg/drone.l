;; Auto-generated. Do not edit!


(when (boundp 'ogretici_paket::drone)
  (if (not (find-package "OGRETICI_PAKET"))
    (make-package "OGRETICI_PAKET"))
  (shadow 'drone (find-package "OGRETICI_PAKET")))
(unless (find-package "OGRETICI_PAKET::DRONE")
  (make-package "OGRETICI_PAKET::DRONE"))

(in-package "ROS")
;;//! \htmlinclude drone.msg.html


(defclass ogretici_paket::drone
  :super ros::object
  :slots (_hiz _isim _batarya ))

(defmethod ogretici_paket::drone
  (:init
   (&key
    ((:hiz __hiz) 0)
    ((:isim __isim) "")
    ((:batarya __batarya) 0)
    )
   (send-super :init)
   (setq _hiz (round __hiz))
   (setq _isim (string __isim))
   (setq _batarya (round __batarya))
   self)
  (:hiz
   (&optional __hiz)
   (if __hiz (setq _hiz __hiz)) _hiz)
  (:isim
   (&optional __isim)
   (if __isim (setq _isim __isim)) _isim)
  (:batarya
   (&optional __batarya)
   (if __batarya (setq _batarya __batarya)) _batarya)
  (:serialization-length
   ()
   (+
    ;; int32 _hiz
    4
    ;; string _isim
    4 (length _isim)
    ;; int32 _batarya
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _hiz
       (write-long _hiz s)
     ;; string _isim
       (write-long (length _isim) s) (princ _isim s)
     ;; int32 _batarya
       (write-long _batarya s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _hiz
     (setq _hiz (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; string _isim
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _isim (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; int32 _batarya
     (setq _batarya (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get ogretici_paket::drone :md5sum-) "ab3da279a675c6dfa18bb8afc332a0ab")
(setf (get ogretici_paket::drone :datatype-) "ogretici_paket/drone")
(setf (get ogretici_paket::drone :definition-)
      "int32 hiz
string isim
int32 batarya
")



(provide :ogretici_paket/drone "ab3da279a675c6dfa18bb8afc332a0ab")


