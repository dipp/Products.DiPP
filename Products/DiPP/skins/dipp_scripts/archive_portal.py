style_sheets = ['plone.css','ploneColumns.css','ploneCustom.css','dipp.css','dipp_article.css']
graphics = ['bullet.gif','portal_logo']
index = 'index.html'

print "<a href='%s'>site entry point</a><br>" % context.absolute_url()
print "<a href='%s/%s'>site index</a><br>" % (context.absolute_url(), index)
for item_name in style_sheets + graphics:
    print "<a href='%s/%s'>%s</a><br>" % (context.absolute_url(), item_name, item_name)

for dir in context.portal_catalog(portal_type='Folder', review_state='published'):
    print "<a href='%s/%s'>%s</a><br>" % (dir.getURL(), index, dir.id)

return printed
