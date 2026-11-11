from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import mm
import os
os.makedirs("downloads",exist_ok=True)
s=getSampleStyleSheet()
s.add(ParagraphStyle(name="TitleX",parent=s["Title"],fontSize=22,textColor=colors.HexColor("#294638"),alignment=1,spaceAfter=8))
s.add(ParagraphStyle(name="SubX",parent=s["Normal"],fontSize=10,textColor=colors.HexColor("#68736b"),alignment=1,spaceAfter=16))
s.add(ParagraphStyle(name="HeadX",parent=s["Heading2"],fontSize=13,textColor=colors.HexColor("#d96d4b"),spaceBefore=9,spaceAfter=6))
def P(t,n="Normal"): return Paragraph(t,s[n])
def tab(rows,widths):
 t=Table(rows,colWidths=widths)
 t.setStyle(TableStyle([("GRID",(0,0),(-1,-1),.5,colors.HexColor("#d9ded5")),("BACKGROUND",(0,0),(-1,0),colors.HexColor("#f7f4ed")),("VALIGN",(0,0),(-1,-1),"MIDDLE"),("TOPPADDING",(0,0),(-1,-1),8),("BOTTOMPADDING",(0,0),(-1,-1),8)]))
 return t
def footer(c,d):
 c.saveState(); c.setFont("Helvetica",8); c.setFillColor(colors.grey); c.drawString(18*mm,9*mm,"PRINTLY • LITTLE STEPS COUNT"); c.drawRightString(A4[0]-18*mm,9*mm,f"Page {d.page}"); c.restoreState()
def build(name,story):
 SimpleDocTemplate("downloads/"+name,pagesize=A4,rightMargin=18*mm,leftMargin=18*mm,topMargin=17*mm,bottomMargin=21*mm).build(story,onFirstPage=footer,onLaterPages=footer)
# 05 Habit tracker
a=[Spacer(1,10*mm),P("THE DAILY HABIT TRACKER","TitleX"),P("Build small routines. Notice your progress. Keep showing up.","SubX"),P("MONTHLY INTENTION","HeadX"),P("This month, I want to make more room for: __________________________________________"),P("MY HABITS","HeadX"),tab([["Habit","Why it matters","Target"]]+[["______________________","______________________","________"] for _ in range(7)],[58*mm,76*mm,35*mm]),P("30-DAY CHECK-IN","HeadX")]
for start in (1,11,21):
 h=["Habit"]+[str(i) for i in range(start,min(start+10,31))]
 a += [tab([h]+[["________"]+["□"]*(len(h)-1) for _ in range(4)],[35*mm]+[13.4*mm]*(len(h)-1)),Spacer(1,5*mm)]
a += [PageBreak(),P("WEEKLY REFLECTION","TitleX"),P("A quick pause to learn what works and what needs adjusting.","SubX")]
for w in range(1,5):
 a += [P(f"WEEK {w}","HeadX"),P("A small win I am proud of: ________________________________________________________"),P("What made my habits easier? ______________________________________________________"),P("What got in the way? ____________________________________________________________"),P("One adjustment for next week: ____________________________________________________"),Spacer(1,5*mm)]
build("05_Daily_Habit_Tracker.pdf",a)
# 06 Meal planner
a=[Spacer(1,10*mm),P("WEEKLY MEAL PLANNER","TitleX"),P("Plan simple meals, make a focused shopping list, and reduce weekday guesswork.","SubX"),P("WEEK OF: __________________________  HOUSEHOLD: __________________________"),P("WEEKLY MEAL PLAN","HeadX"),tab([["Day","Breakfast","Lunch","Dinner"]]+[[d,"","",""] for d in ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]],[25*mm,43*mm,43*mm,43*mm]),P("PREP AHEAD","HeadX"),tab([["Task","Notes"],["Wash / chop vegetables",""],["Cook grains / basics",""],["Defrost / marinate",""],["Pack snacks / lunches",""]],[65*mm,132*mm]),PageBreak(),P("GROCERY SHOPPING LIST","TitleX"),P("Take this list with you and tick items as you shop.","SubX")]
for cat in ["Vegetables & fruit","Dairy & chilled","Grains & bakery","Protein","Pantry & spices","Snacks & drinks","Household"]:
 a += [P(cat,"HeadX"),tab([["Item","Quantity","Done"]]+[["","","□"] for _ in range(3)],[105*mm,55*mm,37*mm]),Spacer(1,3*mm)]
