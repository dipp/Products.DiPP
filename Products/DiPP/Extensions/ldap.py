import ldap
import ldap.modlist
from zLOG import LOG, ERROR, INFO

server = "193.30.112.98"
who = "cn=Manager, dc=dipp,dc=nrw,dc=de"
cred="dippadm"
def connect(self):
    #try: 
    server = self.portal_properties.dipp_properties.ldap_server
    #except:
    #    raise Exception, "no LDAP-Server specified!"

    who = "cn=Manager, dc=dipp,dc=nrw,dc=de"
    cred="dippadm"
    #l = ldap.open(server)
    #return l.simple_bind_s(who, cred)
    ldap = {'server':server,
            'who':who,
            'cred':cred}
    return ldap

#USER_BASE  = "ou=" + journal + ", dc=dipp,dc=nrw,dc=de"
#GROUP_BASE = "ou=groups,ou=" + journal + ", dc=dipp,dc=nrw,dc=de"

#print USER_BASE

def user_base(self):
    try:
        ldap_ou = self.portal_properties.dipp_properties.ldap_ou
    except:
        ldap_ou = "eleed"
    user_base  = "ou=" + ldap_ou + ", dc=dipp,dc=nrw,dc=de"
    return user_base

def group_base(self):
    try:
        ldap_ou = self.portal_properties.dipp_properties.ldap_ou
    except:
        ldap_ou = "eleed"
    group_base  = "ou=" + ldap_ou + ", dc=dipp,dc=nrw,dc=de"
    return group_base



def main(key,keyword):
    try:
        l = ldap.open(server)
        l.simple_bind_s(who, cred)
        print "Successfully bound to server.\n"
        print "Searching..\n"
        return get_users(l,key, keyword)
    except ldap.LDAPError, error_message:
        print "Couldn't Connect. %s " % error_message

def XmembersOfGroup(self,group):
    l = connect(self)
    uids = get_users(self,l,'cn', group)
    members = []
    for uid in uids:
        members.append(get_user(self,l,'uid',uid))
    return members

    
def membersOfGroup(self,group):
    lc = connect(self)
    server = lc['server']
    who    = lc['who']
    cred   = lc['cred']
    #l = ldap.open(server)
    #return  l.simple_bind_s(who, cred)
    
    try:
        l = ldap.open(server)
        l.simple_bind_s(who, cred)
        print "Successfully bound to server.\n"
        print "Searching..\n"
        uids = get_users(self,l,'cn', group)
        members = []
        for uid in uids:
            members.append(get_user(self,l,'uid',uid))
        return members
    except ldap.LDAPError, error_message:
        print "Couldn't Connect. %s " % error_message

def member(self,uid):
    lc = connect(self)
    server = lc['server']
    who    = lc['who']
    cred   = lc['cred']
    try:
        l = ldap.open(server)
        l.simple_bind_s(who, cred)
        print "Successfully bound to server.\n"
        print "Searching..\n"
        member = get_user(self,l,'uid', uid)
        return member
    except ldap.LDAPError, error_message:
        print "Couldn't Connect. %s " % error_message


def get_users(self, l, key, keyword):

    """
        Get all members of a given groupname
        returns a list of uids
    """

    base   = group_base(self)
    scope  = ldap.SCOPE_SUBTREE
    filter = key + "=" + "*" + keyword + "*"
    retrieve_attributes = ('uniqueMember',)
    count  = 0
    result_set = []
    timeout = 0
    try:
        result_id = l.search(base, scope, filter, retrieve_attributes)
        while l:
            result_type, result_data = l.result(result_id, timeout)
            if (result_data == []):
                break
            else:
                if result_type == ldap.RES_SEARCH_ENTRY:
                    result_set.append(result_data)

            if len(result_set) == 0:
                print "No Results."
                uids = []
        #print "len",len(result_set)
        uids = []
        for i in range(len(result_set)):
            for entry in result_set[i]:         
                try:
                    for member in entry[1]['uniqueMember']:
                        uid = ldap.explode_dn(member,notypes=1)[0]
                        #print uid
                        uids.append(uid)
                    count = count + 1
                except:
                    pass

    except ldap.LDAPError, error_message:
        print error_message

    return uids


