;; Auto-generated. Do not edit!


(when (boundp 'basit_uygulamalar::CemberHaraket)
  (if (not (find-package "BASIT_UYGULAMALAR"))
    (make-package "BASIT_UYGULAMALAR"))
  (shadow 'CemberHaraket (find-package "BASIT_UYGULAMALAR")))
(unless (find-package "BASIT_UYGULAMALAR::CEMBERHARAKET")
  (make-package "BASIT_UYGULAMALAR::CEMBERHARAKET"))
(unless (find-package "BASIT_UYGULAMALAR::CEMBERHARAKETREQUEST")
  (make-package "BASIT_UYGULAMALAR::CEMBERHARAKETREQUEST"))
(unless (find-package "BASIT_UYGULAMALAR::CEMBERHARAKETRESPONSE")
  (make-package "BASIT_UYGULAMALAR::CEMBERHARAKETRESPONSE"))

(in-package "ROS")





(defclass basit_uygulamalar::CemberHaraketRequest
  :super ros::object
  :slots (_yaricap ))

(defmethod basit_uygulamalar::CemberHaraketRequest
  (:init
   (&key
    ((:yaricap __yaricap) 0.0)
    )
   (send-super :init)
   (setq _yaricap (float __yaricap))
   self)
  (:yaricap
   (&optional __yaricap)
   (if __yaricap (setq _yaricap __yaricap)) _yaricap)
  (:serialization-length
   ()
   (+
    ;; float64 _yaricap
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _yaricap
       (sys::poke _yaricap (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _yaricap
     (setq _yaricap (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass basit_uygulamalar::CemberHaraketResponse
  :super ros::object
  :slots ())

(defmethod basit_uygulamalar::CemberHaraketResponse
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass basit_uygulamalar::CemberHaraket
  :super ros::object
  :slots ())

(setf (get basit_uygulamalar::CemberHaraket :md5sum-) "534fdc954659adaf837ecd56d547676d")
(setf (get basit_uygulamalar::CemberHaraket :datatype-) "basit_uygulamalar/CemberHaraket")
(setf (get basit_uygulamalar::CemberHaraket :request) basit_uygulamalar::CemberHaraketRequest)
(setf (get basit_uygulamalar::CemberHaraket :response) basit_uygulamalar::CemberHaraketResponse)

(defmethod basit_uygulamalar::CemberHaraketRequest
  (:response () (instance basit_uygulamalar::CemberHaraketResponse :init)))

(setf (get basit_uygulamalar::CemberHaraketRequest :md5sum-) "534fdc954659adaf837ecd56d547676d")
(setf (get basit_uygulamalar::CemberHaraketRequest :datatype-) "basit_uygulamalar/CemberHaraketRequest")
(setf (get basit_uygulamalar::CemberHaraketRequest :definition-)
      "float64 yaricap
---

")

(setf (get basit_uygulamalar::CemberHaraketResponse :md5sum-) "534fdc954659adaf837ecd56d547676d")
(setf (get basit_uygulamalar::CemberHaraketResponse :datatype-) "basit_uygulamalar/CemberHaraketResponse")
(setf (get basit_uygulamalar::CemberHaraketResponse :definition-)
      "float64 yaricap
---

")



(provide :basit_uygulamalar/CemberHaraket "534fdc954659adaf837ecd56d547676d")


