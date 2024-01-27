; Auto-generated. Do not edit!


(cl:in-package basit_uygulamalar-srv)


;//! \htmlinclude CemberHaraket-request.msg.html

(cl:defclass <CemberHaraket-request> (roslisp-msg-protocol:ros-message)
  ((yaricap
    :reader yaricap
    :initarg :yaricap
    :type cl:float
    :initform 0.0))
)

(cl:defclass CemberHaraket-request (<CemberHaraket-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <CemberHaraket-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'CemberHaraket-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name basit_uygulamalar-srv:<CemberHaraket-request> is deprecated: use basit_uygulamalar-srv:CemberHaraket-request instead.")))

(cl:ensure-generic-function 'yaricap-val :lambda-list '(m))
(cl:defmethod yaricap-val ((m <CemberHaraket-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader basit_uygulamalar-srv:yaricap-val is deprecated.  Use basit_uygulamalar-srv:yaricap instead.")
  (yaricap m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <CemberHaraket-request>) ostream)
  "Serializes a message object of type '<CemberHaraket-request>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'yaricap))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <CemberHaraket-request>) istream)
  "Deserializes a message object of type '<CemberHaraket-request>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'yaricap) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<CemberHaraket-request>)))
  "Returns string type for a service object of type '<CemberHaraket-request>"
  "basit_uygulamalar/CemberHaraketRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CemberHaraket-request)))
  "Returns string type for a service object of type 'CemberHaraket-request"
  "basit_uygulamalar/CemberHaraketRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<CemberHaraket-request>)))
  "Returns md5sum for a message object of type '<CemberHaraket-request>"
  "534fdc954659adaf837ecd56d547676d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'CemberHaraket-request)))
  "Returns md5sum for a message object of type 'CemberHaraket-request"
  "534fdc954659adaf837ecd56d547676d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<CemberHaraket-request>)))
  "Returns full string definition for message of type '<CemberHaraket-request>"
  (cl:format cl:nil "float64 yaricap~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'CemberHaraket-request)))
  "Returns full string definition for message of type 'CemberHaraket-request"
  (cl:format cl:nil "float64 yaricap~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <CemberHaraket-request>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <CemberHaraket-request>))
  "Converts a ROS message object to a list"
  (cl:list 'CemberHaraket-request
    (cl:cons ':yaricap (yaricap msg))
))
;//! \htmlinclude CemberHaraket-response.msg.html

(cl:defclass <CemberHaraket-response> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass CemberHaraket-response (<CemberHaraket-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <CemberHaraket-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'CemberHaraket-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name basit_uygulamalar-srv:<CemberHaraket-response> is deprecated: use basit_uygulamalar-srv:CemberHaraket-response instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <CemberHaraket-response>) ostream)
  "Serializes a message object of type '<CemberHaraket-response>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <CemberHaraket-response>) istream)
  "Deserializes a message object of type '<CemberHaraket-response>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<CemberHaraket-response>)))
  "Returns string type for a service object of type '<CemberHaraket-response>"
  "basit_uygulamalar/CemberHaraketResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CemberHaraket-response)))
  "Returns string type for a service object of type 'CemberHaraket-response"
  "basit_uygulamalar/CemberHaraketResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<CemberHaraket-response>)))
  "Returns md5sum for a message object of type '<CemberHaraket-response>"
  "534fdc954659adaf837ecd56d547676d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'CemberHaraket-response)))
  "Returns md5sum for a message object of type 'CemberHaraket-response"
  "534fdc954659adaf837ecd56d547676d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<CemberHaraket-response>)))
  "Returns full string definition for message of type '<CemberHaraket-response>"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'CemberHaraket-response)))
  "Returns full string definition for message of type 'CemberHaraket-response"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <CemberHaraket-response>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <CemberHaraket-response>))
  "Converts a ROS message object to a list"
  (cl:list 'CemberHaraket-response
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'CemberHaraket)))
  'CemberHaraket-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'CemberHaraket)))
  'CemberHaraket-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CemberHaraket)))
  "Returns string type for a service object of type '<CemberHaraket>"
  "basit_uygulamalar/CemberHaraket")