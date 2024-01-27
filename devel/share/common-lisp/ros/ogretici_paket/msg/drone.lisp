; Auto-generated. Do not edit!


(cl:in-package ogretici_paket-msg)


;//! \htmlinclude drone.msg.html

(cl:defclass <drone> (roslisp-msg-protocol:ros-message)
  ((hiz
    :reader hiz
    :initarg :hiz
    :type cl:integer
    :initform 0)
   (isim
    :reader isim
    :initarg :isim
    :type cl:string
    :initform "")
   (batarya
    :reader batarya
    :initarg :batarya
    :type cl:integer
    :initform 0))
)

(cl:defclass drone (<drone>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <drone>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'drone)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ogretici_paket-msg:<drone> is deprecated: use ogretici_paket-msg:drone instead.")))

(cl:ensure-generic-function 'hiz-val :lambda-list '(m))
(cl:defmethod hiz-val ((m <drone>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ogretici_paket-msg:hiz-val is deprecated.  Use ogretici_paket-msg:hiz instead.")
  (hiz m))

(cl:ensure-generic-function 'isim-val :lambda-list '(m))
(cl:defmethod isim-val ((m <drone>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ogretici_paket-msg:isim-val is deprecated.  Use ogretici_paket-msg:isim instead.")
  (isim m))

(cl:ensure-generic-function 'batarya-val :lambda-list '(m))
(cl:defmethod batarya-val ((m <drone>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ogretici_paket-msg:batarya-val is deprecated.  Use ogretici_paket-msg:batarya instead.")
  (batarya m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <drone>) ostream)
  "Serializes a message object of type '<drone>"
  (cl:let* ((signed (cl:slot-value msg 'hiz)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'isim))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'isim))
  (cl:let* ((signed (cl:slot-value msg 'batarya)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <drone>) istream)
  "Deserializes a message object of type '<drone>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'hiz) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'isim) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'isim) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'batarya) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<drone>)))
  "Returns string type for a message object of type '<drone>"
  "ogretici_paket/drone")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'drone)))
  "Returns string type for a message object of type 'drone"
  "ogretici_paket/drone")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<drone>)))
  "Returns md5sum for a message object of type '<drone>"
  "ab3da279a675c6dfa18bb8afc332a0ab")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'drone)))
  "Returns md5sum for a message object of type 'drone"
  "ab3da279a675c6dfa18bb8afc332a0ab")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<drone>)))
  "Returns full string definition for message of type '<drone>"
  (cl:format cl:nil "int32 hiz~%string isim~%int32 batarya~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'drone)))
  "Returns full string definition for message of type 'drone"
  (cl:format cl:nil "int32 hiz~%string isim~%int32 batarya~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <drone>))
  (cl:+ 0
     4
     4 (cl:length (cl:slot-value msg 'isim))
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <drone>))
  "Converts a ROS message object to a list"
  (cl:list 'drone
    (cl:cons ':hiz (hiz msg))
    (cl:cons ':isim (isim msg))
    (cl:cons ':batarya (batarya msg))
))
