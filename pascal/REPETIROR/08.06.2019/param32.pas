var
    h:string;
procedure UpCaseRus(var s:string);
var
    propis,stroch:string;
begin
    stroch:='abcdefghijklmnopqrstuvwxyz';
    propis:='ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    for var i:integer:=1 to length(s) do
        if pos(s[i],stroch)<>0 then
            s[i]:=propis[pos(s[i],stroch)];
end;

begin
readln(h);
UpCaseRus(h);
writeln(h);
end.