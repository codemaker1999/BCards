from reportlab.platypus import BaseDocTemplate, Frame, FrameBreak, PageTemplate
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.platypus.flowables import Image
# init
elements=[]
doc = BaseDocTemplate('cards.pdf',pagesize=letter,showBoundary=0,)
cardx,cardy = 3.5*inch, 2*inch
# Two Columns
frame1 = Frame( 0.65*inch,         0.5*inch, cardx+2, 10*inch+2, id='col1',
                leftPadding=0, bottomPadding=0, rightPadding=0, topPadding=0)
frame2 = Frame( 0.65*inch + cardx + 2, 0.5*inch, cardx+2, 10*inch+2, id='col2',
                leftPadding=0, bottomPadding=0, rightPadding=0, topPadding=0)
# Card Defn
def addCardFront():
  img = Image('front.png', width=3.5*inch, height=2*inch)
  elements.append(img)

def addCardBack():
  img = Image('back.png', width=3.5*inch, height=2*inch)
  elements.append(img)

def addAllFronts():
  # 2 columns of 5 cards
  for i in xrange(5):
    addCardFront()
  elements.append(FrameBreak())
  for i in xrange(5):
    addCardFront()
  #elements.append(PageBreak())

def addAllBacks():
  # 2 columns of 5 cards
  for i in xrange(5):
    addCardBack()
  elements.append(FrameBreak())
  for i in xrange(5):
    addCardBack()

# Page template
frames = [frame1,frame2]#[frame11,frame12,frame13,frame14,frame21,frame22,frame23,frame24]
doc.addPageTemplates([PageTemplate(id='TwoCol',frames=frames), ])

# Testing
addAllFronts()
addAllBacks()
# Construct pdf
doc.build(elements)
