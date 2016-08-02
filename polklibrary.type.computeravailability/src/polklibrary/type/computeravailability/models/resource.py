from plone import api
from plone.app.textfield import RichText
from plone.app.textfield.widget import RichTextWidget
from plone.supermodel import model
from zope import schema
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

resource_types = SimpleVocabulary([
    SimpleTerm(value=u'PC', title=u'PC'),
    SimpleTerm(value=u'MAC', title=u'MAC'),
])

resource_locations = SimpleVocabulary([
    SimpleTerm(value=u'1st North - EMC', title=u'1st North - EMC'),
    SimpleTerm(value=u'1st North - Polk Lab', title=u'1st North - Polk Lab'),
    SimpleTerm(value=u'1st South - Polk 101', title=u'1st South - Polk 101'),
    SimpleTerm(value=u'2nd North - Main Stacks', title=u'2nd North - Main Stacks'),
    SimpleTerm(value=u'2nd South - Periodicals', title=u'2nd South - Periodicals'),
    SimpleTerm(value=u'3rd North - Quiet Study', title=u'3rd North - Quiet Study'),
    SimpleTerm(value=u'3rd South - Gov Info', title=u'3rd South - Gov Info'),
])

class IResourceItem(model.Schema):

    title = schema.TextLine(
            title=u"Title",
            required=True,
        )
        
    resources = schema.Choice(
            title=u"Resource type",
            source=resource_types,
            required=False,
        )
        
    activated = schema.Bool(
            title=u"Is resource available?",
            required=False,
        )
        
    reference = schema.Choice(
            title=u"Location",
            source=resource_locations,
            required=False,
        )
