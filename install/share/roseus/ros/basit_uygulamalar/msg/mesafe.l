;; Auto-generated. Do not edit!


(when (boundp 'basit_uygulamalar::mesafe)
  (if (not (find-package "BASIT_UYGULAMALAR"))
    (make-package "BASIT_UYGULAMALAR"))
  (shadow 'mesafe (find-package "BASIT_UYGULAMALAR")))
(unless (find-package "BASIT_UYGULAMALAR::MESAFE")
  (make-package "BASIT_UYGULAMALAR::MESAFE"))

(in-package "ROS")
;;//! \htmlinclude mesafe.msg.html


(defclass basit_uygulamalar::mesafe
  :super ros::object
  :slots (_mesafe ))

(defmethod basit_uygulamalar::mesafe
  (:init
   (&key
    ((:mesafe __mesafe) 0.0)
    )
   (send-super :init)
   (setq _mesafe (float __mesafe))
   self)
  (:mesafe
   (&optional __mesafe)
   (if __mesafe (setq _mesafe __mesafe)) _mesafe)
  (:serialization-length
   ()
   (+
    ;; float64 _mesafe
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _mesafe
       (sys::poke _mesafe (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _mesafe
     (setq _mesafe (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get basit_uygulamalar::mesafe :md5sum-) "67ce55637aff33e83a28f98ea42e7243")
(setf (get basit_uygulamalar::mesafe :datatype-) "basit_uygulamalar/mesafe")
(setf (get basit_uygulamalar::mesafe :definition-)
      "float64 mesafe

")



(provide :basit_uygulamalar/mesafe "67ce55637aff33e83a28f98ea42e7243")


