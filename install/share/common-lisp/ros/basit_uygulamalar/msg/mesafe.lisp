; Auto-generated. Do not edit!


(cl:in-package basit_uygulamalar-msg)


;//! \htmlinclude mesafe.msg.html

(cl:defclass <mesafe> (roslisp-msg-protocol:ros-message)
  ((mesafe
    :reader mesafe
    :initarg :mesafe
    :type cl:float
    :initform 0.0))
)

(cl:defclass mesafe (<mesafe>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <mesafe>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'mesafe)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name basit_uygulamalar-msg:<mesafe> is deprecated: use basit_uygulamalar-msg:mesafe instead.")))

(cl:ensure-generic-function 'mesafe-val :lambda-list '(m))
(cl:defmethod mesafe-val ((m <mesafe>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader basit_uygulamalar-msg:mesafe-val is deprecated.  Use basit_uygulamalar-msg:mesafe instead.")
  (mesafe m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <mesafe>) ostream)
  "Serializes a message object of type '<mesafe>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'mesafe))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <mesafe>) istream)
  "Deserializes a message object of type '<mesafe>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'mesafe) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<mesafe>)))
  "Returns string type for a message object of type '<mesafe>"
  "basit_uygulamalar/mesafe")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'mesafe)))
  "Returns string type for a message object of type 'mesafe"
  "basit_uygulamalar/mesafe")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<mesafe>)))
  "Returns md5sum for a message object of type '<mesafe>"
  "67ce55637aff33e83a28f98ea42e7243")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'mesafe)))
  "Returns md5sum for a message object of type 'mesafe"
  "67ce55637aff33e83a28f98ea42e7243")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<mesafe>)))
  "Returns full string definition for message of type '<mesafe>"
  (cl:format cl:nil "float64 mesafe~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'mesafe)))
  "Returns full string definition for message of type 'mesafe"
  (cl:format cl:nil "float64 mesafe~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <mesafe>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <mesafe>))
  "Converts a ROS message object to a list"
  (cl:list 'mesafe
    (cl:cons ':mesafe (mesafe msg))
))
