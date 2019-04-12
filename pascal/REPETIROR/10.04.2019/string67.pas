var
   i:longint;
   slovo,itog:string;
begin
itog:='';
readln(slovo);
for i:=1 to length(slovo) div 2 do
   begin
      itog:=itog+slovo[length(slovo)-i+1]+slovo[i];
   end;
writeln(itog)
end.
