var a,b:integer;
function nod2(a,b:integer):integer;
        begin
        repeat
            if a>b then
                a :=a mod b
            else
                b:=b mod a;
        until (a=0)or(b=0);
        nod2:=a+b;
    end;
function nok1(a,b:integer):integer;
    begin
        nok1:=a*(b div nod2(a,b));
    end;

begin
read(a,b);
write(nok1(a,b));
end.