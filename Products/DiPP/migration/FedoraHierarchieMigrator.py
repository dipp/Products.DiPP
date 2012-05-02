from Products.CMFCore.utils import getToolByName
from Products.ATContentTypes.migration.walker import CatalogWalker
from Products.ATContentTypes.migration.migrator import CMFFolderMigrator
from StringIO import StringIO

try:
    from Products.contentmigration.migrator import InlineFieldActionMigrator
    from Products.contentmigration.walker import CustomQueryWalker
    haveContentMigrations = True
except ImportError:
    haveContentMigrations = False

MAP = {'PID':'',
#       'description':'',
       'MetaType':'',
       'Volume':'',
       'Issue':'',
       'IssueDate':'',
#       'CompleteIssue':'',
#       'Body':'',
#      'TitleImage':'',
      }
class IssueMigrator(CMFFolderMigrator):
    walkerClass = CatalogWalker
    src_meta_type = 'FedoraHierarchie'
    src_portal_type = 'FedoraHierarchie'
    dst_meta_type = 'Issue'
    dst_portal_type = 'Issue'
    map = MAP
    
class VolumeMigrator(CMFFolderMigrator):
    walkerClass = CatalogWalker
    src_meta_type = 'FedoraHierarchie'
    src_portal_type = 'FedoraHierarchie'
    dst_meta_type = 'Volume'
    dst_portal_type = 'Volume'
    map = MAP
    
def migrate(self, target):
    out = StringIO()
    catalog = getToolByName(self,'portal_catalog')
    portal_url = getToolByName(self, 'portal_url')
    portal = portal_url.getPortalObject()
    
    id = self.id
    path = '/'.join(self.getParentNode().getPhysicalPath())
    results = catalog(meta_type="FedoraHierarchie", getId=id, path={'query':path, 'depth':1})
    
    if target == 'Issue':
        migrator = IssueMigrator
    elif target == 'Volume':
        migrator = VolumeMigrator
    
    
    walker = CustomQueryWalker(portal, migrator, query = {'path' : {'query':path, 'depth':1}, 'getId':id})
    walker.go(out=out)

    print >> out, walker.getOutput()
    
    return out.getvalue()
