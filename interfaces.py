from zope.interface import Interface

class IFedoraArticle(Interface):
    """An article, which has gone through a peer review. Please add through the EDITORIAL TOOLBOX"""
    
class IFedoraDocument(Interface):
    """A Document belonging to an article"""
    
class IFedoraXML(Interface):
    """The XML Version of the article text"""
    
class IFedoraMultimedia(Interface):
    """Binary data added to an article: Images, video, excelsheets,.."""
    
class IFedoraHierarchie(Interface):
    """For organising the Articles, Superseeded by Volumes and Issues"""
    
class IFedoraVolume(Interface):
    """Journal volumes, contains the issus of one year"""
    
class IFedoraIssue(Interface):
    """Issues with articles"""
