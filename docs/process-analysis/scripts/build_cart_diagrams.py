"""Generate editable draw.io pages and matching PNG previews. Requires Pillow."""
from pathlib import Path
import math
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parents[1]
FONT_DIR = Path('C:/Windows/Fonts')
FONT = ImageFont.truetype(str(FONT_DIR / 'arial.ttf'), 21)
BOLD = ImageFont.truetype(str(FONT_DIR / 'arialbd.ttf'), 30)
SMALL = ImageFont.truetype(str(FONT_DIR / 'arial.ttf'), 18)
COLORS = {'process': ('#F1F5F9', '#64748B'), 'decision': ('#FFF4D5', '#C58B18'),
          'open': ('#F1EAFE', '#8B6BB1'), 'end': ('#DEF3EB', '#2C8566'),
          'error': ('#FFF0EC', '#C76C50'), 'link': ('#E9F0FF', '#5278B5')}
pages = []

def page(title, height=1800):
    p = {'title': title, 'height': height, 'nodes': {}, 'edges': []}
    pages.append(p)
    return p

def node(p, key, text, x, y, w=390, h=120, kind='process'):
    p['nodes'][key] = (text, x, y, w, h, kind)

def edge(p, a, b, label='', start='bottom', end='top', via=()):
    p['edges'].append((a, b, label, start, end, via))

p = page('Cart review', 1780)
node(p,'start','Signed-in customer opens cart',490,150,kind='end')
node(p,'load','Retrieve saved cart; apply retention and current-price rules (page 5)',490,340,kind='link')
node(p,'loaded','Did retrieval succeed?',490,530,kind='decision')
node(p,'error',"Could not load cart. Offer Retry; do not claim empty or zero subtotal.",950,530,kind='error')
node(p,'empty','Are there any active saved items?',490,760,kind='decision')
node(p,'blank','No items: Cart is empty; CAD 0.00; Continue shopping. Explain expiry if applicable.',30,760,kind='end')
node(p,'review','Show names, quantities, prices, line totals and subtotal in CAD; demo pricing notice',490,980)
node(p,'choice','Customer chooses an available action',490,1190,kind='decision')
node(p,'update','Update quantity: page 2. Unresolved-item restrictions apply.',30,1410,kind='link')
node(p,'remove','Remove item: page 3. Unresolved-item restrictions apply.',490,1410,kind='link')
node(p,'shop','Continue shopping: return to products; saved items unchanged',950,1410,kind='end')
edge(p,'start','load'); edge(p,'load','loaded'); edge(p,'loaded','error','No','right','left')
edge(p,'error','load','Customer Retry','top','right',[(1145,400)])
edge(p,'loaded','empty','Yes'); edge(p,'empty','blank','No','left','right'); edge(p,'empty','review','Yes')
edge(p,'review','choice'); edge(p,'choice','update','Update','left','top',[(225,1250)])
edge(p,'choice','remove','Remove'); edge(p,'choice','shop','Continue','right','top',[(1145,1250)])
edge(p,'blank','shop','Continue shopping','left','right',[(15,1580),(1360,1580),(1360,1470)])

p = page('Quantity update', 1900)
node(p,'start','Customer chooses quantity update',490,150,kind='end')
node(p,'blocked','Earlier update for this item processing or unconfirmed?',490,340,kind='decision')
node(p,'recover','Prevent another update/removal for this item; Check update status: page 4',950,340,kind='link')
node(p,'input','Customer enters quantity',490,550)
node(p,'valid','Whole number from 1 to 10?',490,740,kind='decision')
node(p,'invalid','Enter a whole number from 1 to 10. Saved quantities and totals unchanged.',30,740,kind='error')
node(p,'save','Attempt to save requested quantity',490,950)
node(p,'result','What outcome is confirmed?',490,1140,kind='decision')
node(p,'success','Success: display saved quantity and totals; Quantity updated successfully. Reset retention.',30,1380,kind='end')
node(p,'fail','Confirmed failure: show confirmed values; Update failed. Please try again. Customer chooses retry.',490,1380,kind='error')
node(p,'unknown','Unknown outcome: do not infer failure. Recovery: page 4.',950,1380,kind='link')
node(p,'return','Return to cart review (page 1)',30,1610,kind='end')
edge(p,'start','blocked'); edge(p,'blocked','recover','Yes','right','left'); edge(p,'blocked','input','No')
edge(p,'input','valid'); edge(p,'valid','invalid','No','left','right')
edge(p,'invalid','input','Correct input','top','left',[(225,610)])
edge(p,'valid','save','Yes'); edge(p,'save','result')
edge(p,'result','success','Success','left','top',[(225,1200)])
edge(p,'result','fail','Failure'); edge(p,'result','unknown','Unknown','right','top',[(1145,1200)])
edge(p,'success','return')
edge(p,'fail','input','Customer Retry','bottom','right',[(685,1760),(1370,1760),(1370,610)])

