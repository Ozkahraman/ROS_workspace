
(cl:in-package :asdf)

(defsystem "basit_uygulamalar-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "CemberHaraket" :depends-on ("_package_CemberHaraket"))
    (:file "_package_CemberHaraket" :depends-on ("_package"))
  ))