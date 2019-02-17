var h,m,s,t:integer;
procedure inctime(h,m,s,t:integer);
begin
s:=s+t;
if (s div 60=0) then
    writeln(h,m,s)
else
    begin
        t:=s div 60;
        s:=s mod 60;
        m:=m+t;
        if (m div 60=0) then
            writeln(h,m,s)
        else
            begin
                t:=m div 60;
                m:=m mod 60;
                h:=h+t;
                writeln(h,m,s);
            end;
    end;
end;
begin
read(h,m,s,t);
inctime(h,m,s,t);
end.