p = page('Item removal', 1900)
node(p,'start','Customer chooses Remove for a cart line',490,150,kind='end')
node(p,'blocked','Earlier quantity update processing or unconfirmed for this item?',490,340,kind='decision')
node(p,'recover','Prevent removal; explain restriction; Check update status: page 4',950,340,kind='link')
node(p,'attempt','Attempt removal of the entire line',490,570)
node(p,'result','Removal outcome?',490,790,kind='decision')
node(p,'failure','Confirmed failure: keep item and totals; Item removal failed. Please try again.',30,790,kind='error')
node(p,'unknown','Unknown: no success/failure claim or automatic repeat. Removal recovery remains open (CART-Q-06).',950,790,kind='open')
node(p,'success','Confirmed success: remove line, recalculate subtotal; Item removed successfully. Record successful change.',490,1030)
node(p,'empty','Is the resulting cart empty?',490,1270,kind='decision')
node(p,'blank','Yes: Cart is empty; CAD 0.00; Continue shopping (page 1)',950,1500,kind='end')
node(p,'review','No: display remaining items and subtotal; return to review (page 1)',30,1500,kind='end')
edge(p,'start','blocked'); edge(p,'blocked','recover','Yes','right','left'); edge(p,'blocked','attempt','No')
edge(p,'attempt','result'); edge(p,'result','failure','Failure','left','right'); edge(p,'result','unknown','Unknown','right','left')
edge(p,'failure','start','Customer Retry','top','left',[(225,210)])
edge(p,'result','success','Success'); edge(p,'success','empty')
edge(p,'empty','blank','Yes','right','top',[(1145,1330)]); edge(p,'empty','review','No','left','top',[(225,1330)])

p = page('Unresolved quantity-update recovery', 2320)
node(p,'entry','Entry from pages 2 or 3: original quantity update unresolved',490,150,kind='end')
node(p,'lock','Block another update and removal for this item. Label old values last confirmed.',490,350)
node(p,'check','Customer selects Check update status; check original request, do not repeat mutation',490,550)
node(p,'status','What does the status check establish?',490,760,kind='decision')
node(p,'processing','Processing confirmed: explain verified state; keep restrictions and status-check action.',30,760,kind='process')
node(p,'unknown','Check failed / unknown: explain outcome unconfirmed; keep restrictions and status-check action.',950,760,kind='error')
node(p,'retrieve','Terminal success or failure confirmed; original request can no longer alter cart. Retrieve saved cart.',490,1030)
node(p,'loaded','Did fresh cart retrieval succeed?',490,1270,kind='decision')
node(p,'success','Yes, request succeeded: display current saved values and Update confirmed.',30,1510,kind='end')
node(p,'failed','Yes, request failed: display confirmed values and failure message. Customer may retry.',490,1510,kind='error')
node(p,'loadfail','No: success confirmed? Explain update confirmed but refresh failed; keep removal blocked; offer Refresh cart.',950,1510,kind='error',h=155)
node(p,'unlock','On successful retrieval: enable removal if item remains present. Return to cart review (page 1).',30,1780,w=850)
node(p,'open','OPEN: failure-confirmed / retrieval-failed branch; prolonged recovery and safe unlock; concurrency and technical feasibility. CART-Q-01 to CART-Q-03.',30,2040,w=1310,h=130,kind='open')
edge(p,'entry','lock'); edge(p,'lock','check'); edge(p,'check','status')
edge(p,'status','processing','Processing','left','right'); edge(p,'status','unknown','Unknown','right','left')
edge(p,'processing','check','Check again','top','left',[(225,610)])
edge(p,'unknown','check','Check again','top','right',[(1145,610)])
edge(p,'status','retrieve','Terminal result'); edge(p,'retrieve','loaded')
edge(p,'loaded','success','Yes / success','left','top',[(225,1330)])
edge(p,'loaded','failed','Yes / failure'); edge(p,'loaded','loadfail','No','right','top',[(1145,1330)])
edge(p,'success','unlock','Continue','bottom','top',[(225,1740),(455,1740)]); edge(p,'failed','unlock','Continue','bottom','top',[(685,1720),(685,1750),(455,1750)])
edge(p,'loadfail','retrieve','Refresh: success branch','right','right',[(1360,1580),(1360,1090)])
edge(p,'loadfail','open','Failure branch: unresolved','bottom','right',[(1145,1980),(1360,1980),(1360,2105)])

