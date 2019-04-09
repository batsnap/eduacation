var
   slovar,slovar2,slovo,m:string;
   i,k,num:integer;
begin
k:=1;
i:=1;
readln(slovo);
slovar2:='1234567890';
slovar:='abcdefghijklmnopqrstuvwxyz';
while pos(slovo[k],slovar)=0 do
   k+=1;
m:=slovo[k];
writeln(m);
num:=k;
for i:=k+1 to length(slovo) do
   begin
      if pos(slovo[i],slovar2)=0 then
         if pos(slovo[i],slovar)>=pos(m,slovar) then
            m:=slovo[i]
         else
            begin
               k:=i;
               break
            end;       
   end;
if num=k then
   writeln(0)
else
   writeln(k)
   end.