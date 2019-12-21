
(cl:in-package :asdf)

(defsystem "segmentation-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "wound" :depends-on ("_package_wound"))
    (:file "_package_wound" :depends-on ("_package"))
  ))