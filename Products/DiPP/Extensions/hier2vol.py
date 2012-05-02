from Products.CMFCore.utils import getToolByName
from StringIO import StringIO
from Products.ATContentTypes.migration.walker import CatalogWalker
try:
    from Products.contentmigration.migrator import InlineFieldActionMigrator
    from Products.contentmigration.walker import CustomQueryWalker
    haveContentMigrations = True
except ImportError:
    haveContentMigrations = False

#from Products.contentmigration.walker import *
from Products.ATContentTypes.migration.migrator import CMFFolderMigrator, CMFItemMigrator
#from Archetypes.public import *
# for zope >2.7:
#import transaction
from Products.CMFCore.utils import getToolByName


class MyMigrator(CMFFolderMigrator):
    walkerClass = CatalogWalker
    src_meta_type = 'FedoraHierarchie'
    src_portal_type = 'FedoraHierarchie'
    dst_meta_type = 'Volume'
    dst_portal_type = 'Volume'
    # map = {'PID':'PID',
    #        'DsID':'DsID'}

def uniq(inlist):
    # order preserving
    uniques = []
    for item in inlist:
        if item not in uniques:
            uniques.append(item)
    return uniques


def find(self):
    
    #FOLDER = ('issues',)
    FOLDER = ('',)
    DEPTH = 2
    out = StringIO()
    
    portal = getToolByName(self, 'portal_url').getPortalObject()
    portal_path = portal.getPhysicalPath()
    folder_path = portal_path + FOLDER
    path = '/'.join(folder_path)
    print >>out, path
    query = {'query':path, 'depth':DEPTH}
    results = self.portal_catalog(meta_type="FedoraHierarchie", path=query)
    
    return query 

    print >>out, len(results)
    for result in results:
        print >>out, result.getURL()
    return out.getvalue()


def migrate(self):
      """Run the migration"""

      out = StringIO()
      print >> out, "Starting migration"

      portal_url = getToolByName(self, 'portal_url')
      portal = portal_url.getPortalObject()

      migrators = (MyMigrator,)

      for migrator in migrators:
          walker = CustomQueryWalker(portal, migrator, 
                             query = {'path' : find(self)})

          # walker = migrator.walkerClass(portal, migrator)
          walker.go(out=out)

          print >> out, walker.getOutput()

      print >> out, "Migration finished"
      return out.getvalue()