def get_user(self ,l, key, keyword):

    """
    get memberdata of a given uid
    return uid,cn,mail
    """

    defaultLanguage = self.portal_properties.defaultLanguage
     
    base   = user_base(self)
    scope  = ldap.SCOPE_SUBTREE
    filter = key + "=" + "*" + keyword + "*"
    retrieve_attributes = ('uid', 'cn', 'mail', 'preferredLanguage')
    count  = 0
    result_set = []
    timeout = 0
    try:
        result_id = l.search(base, scope, filter, retrieve_attributes)
        while l:
            result_type, result_data = l.result(result_id, timeout)
            if (result_data == []):
                break
            else:
                if result_type == ldap.RES_SEARCH_ENTRY:
                    result_set.append(result_data)

            if len(result_set) == 0:
                print "No Results."
                return
        #print "len",len(result_set)
        for i in range(len(result_set)):
            for entry in result_set[i]:         
                try:
                    uid               = entry[1]['uid'][0]
                    cn                = entry[1]['cn'][0]
                    mail              = entry[1]['mail'][0]
                    preferredLanguage = entry[1].get('preferredLanguage',[defaultLanguage])
                    count             = count + 1
                    user = {'uid':uid,
                            'mail':mail,
                            'cn':cn, 
                            'preferredLanguage':preferredLanguage[0]}
                    print "%d. %s\t %s\t %s" % (count, uid, name, mail)
                except:
                    pass
            return user

    except ldap.LDAPError, error_message:
        print error_message


if __name__=='__main__':
    main()


def usersAssignableTo(self, process_id, activity_id, object=None):
    """ List all user name assignable to activity in the process """
    of = getattr(self,'portal_openflow')
    activity = getattr(getattr(of,process_id),activity_id)
    lc = connect(self)
    server = lc['server']
    who    = lc['who']
    cred   = lc['cred']
    try:
        l = ldap.open(server)
        l.simple_bind_s(who, cred)
        print "Successfully bound to server.\n"
        print "Searching..\n"
        members = []
        for group in activity.getPullRoles():
            uids = get_users(self,l,'cn', group)
            for uid in uids:
                members.append(get_user(self,l,'uid',uid))
        return members

    except ldap.LDAPError, error_message:
        print "Couldn't Connect. %s " % error_message

def addEntry(self,password,uid,properties):
    server = self.portal_properties.dipp_properties.ldap_server
    ou = self.portal_properties.dipp_properties.ldap_ou
    who = "uid=" + uid + ",ou=" + ou  + ",dc=dipp,dc=nrw,dc=de"
    cred = password
    l = ldap.open(server)
    l.simple_bind_s(who, cred)
    
    givenName = properties['givenName']
    surname = properties['surname']
    cn = properties['givenName'] + " " + properties['surname']
    preferredLanguage = properties['preferredLanguage']
    mail = properties['email']
    LOG('DiPP', INFO, mail)
    modlist = ldap.modlist.modifyModlist({'givenName':uid},{'givenName':givenName})
    l.modify(who, modlist)
    modlist = ldap.modlist.modifyModlist({'surname':uid},{'surname':surname})
    l.modify(who, modlist)
    modlist = ldap.modlist.modifyModlist({'cn':uid},{'cn':cn})
    l.modify(who, modlist)
    modlist = ldap.modlist.modifyModlist({'preferredLanguage':uid},{'preferredLanguage':preferredLanguage})
    l.modify(who, modlist)
    modlist = ldap.modlist.modifyModlist({'mail':uid},{'mail':mail})
    l.modify(who, modlist)
    return modlist

def auth(self,username,password):
    server = self.portal_properties.dipp_properties.ldap_server
    ou = self.portal_properties.dipp_properties.ldap_ou
    uid = username
    who = "uid=" + uid + ",ou=" + ou  + ",dc=dipp,dc=nrw,dc=de"
    cred = password
    try:
        l = ldap.open(server)
        l.simple_bind_s(who, cred)
        return True
    except ldap.LDAPError, error_message:
        return False
