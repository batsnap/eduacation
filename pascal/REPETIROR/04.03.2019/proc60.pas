var
   a,b,c,d,e,f,h1,h2,h3:real;
   i:integer;
function leng(x1,y1,x2,y2:real):real;
   begin
      leng:=sqrt(sqr(x1-x2)+sqr(y1-y2));
   end;
function perim(x1,y1,x2,y2,x3,y3:real):real;
   begin
      perim:=leng(x1,y1,x2,y2)+leng(x2,y2,x3,y3)+leng(x1,y1,x3,y3);
   end;
function area(x1,y1,x2,y2,x3,y3:real):real;
   var p:real;
   begin
      p:=perim(x1,y1,x2,y2,x3,y3)/2;
      area:=sqrt(p*(p-leng(x1,y1,x2,y2))*(p-leng(x2,y2,x3,y3))*(p-leng(x1,y1,x3,y3)));
   end;
function dist(x1,y1,x2,y2,x3,y3:real):real;
   var
      a,s:real;
   begin
      s:=area(x1,y1,x2,y2,x3,y3);
      a:=leng(x3,y3,x2,y2);
      dist:=((2*s)/a);
   end;
procedure altitudes(x1,y1,x2,y2,x3,y3,h1,h2,h3:real);
begin
   h1:=dist(x1,y1,x2,y2,x3,y3);
   h2:=dist(x2,y2,x1,y1,x3,y3);
   h3:=dist(x3,y3,x2,y2,x1,y1);
   writeln(h1:2:2);
   writeln(h2:2:2);
   writeln(h3:2:2);
end;
begin
   readln(a,b,c,d,e,f);
   altitudes(a,b,c,d,e,f,h1,h2,h3);
end.