p = page('Supporting rules and scope boundaries', 1900)
node(p,'merge','MERGING: same product and variant share one line; different variants separate. Price alone is not identity.',60,170,w=1250)
node(p,'limit','LIMIT: 1 to 10 per product/variant, including combined additions. Reject excess; preserve saved values.',60,370,w=1250)
node(p,'retention','RETENTION: 30 x 24 hours from last successful add, update or removal. Active before expiry; expired at the instant and afterward.',60,570,w=1250)
node(p,'noreset','NO RESET: viewing, refreshing, sign-in, logout or confirmed failed changes. Explain expired cart; CAD 0.00; Continue shopping.',60,770,w=1250)
node(p,'price','PRICES: on successful refresh apply current price; notify increases/decreases with old/new unit prices in text; recalculate totals.',60,970,w=1250)
node(p,'demo','DEMO: item-price subtotals in CAD, two decimals. No tax/shipping calculation or payment. No stock checks or reservation.',60,1170,w=1250)
node(p,'logout','LOGOUT: included in first increment; retain cart without resetting expiry. Security guarantee, token invalidation and failure behaviour remain OPEN (CART-Q-08).',60,1370,w=1250,h=145,kind='open')
node(p,'scope','These are rule references, not sequential steps. Session expiry, in-flight expiry interactions, prolonged recovery and feasibility still need review.',60,1620,w=1250,h=120,kind='open')

def wrapped(draw, text, width):
    lines = []
    current = ''
    for word in text.split():
        test = (current + ' ' + word).strip()
        if current and draw.textlength(test, font=FONT) > width:
            lines.append(current); current = word
        else:
            current = test
    return lines + [current]

def anchor(n, side):
    _, x, y, w, h, _ = n
    return {'top':(x+w/2,y),'bottom':(x+w/2,y+h),'left':(x,y+h/2),'right':(x+w,y+h/2)}[side]

