var
   i,k:longint;
   slovo,itog:string;
begin
itog:='';
readln(slovo);
for i:=1 to length(slovo) do
   begin
      if i mod 2=0 then
         itog:=itog+slovo[i];
   end;
for i:=length(slovo) downto 1 do
   begin
      if i mod 2=1 then
         itog:=itog+slovo[i];
   end;
writeln(itog)
end.