import pcbnew
from pcbnew import LoadBoard,FOOTPRINT,wxPoint

MM=10**6      # 1mm

F_Cu = pcbnew.F_Cu
In1_Cu = pcbnew.In1_Cu
In2_Cu = pcbnew.In2_Cu
B_Cu = pcbnew.B_Cu

F_Paste = pcbnew.F_Paste
B_Paste = pcbnew.B_Paste

F_SilkS = pcbnew.F_SilkS
B_SilkS = pcbnew.B_SilkS

F_Mask = pcbnew.F_Mask
B_Mask = pcbnew.B_Mask

F_Fab = pcbnew.F_Fab
B_Fab = pcbnew.B_Fab

F_CrtYd = pcbnew.F_CrtYd
B_CrtYd = pcbnew.B_CrtYd

Edge_Cuts = pcbnew.Edge_Cuts

Margin = pcbnew.Margin

Dwgs_User = pcbnew.Dwgs_User
Cmts_User = pcbnew.Cmts_User


def get_position(item):
    return item.GetPosition()    

def set_position(item,point):  
    item.SetPosition(point)

def get_center(item):
    return item.GetCenter()

def point_new(point,dx,dy=0):
    x,y=point.x,point.y
    return wxPoint(x+dx*MM,y+dy*MM)

def point2MM(point):
    x,y=point.x,point.y
    return (x/MM,y/MM)

def get_footprint(board,fp_id):
    return board.FindFootprintByReference(fp_id)

def get_pad(footprint,pad_id):
    return footprint.FindPadByNumber(str(pad_id))

def get_angle(item):
    return item.GetOrientation()

def set_angle(item,num):
    return item.SetOrientation(num)

def draw_line(board,start, end, width=0.15, layer=F_SilkS): # 0.15mm

    segment = pcbnew.PCB_SHAPE(board)
    segment.SetShape(pcbnew.SHAPE_T_SEGMENT)
    segment.SetStart(start)
    segment.SetEnd(end)
    segment.SetLayer(layer)
    segment.SetWidth(int(width * pcbnew.IU_PER_MM))
    board.Add(segment)

def draw_box(board,start, end, width=0.15,layer=F_SilkS):
    segment = pcbnew.PCB_SHAPE(board)
    segment.SetShape(pcbnew.SHAPE_T_RECT)
    segment.SetStart(start)
    segment.SetEnd(end)
    segment.SetLayer(layer)
    segment.SetWidth(int(width * pcbnew.IU_PER_MM))
    board.Add(segment)

def draw_arc(board,start, center, angle=90,width=0.15, layer=F_SilkS): # 顺时针方向
    
    arc = pcbnew.PCB_SHAPE(board)
    arc.SetShape(pcbnew.SHAPE_T_ARC)
    arc.SetStart(start)
    arc.SetCenter(center)
    arc.SetArcAngleAndEnd(angle * 10, False)
    arc.SetLayer(layer)
    arc.SetWidth(int(width * pcbnew.IU_PER_MM))
    board.Add(arc)

def draw_track(board,start, end, width=0.15,layer=F_Cu):
    
    track = pcbnew.PCB_TRACK(board)
    track.SetStart(start)
    track.SetEnd(end)
    track.SetWidth(int(width*MM))
    track.SetLayer(layer)
    board.Add(track)

# horizJustify=1 :右边对齐；horizJustify=0 :居中对齐；horizJustify=-1 :左边对齐
def draw_text(board,text,point,horizJustify=1,angle=0,layer=F_SilkS,w=1,h=1,t=0.15): 

    segment = pcbnew.PCB_TEXT(board)
    segment.SetText(text)
    segment.SetPosition(point)
    segment.SetTextHeight(int(h*MM))
    segment.SetTextWidth(int(w*MM))
    segment.SetTextAngle(int(angle*10))
    segment.SetTextThickness(int(t*MM))
    segment.SetHorizJustify(horizJustify)
    segment.SetLayer(layer)
    board.Add(segment)

def test():
    filename="C:/Users/soy/Downloads/test/test.kicad_pcb"
    pcb = LoadBoard(filename)

    # draw_line(pcb,wxPoint(30*MM,30*MM),wxPoint(55*MM,67*MM),0.2)
    # draw_arc(pcb,wxPoint(0,0),wxPoint(30*MM,40*MM),120)
    # draw_arc(pcb,wxPoint(30*MM,40*MM),wxPoint(0,0),360)
    # draw_track(pcb,wxPoint(0,0),wxPoint(30*MM,40*MM))
    # draw_text(pcb,'000100',wxPoint(0,0),-1)

    footprint_id='J1'
    u304 = get_footprint(pcb,footprint_id)
    # u304 = pcb.FindFootprintByReference(footprint_id)

    for i in range(1,37):
        pad=get_pad(u304,i)
        center=get_center(pad)
        end=point_new(center,3)
        # draw_line(pcb,center,end,0.2,F_SilkS)
        draw_text(pcb,'PA'+str(i),end,-1)
    # point=get_position(u304)
    # print(point)
    # set_position(u304,point[0]+10.3,point[1]+16.51) # X: 10.3mm, Y: 16.51mm, 左上角为原点
    # print(get_position(u304))

    # print(get_angle(u304))
    # set_angle(u304,900)  # 90度, 逆时针方向为正
    # print(get_angle(u304))

    pcb.Save(filename)

if __name__=='__main__':
    print('run : ')
    print(pcbnew.IU_PER_MM)
    # test()
    filename="C:/Users/soy/Downloads/creeLED/creeLED.kicad_pcb"
    pcb = LoadBoard(filename)
    # draw_box(pcb,wxPoint(0,0),wxPoint(150*MM,100*MM),layer=Edge_Cuts)
    # draw_box(pcb,wxPoint(1.5*MM,1.5*MM),wxPoint(150*MM-1.5*MM,100*MM-1.5*MM),layer=Margin)
    for i in range(1,121):
        fp=get_footprint(pcb, 'D'+str(i))
        if i+10>120:
            continue
        # fp2=get_footprint(pcb, 'D'+str(i+10))
        # pad1=get_pad(fp,2)
        # pad2=get_pad(fp2,1)
        # p1=get_center(pad1)
        # p2=get_center(pad2)
        # draw_track(pcb,p1,p2,2.2)
        
        
        j=(i-1)//10
        k=(i-1)%10
        # set_position(fp,point_new(wxPoint(20*MM,14*MM),10*j,8*k))
        print(i)
    for i in range(1,21):
        fp=get_footprint(pcb, 'J'+str(i))
        j=(i-1)//10
        k=(i-1)%10
        # set_position(fp,point_new(wxPoint(7*MM,14*MM),136*j,8*k))
        c=get_position(fp)
        center=point_new(c,0,4)
        start=point_new(center,1)
        fp2=get_footprint(pcb, 'J'+str(i+20))
        set_position(fp2,center)
        # draw_arc(pcb,start,center,3600,0.1,Edge_Cuts)
        print(i)

    #     pad=get_pad(fp, i)
    #     link=pad.GetNet().GetNetname()
    #     c=get_center(pad) 
    #     s=point_new(c,0,6)
    #     draw_text(pcb, link.strip(' /'), s, horizJustify=-1,angle=90, layer=37, w=1, h=1, t=0.15)
        # draw_line(pcb,c,point_new(c,0,2))
        # if(i%5==0):
        #     draw_line(pcb,c,point_new(c,0,-2))
        #     draw_text(pcb, str(i), point_new(c,0,-3), horizJustify=0, layer=37, w=1.5, h=1.5, t=0.15)

    pcb.Save(filename)