doc = ET.Element('mxfile', host='app.diagrams.net')
counts = []
for index,p in enumerate(pages,1):
    diagram = ET.SubElement(doc,'diagram',name=f'{index:02} {p["title"]}',id=f'cart-v04-{index}')
    model = ET.SubElement(diagram,'mxGraphModel',grid='1',gridSize='10',page='1',pageWidth='1400',pageHeight=str(p['height']),background='#FFFFFF')
    root = ET.SubElement(model,'root')
    ET.SubElement(root,'mxCell',id='0'); ET.SubElement(root,'mxCell',id='1',parent='0')
    im = Image.new('RGB',(1400,p['height']),'white'); d = ImageDraw.Draw(im)
    metadata = f'Kailas Krishnan | 25 October 2026 | Draft v0.4 | Page {index} of {len(pages)}'
    texts = [('title',f'ShopStack: {p["title"]}',35,22,1330,45,30),('meta',metadata,35,82,1330,35,18),
             ('footer','Simulated case study. Proposed behaviour, not implemented or approved. Purple boxes mark open requirements.',35,p['height']-70,1330,45,18)]
    for key,text,x,y,w,h,size in texts:
        cell=ET.SubElement(root,'mxCell',id=key,value=text,style=f'text;html=0;whiteSpace=wrap;align=left;fontSize={size};fontColor=#172B4D;',vertex='1',parent='1')
        ET.SubElement(cell,'mxGeometry',x=str(x),y=str(y),width=str(w),height=str(h),attrib={'as':'geometry'})
        d.text((x,y),text,font=BOLD if size==30 else SMALL,fill='#172B4D')
    for key,n in p['nodes'].items():
        text,x,y,w,h,kind=n; fill,stroke=COLORS[kind]
        lines=wrapped(d,text,w-38)
        assert len(lines)*26 <= h-12,(p['title'],key,'text overflow')
        cell=ET.SubElement(root,'mxCell',id=key,value=text,style=f'rounded=1;arcSize=12;html=0;whiteSpace=wrap;fillColor={fill};strokeColor={stroke};fontColor=#172B4D;fontFamily=Arial;fontSize=21;spacing=14;',vertex='1',parent='1')
        ET.SubElement(cell,'mxGeometry',x=str(x),y=str(y),width=str(w),height=str(h),attrib={'as':'geometry'})
        d.rounded_rectangle((x,y,x+w,y+h),radius=12,fill=fill,outline=stroke,width=2)
        top=y+(h-len(lines)*26)/2
        for line in lines:
            d.text((x+(w-d.textlength(line,font=FONT))/2,top),line,font=FONT,fill='#172B4D');top+=26
    for i,(a,b,label,start,end,via) in enumerate(p['edges']):
        assert a in p['nodes'] and b in p['nodes']
        xy={'top':(.5,0),'bottom':(.5,1),'left':(0,.5),'right':(1,.5)}
        sx,sy=xy[start];ex,ey=xy[end]
        style=f'edgeStyle=orthogonalEdgeStyle;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#53677F;strokeWidth=2;fontSize=18;labelBackgroundColor=#FFFFFF;exitX={sx};exitY={sy};entryX={ex};entryY={ey};exitDx=0;exitDy=0;entryDx=0;entryDy=0;'
        cell=ET.SubElement(root,'mxCell',id=f'e{i}',value=label,style=style,edge='1',parent='1',source=a,target=b)
        geom=ET.SubElement(cell,'mxGeometry',relative='1',attrib={'as':'geometry'})
        if via:
            arr=ET.SubElement(geom,'Array',attrib={'as':'points'})
            for x,y in via: ET.SubElement(arr,'mxPoint',x=str(x),y=str(y))
        pts=[anchor(p['nodes'][a],start),*via,anchor(p['nodes'][b],end)]
        d.line(pts,fill='#53677F',width=3)
        x,y=pts[-1];prev=pts[-2];angle=math.atan2(y-prev[1],x-prev[0])
        d.polygon([(x,y),(x-13*math.cos(angle-.45),y-13*math.sin(angle-.45)),(x-13*math.cos(angle+.45),y-13*math.sin(angle+.45))],fill='#53677F')
        if label:
            # Use the longest routed segment and keep labels within the page.
            left,right=max(zip(pts,pts[1:]),key=lambda pair: math.dist(*pair))
            x=(left[0]+right[0])/2;y=(left[1]+right[1])/2
            tw=d.textlength(label,font=SMALL)
            x=max(tw/2+20,min(1380-tw/2,x))
            d.rectangle((x-tw/2-4,y-13,x+tw/2+4,y+12),fill='white')
            d.text((x-tw/2,y-11),label,font=SMALL,fill='#172B4D')
    im.save(OUT/f'ShopStack-Future-State-Cart-{index:02}.png')
    counts.append((p['title'],len(p['nodes']),len(p['edges'])))
ET.indent(doc,space='  ')
ET.ElementTree(doc).write(OUT/'ShopStack-Future-State-Cart-Reviewed.drawio',encoding='utf-8',xml_declaration=True)
print('Generated 5 pages; all edge endpoints resolve; all node text fits:',counts)