a += [P("BUDGET & NOTES","HeadX"),P("Planned grocery budget: __________________  Actual spend: __________________"),P("Meals to repeat next week: ________________________________________________________")]
build("06_Weekly_Meal_Planner_Grocery_List.pdf",a)
# 07 Student planner
a=[Spacer(1,10*mm),P("STUDENT STUDY PLANNER","TitleX"),P("Turn big subjects into manageable study sessions.","SubX"),P("STUDENT: __________________________  WEEK OF: __________________________"),P("WEEKLY STUDY MAP","HeadX"),tab([["Day","Subject / Topic","Study goal","Done"]]+[[d,"","","□"] for d in ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]],[22*mm,58*mm,80*mm,17*mm]),P("TOP 3 PRIORITIES","HeadX"),tab([["Priority","Next action","Due"],["1","",""],["2","",""],["3","",""]],[45*mm,95*mm,37*mm]),PageBreak(),P("DAILY FOCUS SESSION","TitleX"),P("Use one copy for each important study day.","SubX")]
for i in range(1,4):
 a += [P(f"SESSION {i}","HeadX"),P("Subject: _____________________  Topic: _____________________  Time: ______________"),P("What I want to understand: _______________________________________________________"),tab([["Focus block","Task","Complete"],["1","","□"],["2","","□"],["3","","□"]],[35*mm,112*mm,30*mm]),Spacer(1,6*mm)]
a += [P("END-OF-WEEK REVIEW","HeadX"),P("What improved? _________________________________________________________________"),P("What needs more practice? _______________________________________________________"),P("My next week's first step: _______________________________________________________")]
build("07_Student_Study_Planner.pdf",a)
# 08 Invoice and quote kit
a=[Spacer(1,10*mm),P("SMALL BUSINESS INVOICE & QUOTE KIT","TitleX"),P("A printable worksheet to prepare estimates, record payments and follow up confidently.","SubX"),P("BUSINESS DETAILS","HeadX"),P("Business name: _________________________________________________________________"),P("Address / phone / email: ________________________________________________________"),P("Tax / registration details (if applicable): ___________________________________________"),P("QUOTE / ESTIMATE","HeadX"),P("Quote number: __________________  Date: ______________  Valid until: ______________"),P("Customer name: ______________________________  Contact: _______________________"),P("Project / service: _______________________________________________________________"),tab([["Description","Qty","Rate","Amount"]]+[["","","",""] for _ in range(6)],[82*mm,22*mm,35*mm,38*mm]),P("Subtotal: __________________  Discount: __________________  Tax (if applicable): __________________"),P("TOTAL QUOTED: ______________________________"),P("Terms / delivery timeline: _______________________________________________________"),PageBreak(),P("INVOICE & PAYMENT RECORD","TitleX"),P("Invoice number: __________________  Invoice date: ______________  Due date: ______________"),P("Customer / client: _______________________________________________________________"),tab([["Description","Qty","Rate","Amount"]]+[["","","",""] for _ in range(6)],[82*mm,22*mm,35*mm,38*mm]),P("Subtotal: __________________  Tax (if applicable): __________________  Total due: __________________"),P("Payment received: __________________  Balance due: __________________"),P("Payment method / reference: ____________________________________________________"),P("PAYMENT FOLLOW-UP","HeadX"),tab([["Date","Follow-up / note","Next action"],["","",""],["","",""],["","",""]],[35*mm,90*mm,52*mm]),Spacer(1,5*mm),P("Adapt tax fields and invoice requirements to the rules that apply to your business. Planning aid only; not tax or legal advice.")]
build("08_Small_Business_Invoice_Quote_Kit.pdf",a)
