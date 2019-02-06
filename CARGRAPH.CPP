#include<iostream.h>
#include<conio.h>
#include<graphics.h>
#include<dos.h>
void car()
{
	circle(100,25,25);
	setfillstyle(SOLID_FILL,RED);
	floodfill(100,25,15);
	for(int i=0;i<500;i++){
	//line(50,200,500,200);
	//line(50,280,500,280);
	line(50,240,500,240);
	//line(150,240,200,240);
	//line(250,240,300,240);
	//line(350,240,400,240);
	//line(450,240,500,240);
	//line(100,50,100,240);
	circle(180+i,230,10);
	//setfillstyle(SOLID_FILL,YELLOW);
       // 	floodfill(180,230,YELLOW);
	circle(230+i,230,10);
	arc(180+i,230,0,180,15);
	arc(230+i,230,0,180,15);
	line(195+i,230,215+i,230);
	line(145+i,230,165+i,230);
	line(245+i,230,265+i,230);
	line(145+i,230,145+i,210);
	line(265+i,230,265+i,210);
	line(145+i,210,155+i,210);
	line(265+i,210,255+i,210);
	line(155+i,210,170+i,190);
	line(255+i,210,240+i,190);
	line(170+i,190,240+i,190);
	line(165+i,210,176+i,194);
	line(245+i,210,234+i,194);
	line(176+i,194,234+i,194);
	line(165+i,210,245+i,210);
	line(205+i,194,205+i,210);
	delay(10);
	cleardevice();
	}


}

void main()
{
	clrscr();
	int gd= DETECT,gm;
	initgraph(&gd,&gm,"C:\\TURBOC3\\BGI");
	car();
	getch();
	closegraph();
}
