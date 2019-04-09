var
   i,k:longint;
   slovo,itog:string;
begin
k:=0;
itog:='';
readln(slovo);
for i:=1 to length(slovo) div 2 do
   begin
      itog:=itog+slovo[length(slovo)-k]+slovo[i];
      k+=1;
   end;
writeln(itog)
end.
