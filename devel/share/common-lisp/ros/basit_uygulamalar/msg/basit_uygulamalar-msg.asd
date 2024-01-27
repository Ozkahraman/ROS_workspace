
(cl:in-package :asdf)

(defsystem "basit_uygulamalar-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "mesafe" :depends-on ("_package_mesafe"))
    (:file "_package_mesafe" :depends-on ("_package"))
  ))