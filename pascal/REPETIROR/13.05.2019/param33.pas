var
    h:string;
procedure LowCaseRus(var s:string);
var
    propis,stroch:string;
begin
    stroch:='абвгґдеєжзиіїйклмнопрстуфхцчшщьюя';
    propis:='АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ';
    for var i:integer:=1 to length(s) do
        if pos(s[i],propis)<>0 then
            s[i]:=stroch[pos(s[i],propis)];
end;

begin
readln(h);
LowCaseRus(h);
writeln(h);
end.