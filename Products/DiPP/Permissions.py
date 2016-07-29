from Products.CMFCore import permissions as CMFCorePermissions
from AccessControl.SecurityInfo import ModuleSecurityInfo
from Products.CMFCore.permissions import setDefaultRoles

security = ModuleSecurityInfo("DiPP")

security.declarePublic("MANAGE_JOURNAL")
MANAGE_JOURNAL = "DiPP: Manage Journal"

security.declarePublic("VIEW_STATISTICS")
VIEW_STATISTICS = "DiPP: View Statistics"

setDefaultRoles(MANAGE_JOURNAL, ())
setDefaultRoles(VIEW_STATISTICS, ())

# Publishing Permission
ADD_CONTENTS_PERMISSION  = "Fedora: Add Content"
setDefaultRoles(ADD_CONTENTS_PERMISSION, ('Manager',))
VIEW_CONTENTS_PERMISSION = "Fedora: View Content"
setDefaultRoles(VIEW_CONTENTS_PERMISSION, ('Manager',))
EDIT_CONTENTS_PERMISSION = "Fedora: Edit Content"
setDefaultRoles(EDIT_CONTENTS_PERMISSION, ('Manager',))

# Review Permission
VIEW_ORIGINAL_MANUSCRIPT_PERMISSION = "DiPPReview: View the original manuscript"
VIEW_ANONYM_MANUSCRIPT_PERMISSION = "DiPPReview: View the anonymized manuscript"
ADD_ANONYM_MANUSCRIPT_PERMISSION = "DiPPReview: Add the anonymized manuscript"
VIEW_AUTHOR_REVIEW_PERMISSION = "DiPPReview: View the reviewers report for the author"
VIEW_EDITOR_REVIEW_PERMISSION = "DiPPReview: View the reviewers report for the editor"
VIEW_ORIGINAL_ATTACHMENT_PERMISSION = "DiPPReview: View the original attachment"
VIEW_ANONYM_ATTACHMENT_PERMISSION = "DiPPReview: View the anonymized attachment"
VIEW_REVIEWER_DETAILS = "DiPPReview: View reviewer details"
VIEW_AUTHOR_DETAILS = "DiPPReview: View author details"
