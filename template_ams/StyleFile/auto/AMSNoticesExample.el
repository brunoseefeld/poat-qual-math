(TeX-add-style-hook
 "AMSNoticesExample"
 (lambda ()
   (TeX-run-style-hooks
    "latex2e"
    "notices"
    "notices10"
    "amsfonts"
    "amssymb"
    "amsmath"
    "amscd")
   (LaTeX-add-bibliographies
    "ExampleRefs"))
 :latex)

