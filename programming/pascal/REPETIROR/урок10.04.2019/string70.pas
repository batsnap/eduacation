var
   slovo:string;
   num,num2,num3,i,osh:integer;
begin
osh:=0;
readln(slovo);
for i:=1 to length(slovo) do
   begin
      if slovo[i]='(' then
         num+=1;
      if slovo[i]=')' then
         num-=1;
      if slovo[i]='[' then
         num2+=1;
      if slovo[i]=']' then
         num2-=1;
      if slovo[i]='{' then
         num3+=1;
      if slovo[i]='}' then
         num3-=1;
      if ((num<0) or (num2<0) or (num3<0))and (osh=0) then
         osh:=i-1;
   end;
if osh<>0 then
   writeln(osh)
else
   if (num<0) or (num2<0) or (num3<0) then 
      writeln(-1)
   else
      writeln(0);
end.