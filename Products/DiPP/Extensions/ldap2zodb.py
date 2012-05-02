# -*- coding: utf-8 -*-
import ldap
import ldap.modlist
from StringIO import StringIO
from zLOG import LOG, ERROR, INFO



def getGroups(self):

    SERVER = "127.0.0.1"
    WHO = "cn=Manager, dc=dipp,dc=nrw,dc=de"
    CRED = "dippadm"
    #OU = "training"
    OU = self.portal_properties.dipp_properties.ldap_ou
    
    out = StringIO()
    try:
        l = ldap.open(SERVER)
        l.simple_bind_s(WHO, CRED)
    except ldap.LDAPError, error_message:
        print >> out, "Couldn't Connect. %s " % error_message
    

    
    base   = "ou=groups,ou=" + OU + ", dc=dipp,dc=nrw,dc=de"
    scope  = ldap.SCOPE_ONELEVEL
    filter = "cn=*"
    retrieve_attributes = ('uniqueMember',)
    count  = 0
    result_set = []
    timeout = 0
    groups = []
    try:
        result_id = l.search(base, scope, filter, retrieve_attributes)
        while 1:
            result_type, result_data = l.result(result_id, timeout)
            if (result_data == []):
                break
            else:
                if result_type == ldap.RES_SEARCH_ENTRY:
                    result_set.append(result_data)

        if len(result_set) == 0:
            print >> out, "no results"
        
        for i in range(len(result_set)):
            for entry in result_set[i]:
                uid = ldap.explode_dn(entry[0],notypes=1)[0]
                groups.append(uid)
        
    except ldap.LDAPError, error_message:
        print >> out, error_message
    
    return groups

def ldap2zodb(self):

    out = StringIO()
    SERVER = "127.0.0.1"
    WHO = "cn=Manager, dc=dipp,dc=nrw,dc=de"
    CRED = "dippadm"
    #OU = "training"
    OU = self.portal_properties.dipp_properties.ldap_ou
    
    groups = getGroups(self)
     
    for KEYWORD in groups: 
        print >> out, "\n### " + KEYWORD + "###"
        group = self.portal_groups.getGroupById(KEYWORD)
        if group == None:
            print >> out, "Group %s does not exist, ceating it now" % KEYWORD
            self.portal_groups.addGroup(KEYWORD,(),())
            group = self.portal_groups.getGroupById(KEYWORD)
            
        print >> out, "Plonegroup: %s" % group
        
        base   = "ou=groups,ou=" + OU + ", dc=dipp,dc=nrw,dc=de"
        scope  = ldap.SCOPE_SUBTREE
        filter = "cn=" + KEYWORD
        retrieve_attributes = ('uniqueMember',)
        count  = 0
        result_set = []
        timeout = 0
        try:
            l = ldap.open(SERVER)
            l.simple_bind_s(WHO, CRED)
            print >> out, "(Successfully bound to %s, %s)" % (SERVER, base)
        except ldap.LDAPError, error_message:
            print >> out, "Couldn't Connect. %s " % error_message
        

        
        try:
            result_id = l.search(base, scope, filter, retrieve_attributes)
            while 1:
                result_type, result_data = l.result(result_id, timeout)
                if (result_data == []):
                    break
                else:
                    if result_type == ldap.RES_SEARCH_ENTRY:
                        result_set.append(result_data)

            if len(result_set) == 0:
                print >> out, "no results"
            
            for i in range(len(result_set)):
                for entry in result_set[i]:
                    for member in entry[1]['uniqueMember']:
                        uid = ldap.explode_dn(member,notypes=1)[0]
                        # skip user 'cn=Manager,dc=dipp,dc=nrw,dc=de' 
                        if uid != 'Manager':
                            try:
                                group.addMember(uid)
                                print >> out, '%s: Member added to group %s' % (uid,group)
                            except:
                                print >> out, '%s: Could not add member to group' % uid
            
        except ldap.LDAPError, error_message:
            print >> out, error_message
    
    print >> out, "\n### Roles ###"

    try:
        groupstool=self.portal_groups
        groupstool.editGroup('Herausgeber', roles=('Herausgeber',), groups=())
        groupstool.editGroup('Redakteure', roles=('Redakteur',), groups=())
        groupstool.editGroup('Gastherausgeber', roles=('Gastherausgeber',), groups=())
        groupstool.editGroup('Manager', roles=('Manager',), groups=())
        print >> out, "Set roles to groups"
    except:
        print >> out, "Could not assign roles to groups"

    return out.getvalue()

