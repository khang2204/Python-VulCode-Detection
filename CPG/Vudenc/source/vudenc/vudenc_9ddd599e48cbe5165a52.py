def test_rfc5228_extended(self):...
self.compilation_ok(
    """
#
# Example Sieve Filter
# Declare any optional features or extension used by the script
#
require ["fileinto"];

#
# Handle messages from known mailing lists
# Move messages from IETF filter discussion list to filter mailbox
#
if header :is "Sender" "owner-ietf-mta-filters@imc.org"
        {
        fileinto "filter";  # move to "filter" mailbox
        }
#
# Keep all messages to or from people in my company
#
elsif address :DOMAIN :is ["From", "To"] "example.com"
        {
        keep;               # keep in "In" mailbox
        }

#
# Try and catch unsolicited email.  If a message is not to me,
# or it contains a subject known to be spam, file it away.
#
elsif anyof (NOT address :all :contains
               ["To", "Cc", "Bcc"] "me@example.com",
             header :matches "subject"
               ["*make*money*fast*", "*university*dipl*mas*"])
        {
        fileinto "spam";   # move to "spam" mailbox
        }
else
        {
        # Move all other (non-company) mail to "personal"
        # mailbox.
        fileinto "personal";
        }
"""
    )
self.representation_is(
    """
require (type: control)
    ["fileinto"]
if (type: control)
    header (type: test)
        :is
        "Sender"
        "owner-ietf-mta-filters@imc.org"
    fileinto (type: action)
        "filter"
elsif (type: control)
    address (type: test)
        :DOMAIN
        :is
        ["From","To"]
        "example.com"
    keep (type: action)
elsif (type: control)
    anyof (type: test)
        not (type: test)
            address (type: test)
                :all
                :contains
                ["To","Cc","Bcc"]
                "me@example.com"
        header (type: test)
            :matches
            "subject"
            ["*make*money*fast*","*university*dipl*mas*"]
    fileinto (type: action)
        "spam"
else (type: control)
    fileinto (type: action)
        "personal\"
"""
    )
