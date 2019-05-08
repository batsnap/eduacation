var
    s:string;

function IsIdent(s:string):integer;
var
    simvol,buk,cifri:string;
    i:integer;
begin
    cifri:='1234567890';
    buk:='abcdefghijklmonpqrstuwxyz';
    simvol:='_';
    if s='' then 
        IsIdent:=-1 else
    if pos(s[1],cifri)<>0 then
        IsIdent:=-2 else
        for i:=1 to length(s) do
            if (pos(s[i],simvol)<>0) or (pos(s[i],buk)<>0) or (pos(s[i],cifri)<>0) then
                IsIdent:=0
            else
                begin
                    IsIdent:=i;
                    break
                end;
    
end;

begin
readln(s);
writeln(IsIdent(s));
end.
