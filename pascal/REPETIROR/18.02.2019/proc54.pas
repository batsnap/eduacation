var a,b,c:integer;
function isleapyear(a:integer):boolean;
    begin
        if (a mod 4=0) and (a mod 100<>0) or (a mod 400=0) then
            isleapyear:=true
        else
            isleapyear:=false;
    end;
function monthdays(m,y:integer):integer;
    begin
        if not isleapyear(y) then
            begin
                if m=1 then monthdays:=31
                else if m=2 then monthdays:=28
                else if m=3 then monthdays:=31
                else if m=4 then monthdays:=30
                else if m=5 then monthdays:=31
                else if m=6 then monthdays:=30
                else if m=7 then monthdays:=31
                else if m=8 then monthdays:=31
                else if m=9 then monthdays:=30
                else if m=10 then monthdays:=31
                else if m=11 then monthdays:=30
                else if m=12 then monthdays:=31
            end
        else
            begin
            if m=1 then monthdays:=31
                else if m=2 then monthdays:=29
                else if m=3 then monthdays:=31
                else if m=4 then monthdays:=30
                else if m=5 then monthdays:=31
                else if m=6 then monthdays:=30
                else if m=7 then monthdays:=31
                else if m=8 then monthdays:=31
                else if m=9 then monthdays:=30
                else if m=10 then monthdays:=31
                else if m=11 then monthdays:=30
                else if m=12 then monthdays:=31
            end;
    end;
procedure prevdate(d,m,y:integer);
    begin
        if d<>1 then
            writeln(d-1,' ',m,' ',y)
        else
            begin
                if m<>1 then
                    writeln(monthdays(m-1,y),' ',m-1,' ',y)
                else
                    begin
                        writeln(monthdays(12,y-1),' ',12,' ',y-1)
                    end;
            end;
    end;
begin
//readln(a,b,c);
readln(a);
//prevdate(a,b,c);
write(isleapyear(a));
end.