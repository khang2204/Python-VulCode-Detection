def test_multiline_string(self):...
self.compilation_ok(
    """
require "reject";

if allof (false, address :is ["From", "Sender"] ["blka@bla.com"]) {
    reject text:
noreply
============================
Your email has been canceled
============================
.
;
    stop;
} else {
    reject text:
================================
Your email has been canceled too
================================
.
;
}
"""
    )
self.representation_is(
    """
require (type: control)
    "reject"
if (type: control)
    allof (type: test)
        false (type: test)
        address (type: test)
            :is
            ["From","Sender"]
            ["blka@bla.com"]
    reject (type: action)
        text:
noreply
============================
Your email has been canceled
============================
.
    stop (type: control)
else (type: control)
    reject (type: action)
        text:
================================
Your email has been canceled too
================================
.
"""
    )
